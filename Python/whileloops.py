import time
def blastoff():
    takeoff = 10
    while takeoff > 0:
        print(takeoff)
        time.sleep(1)
        takeoff -= 1
    print("Blastoff!")
#blastoff()

def magic(word):
    end = len(word)
    while end > 0:
        print(word[0:end])
        end -= 1
#magic("abararcadabara")

def count_chars(word, letter):
    index = 0
    letters = 0
    while index < len(word):
        if word[index] == letter:
            letters += 1
        index += 1
    return letters
#print(count_chars("bonobo", "o"))

def until_dot(words):
    index = 0
    while index < len(words) and words[index] != ".":
        index += 1
    return words[0:index]
#print(until_dot('Udacity.com'))

def is_substring(part, word):
    index = 0
    count = 0
    while index < len(word):
        if word[index : index + len(part)] == part:
           count += 1
        index += len(part)
    return count    
#print(is_substring('bad', 'abracadabra'))
#print(is_substring('dab', 'abracadabra'))
#print(is_substring('love', 'love, love, love, all you need is love'))
#print(is_substring('AA','AAAA'))

def locate_first(target, whole):
    index = 0
    found = []
    while index < len(whole):
        if whole[index : index + len(target)] == target:
            found.append(index)
        index += 1
    return found
print(locate_first('ook', 'cookbook'))
print(locate_first('base', 'all your bass are belong to us'))