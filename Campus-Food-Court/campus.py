class Campus:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.food_court = []

    def add_food_court(self, food_court):
        self.food_court.append(food_court)

    def get_food_courts(self):
        return self.food_court