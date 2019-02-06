import animals
import dogpark

rue = animals.lab("Rue")

#rue.speak()
rue.food('treat')
rue.food('spinach')
#rue.knows_name("Does Rue know her name now?")
print(rue.name)
rue.count_barks()
vegas = animals.Dog("Vegas")
print(vegas.name)
vegas.count_barks()
rue.count_barks()
eastside = dogpark.DogPark([rue,vegas])
eastside.rollcall()
eastside.converse()
#whisk = animals.Cat("whiskers")
#print(whisk.mood, whisk.name)
#whisk.speak()
#whisk.mood = "happy"
#whisk.speak()