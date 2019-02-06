def start_K(word):
    if word[0] == 'K':
        return True
    else:
        return False

#print(start_K("Kelly"))

# And one like this should return False:
#print(start_K("Abe"))

def three_nums():
    n1 = int(input("Give me a number: "))
    n2 = int(input("Give me another: "))
    n3 = int(input("Please just one more: "))
    print(f"Your total is: {n1+n2+n3}")
three_nums()