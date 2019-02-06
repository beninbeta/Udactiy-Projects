favorites = {'color': 'purple', 'number': 42, 'animal': 'turtle', 'language': 'python'}

#for key, value in favorites.items():
    #print(f"My favorite {key} is {value}")

str = 'it appears that the the appears the most in the sentence'
dict = {}
words = str.split(' ')
for word in words:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1
for key, value in dict.items():
    print(f"'{key}' appears {value} times in this string")
