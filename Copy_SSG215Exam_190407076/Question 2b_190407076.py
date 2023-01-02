def exists_in_statement(word, statements):
  return any(word in statement for statement in statements)

statements = ["The quick brown fox jumped over the lazy dog", "a brown dog and a lazy fox are similar in nature", "Dami is so lazy that she could not make the effort to get brown sugar"]

word = "brown"



if exists_in_statement(word, statements):
  print(f"The word '{word}' exists in at least one of the statements.")
else:
  print(f"The word '{word}' does not exist in any of the statements.")

