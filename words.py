words = ["can","i","Ethan","live","toast","eVen"]
starts = ["l", "t"]

def print_upper_words(words, starts_with):
"""Print each word that starts with the given letters, in uppercase on seperate lines """
    for word in words:
        for start in starts_with:
            if word.startswith(start):
                print(word.upper())

print_upper_words(words, starts)