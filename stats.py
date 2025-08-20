def get_word_count(string):
  return len(string.split())

def get_char_counts(string):
  character_set = {}

  for char in string:
    l_char = char.lower()

    if l_char in character_set:
      character_set[l_char] += 1
    else:
      character_set[l_char] = 1

  return character_set

def get_sorted_char_counts(char_set):
  char_counts = []

  for char in char_set:
    char_counts.append({"char" : char, "count": char_set[char]})

  return sorted(char_counts, key=lambda item:item["count"], reverse=True)
