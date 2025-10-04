# String Operations - All Problems Together
words = sentence.split()
rev_sentence = ' '.join([''.join(list(w)[::-1]) for w in words])
print("3. Reversed each word:", rev_sentence)


# 4. Count Uppercase and Lowercase Letters
upper_count = 0
lower_count = 0
for c in main_string:
if c.isupper():
upper_count += 1
elif c.islower():
lower_count += 1
print("4. Uppercase:", upper_count, "Lowercase:", lower_count)


# 5. Remove Punctuation
punctuations = "!()-[]{};:'\"\\,<>./?@#$%^&*_~"
no_punct = "".join([c for c in main_string if c not in punctuations])
print("5. Without punctuation:", no_punct)


# 6. Character Frequency Counter
freq = {}
for c in main_string.replace(" ", "").lower():
freq[c] = freq.get(c, 0) + 1
print("6. Character frequencies:", freq)


# 7. Replace Vowels with '*'
replace_vowels = "".join("*" if c in vowels else c for c in main_string)
print("7. Replace vowels:", replace_vowels)


# 8. Find the Longest Word in a Sentence
longest = ""
for w in sentence.split():
if len(w) > len(longest):
longest = w
print("8. Longest word:", longest)


# 9. Remove Duplicate Characters
result = ""
for c in main_string:
if c not in result:
result += c
print("9. After removing duplicates:", result)


# 10. Check for Anagram Strings
s1 = ''.join(main_string.split()).lower()
s2 = ''.join(second_string.split()).lower()
# Use sorting to compare—simple and clear for beginners
if sorted(s1) == sorted(s2):
print("10. Anagrams")
else:
print("10. Not Anagrams")
