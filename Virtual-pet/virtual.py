class Pet:

    # __init__ is called when a Pet object is created.
    # It creates the pet's basic attributes.
    def __init__(self, name, animal_type):
        # Store the pet's name and animal type.
        self.name = name
        self.animal_type = animal_type
        self.hunger = 5
        self.energy = 5

    # Feeding should reduce hunger by 1.
    def feed(self):
        self.hunger -= 1
        print(f"{self.name} enjoyed the food!")
        print(f"Hunger level: {self.hunger}")

   # Playing should increase hunger by 1 and reduce energy by 1.
    def play(self):
        self.hunger += 1
        self.energy -= 1
        print(f"{self.name} is playing!")
        print(f"Hunger level: {self.hunger}")
        print(f"Energy level: {self.energy}")

    # This method displays the pet's information.
    def status(self):
        print(f"--- {self.name} ---")
        print(f"Type: {self.animal_type}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")


# Create two pet objects.
pet1 = Pet("Milo", "Dog")
pet2 = Pet("Luna", "Cat")

# Show pet1's current information.
pet1.status()

# Feedings and play with pet1.
pet1.feed()
pet1.play()

# Show the pet's updated information.
pet1.status()

       