def duplicate_count(text):
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])


print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
