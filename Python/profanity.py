#  Check for rude words from a list in a string of text 0.1
import string

rude_words = ["crap", "shit", "poop", "hell", "jerk", "crap"]

def check_string(line):
    rude_word_count = 0
    words = line.split(" ")
    for word in words:
        word = word.strip(string.punctuation).lower()
        print(word)
        if word in rude_words:
            rude_word_count += 1
            print(f"Rude word found: {word}")
    return rude_word_count

def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0
        for line in myfile:
            rude_count += check_string(line)
    
    if rude_count == 0:
        print("No Rude words Found!")
    else:
        print(f"There were {rude_count} rude words founds!")

if __name__ == '__main__':
    check_file("my_file.txt")