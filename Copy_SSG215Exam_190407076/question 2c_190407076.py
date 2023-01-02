def contains_fox(statement):
  if "fox" in statement:
    return True
  else:
    return False

# Test the function with the three given sentences
print(contains_fox("The quick brown fox jumped over the lazy dog")) #It should return True
print(contains_fox("a brown dog and a lazy fox are similar in nature")) #It should return True
print(contains_fox("Dami is so lazy that she could not make the effort to get brown sugar")) # It should return false
