Author: Nicholas McComb

A simple tool for counting the frequency of any given word in a text file, implemented in Python through a custom hash table implementation (uses Python's built-in hash function)

To use (in command line):
  python freq-ct.py text
    where "text" is a Python-readable text file in the same directory (public domain text files of Alice's Adventures in Wonderland and A Tale of Two Cities included)
  From here, the program will run through the specified text file and count word frequency, then print out the number of unique words in the text and prompt the user for more input.
  Commands:
    word returns the number of times "word" appears in the text.
    -word removes "word" from the table.
    Just pressing "Enter" with no input ends the program.

This program ignores case (i.e. hello and Hello count as the same word) and treats words separated by an underscore as one word (i.e. hello_world is counted as one word).
