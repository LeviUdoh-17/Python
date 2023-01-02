def Word_Count(word):
  statements = ["The quick brown fox jumped over the lazy dog", 
                "a brown dog and a lazy fox are similar in nature", 
                "Dami is so lazy that she could not make the effort to get brown sugar"]
  count = 0
  for statement in statements:
    count += statement.count(word)
  return count

count = Word_Count("brown")
print(count)
