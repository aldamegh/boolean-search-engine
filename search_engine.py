import cProfile
import json
import time

# Part (a): Inverted Index
def create_index(corpus):
    index = {}
    for doc_id, document in enumerate(corpus):
        for term in document.split():
            term = term.lower()  # Ensure case-insensitivity
            if term not in index:
                index[term] = [doc_id]
            elif doc_id not in index[term]:
                index[term].append(doc_id)
    return index

# Part (b): Boolean Search
def boolean_search(query, index):
    """Return sorted document IDs; AND binds more tightly than whitespace OR."""
    import re
    groups = re.sub(r"\s*&\s*", "&", query.strip()).split()
    result = set()
    for group in groups:
        terms = group.lower().split("&")
        if any(not term for term in terms):
            raise ValueError("AND requires a term on each side")
        matches = set(index.get(terms[0], []))
        for term in terms[1:]:
            matches.intersection_update(index.get(term, []))
        result.update(matches)
    return sorted(result)


def load_dataset(file_path):
    corpus = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            try:
                doc = json.loads(line)
                corpus.append(doc['short_description'])
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
            except KeyError:
                print(f"Key 'short_description' not found in document: {i+1}")



    return corpus






# Main function to run experiments
def run_experiments(file_path, queries):
    # Load the dataset and create the index
    corpus = load_dataset(file_path)
    index_creation_start_time = time.perf_counter()
    index = create_index(corpus)
    index_creation_time = (time.perf_counter() - index_creation_start_time) * 10**6  # Convert to microseconds
    print(f"Time taken to create index: {index_creation_time} microseconds")
    
    # Process each query and measure the time taken for search
    for query in queries:
        # Ensure spaces around '&' to separate terms correctly
        formatted_query = ' '.join(query.split()).replace("&", " & ").replace("  ", " ")
        search_start_time = time.time()
        
        try:
            results = boolean_search(formatted_query, index)
            search_time = (time.time() - search_start_time) * 10**6  # Convert to microseconds
            
            # Output results
            if results:
                print(f"Query: {formatted_query}")
                print(f"Number of results: {len(results)}")
                print(f"Time taken for search: {search_time} microseconds\n")
            else:
                print(f"Query: {formatted_query}")
                print("Number of results: 0")
                print(f"Time taken for search: {search_time} microseconds\n")
        
        except Exception as e:
            print(f"An error occurred while processing query '{formatted_query}': {e}")
            print(f"Time since search start: {(time.time() - search_start_time) * 10**6} microseconds\n")




def main():
    import argparse
    parser = argparse.ArgumentParser(description="Coursework Boolean search")
    parser.add_argument("--data", help="Optional JSONL file with short_description strings")
    parser.add_argument("queries", nargs="*", default=["apple", "samsung sony&tv"])
    args = parser.parse_args()
    if args.data:
        run_experiments(args.data, args.queries)
    else:
        corpus = ["apple tv", "samsung tv", "sony tv", "apple samsung"]
        index = create_index(corpus)
        for query in args.queries:
            print(query, "->", boolean_search(query, index))


if __name__ == "__main__":
    main()
