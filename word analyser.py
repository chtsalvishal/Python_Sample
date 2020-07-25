"""
Written by Gavin Kroeger for FIT9136
Started 1/04/2020
Last Editted 1/04/2020

A script for reading and analysing books from plain text
"""

# string is used to reference ascii chars and digits
import string


def read_book(name):
    # this line is important for project gutenberg books
    # since the encoding is UTF-8, without it some chars wont be displayed properly
    book = open(name, "r", encoding="UTF-8")

    content = book.readlines()

    book.close()

    return content


# removes the header by ignoring the lines before the *** of the book start
def remove_header(text):
    clean = []

    # flag used to see if the end of the header has been found
    header_found = False

    # keep searching for the header end, once found, copy over the rest
    # of the text
    for line in text:
        if header_found:
            clean.append(line)
        elif line[0:3] == "***":
            header_found = True

    return clean


# removes the post script by reading everything until it finds a ***
# Must be used AFTER the header is removed
def remove_post(text):
    clean = []

    i = 0

    # keep reading until either there are no more lines, OR the text
    # starts with ***
    while i < len(text) and text[i][0:3] != "***":
        clean.append(text[i])
        i += 1

    return clean


# makes all text lowercase
def make_lower(text):
    clean = []

    for line in text:
        clean.append(line.lower())

    return clean


# takes as input a single string that is the text and outputs the text
# containing only alpha numeric characters
def remove_punctuation(text):
    presentChars = set(text)

    for char in presentChars:
        if char not in string.ascii_lowercase and char not in string.digits:
            # make sure you don't remove spaces and new lines, or the text
            # cant be analysed
            if char != " " and char != "\n":
                text = text.replace(char, "")

    return text


# driver function to use all of the cleaning functions in the correct order
# takes as input a file name in this directory and outputs clean text as a string
def clean(name):
    book_text = read_book(name)
    book_text = remove_header(book_text)
    book_text = remove_post(book_text)
    book_text = make_lower(book_text)

    # turn our lists of strings into one string for punctuation cleaning
    book_text = "".join(book_text)
    book_text = remove_punctuation(book_text)

    return book_text


# uses a clean text to find the counts of each word used
# book_text must be a single string, and outputs a dictionary
def analyse(book_txt):
    # remove new lines for the sake of counting words
    split_text = book_txt.replace("\n", "")
    split_text = split_text.split(" ")

    counts = dict()

    # for every word, if word is in dictionary, increment by 1, if not, start
    # the word count at 1
    for word in split_text:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


book_text = clean("book.txt")

# open a new file to save the cleaned text. This is mostly for debugging
clean_file = open("clean.txt", "w", encoding="UTF-8")

# write each line, as the text should be a list of strings
for line in book_text:
    clean_file.write(line)

clean_file.close()

counts = analyse(book_text)

# make a file to output our counts
clean_analysis = open("clean_counts.txt", "w", encoding="UTF-8")

# for each word, make a formatted string to describe out counts
for word in counts:
    clean_analysis.write(str(word) + ":" + str(counts[word]) + "\n")

# never forget to close the file. The write happens when the file is closed.
clean_analysis.close()