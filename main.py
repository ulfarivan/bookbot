from stats import get_word_count, get_char_counts, get_sorted_char_counts
import sys

def get_book_content(filepath):
  with open(filepath) as book:
    return book.read()

def print_report(filepath, word_count, char_counts):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  for item in char_counts:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["count"]}")

  print("============= END ===============")

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  filepath = sys.argv[1]
  book_content = get_book_content(filepath)
  word_count = get_word_count(book_content)
  char_counts = get_char_counts(book_content)
  sorted_char_counts = get_sorted_char_counts(char_counts)

  print_report(filepath, word_count, sorted_char_counts)

main()
