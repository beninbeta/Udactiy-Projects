import os

with open("counting.txt", "w") as counting:
    for n in range(0,32,2):
        counting.write(f"{n}\n")



with open("dest.txt", "w") as destinataion:
    with open("counting.txt") as read:
        for line in read:
            destinataion.write(line)

