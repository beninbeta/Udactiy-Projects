def password_check(password):
    return len(password) > 7 and len(password) <=64

#print(password_check("hello"))
#print(password_check("How's it going today?"))
#print(password_check("1234567890101112131415161718192021222324252627282930313233343536373839"))

def total_length(list):
    total_length = 0;
    for item in list:
        total_length += len(item)
    return total_length

print(total_length(['foo', 'bar']))
print(total_length([]))