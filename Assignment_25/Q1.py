# Develop a function that takes a text and a list of forbidden words. Replace all
# occurrences of these forbidden words with asterisks (*) using regular expressions.

import re

def replace_forbidden_words(text, forbidden_words):

    pattern = r'\b(' + '|'.join(map(re.escape, forbidden_words)) + r')\b'

    result = re.sub(pattern, lambda match: '*' * len(match.group()), text)

    return result


text = input("Enter text: ")

forbidden_words = ["bad", "stupid", "ugly"]

result = replace_forbidden_words(text, forbidden_words)

print("Result:", result)
