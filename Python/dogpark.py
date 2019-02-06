import animals

class DogPark:
    def __init__(self, dogs):
        self.dogs = dogs
    
    def rollcall(self):
        print("Dogs in park: ")
        for dog in self.dogs:
            print(f" {dog.name}")
        print()
    
    def shout(self, words):
        for dog in self.dogs:
           dog.knows_name(words)
    
    def converse(self):
        self.rollcall()
        while True:
            words = input("Talk to doggos! ('quit' to quit) > ")
            if 'quit' in words:
                print("Bye!")
                break
            else:
                self.shout(words)

if __name__ == '__main__':
    dogs = [animals.lab("Toklat"),
            animals.chihuahua("Scrappy"),
            animals.husky("Barrett")]
    park = DogPark(dogs)
    park.converse()
    

