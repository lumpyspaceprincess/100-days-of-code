def generator(a, b):
    return b + " " + a


print("Welcome to the Band Name Generator")
pet = input("Type the name of your first pet and press ENTER:\n")
city = input("Type the name of the city you grew up in and press ENTER:\n")

print("Your band name could be: " + generator(pet, city))
