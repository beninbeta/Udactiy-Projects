def builtins():
    tale ="I really love chocolatey chocolate!"
    print("choc" in tale)
    print(tale.find("chocolate"))
    print(tale.count("chocolate"))
#builtins()

def breakify(lines):
    return '<br>'.join(lines)

#print(breakify(["Haiku frogs in snow","A limerick came from Nantucket","Tetrametric drum-beats thrumming, Hiawathianic rhythm."]))

def replace_substring(string, search, replace):
    new_string = []
    index = 0
    while index < len(string):
        if string[index: index + len(search)] == search:
            new_string.append(replace)
            index += len(search)
        else:
            new_string.append(string[index])
            index += 1
    return "".join(new_string)
#print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
#print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
#print(remove_substring('I am NOT learning to code.', 'NOT '))
#print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
#print(replace_substring("The word 'definately' is definately often misspelled.", 'definately', 'definitely'))
