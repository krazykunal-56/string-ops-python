# string-ops-python

This repository contains a beginner-friendly Python program that solves **10 classic string problems** in one run. The program asks for inputs once and then prints all results step by step.

---

## Problems Covered

1. Count vowels and consonants
2. Check if a string is a palindrome
3. Reverse each word in a sentence
4. Count uppercase and lowercase letters
5. Remove punctuation from a string
6. Character frequency counter
7. Replace vowels with `*`
8. Find the longest word in a sentence
9. Remove duplicate characters
10. Check if two strings are anagrams

---

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/string-ops-python.git
   cd string-ops-python
   ```

2. Run the program:

   ```bash
   python main.py
   ```

3. Enter:

   * A main string (used in most problems)
   * A sentence (used in sentence-based problems)
   * A second string (used for the anagram check)

The program will display results for all 10 problems together.

---

## Example Run

**Input:**

```
Enter a string: HelloWorld!!
Enter a sentence: Python is amazing
Enter another string (for Anagram check): dlroWolleH
```

**Output:**

```
--- Results ---
1. Vowels: 3 Consonants: 7
2. Not Palindrome
3. Reversed each word: nohtyP si gnizama
4. Uppercase: 2 Lowercase: 8
5. Without punctuation: HelloWorld
6. Character frequencies: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
7. Replace vowels: H*ll*W*rld!!
8. Longest word: amazing
9. After removing duplicates: HeloWrd!
10. Anagrams
```

---

## Files

* `main.py` — Python program with all 10 string problems
* `README.md` — this documentation

---

## License

MIT License (you can change it if you prefer)
