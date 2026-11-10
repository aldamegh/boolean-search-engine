"""A deterministic portfolio example using fictional documents only."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from search_engine import boolean_search, create_index


def main():
    corpus = ["apple tv", "samsung tv", "sony tv", "apple samsung"]
    index = create_index(corpus)
    print("Synthetic documents (zero-based IDs)")
    for doc_id, text in enumerate(corpus):
        print(f"  {doc_id}: {text}")
    print("\nBoolean queries")
    for query in ["apple", "apple & tv", "samsung sony&tv", "missing"]:
        print(f"  {query:<20} -> {boolean_search(query, index)}")
    print("\nWhitespace = OR; & = AND; AND is evaluated first.")


if __name__ == "__main__":
    main()
