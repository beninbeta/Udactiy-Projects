class Dog:
    
    
    def __init__(self, name):
        self.name = name
        self.count = 0
    
    
    def speak(self):
        print("wuff")
    
    def food(self, food):
        foods = ['treat', 'carrot','sweet potato','kong']
        if food in foods:
            print("Yummy, I love that!")
        else:
            print("That's not something a princess would eat!")

    def knows_name(self, words):
        lower_words = words.lower()
        if self.name.lower() in lower_words:
            self.speak() # need to use the self. to call the function we want to use
    
    def count_barks(self):
        self.count += 1
        for barks in range(self.count):
            self.speak() 

class lab(Dog):
    origin = "New Foundland"

    def speak(self):
        print("mrrrrrrrr")

class chihuahua(Dog):
    origin = "Mexio"

    def speak(self):
        print("yip")

class husky(Dog):
    origin = "New Foundland"

    def speak(self):
        print("ummmmwaroo")

class Cat:
   
   def __init__(self, name):
       self.mood = "neutral"
       self.name = name
       
   def speak(self):
        if self.mood == "neutral":
          print("meow, meow!")
        elif self.mood == "happy":
            print("purrrrrr")
        else:
            print("Hisssss")
