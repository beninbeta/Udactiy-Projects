def starts_with(long, short):
    shortlen = 0
    for postition in range(len(short)):
        shortlen +=1    
    # Will produce index errors because position is out of bounds
    return long[shortlen-1] == short[shortlen-1]

def way_two(long, short):
    for postition in range(len(short)):
        if long[postition] != short[postition]:
            return False
    return True 

def way_three(long,short):
    return long[0:len(short)] == short   

print(starts_with("apple", "app"))
print(starts_with("zebonkey", "kiwi"))
print(way_two("apple", "app"))
print(way_two("zebonkey", "kiwi"))
print(way_three("zebonkey", "kiwi"))
print(way_three("apple", "app"))
#print(starts_with("tin", "tinkerbell"))
#print(way_two("tin", "tinkerbell"))
print(way_three("tin", "tinkerbell"))
print("banana".startswith("ban"))
print("bonobo".startswith("ban"))