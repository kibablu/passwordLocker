class Restaurant():
    def __init__(self, restaurantName, cuisineType):
        self.restaurantName = restaurantName # attributes
        self.cuisineType = cuisineType

    def describeRestaurant(self): # method
        print(self.restaurantName.title() + " is offering varieties of foods")

    def openRestaurant(self):
        print(self.restaurantName.title() + " is now opened at 5pm")

favourateRestaurant = Restaurant("Alphonso", "salad") # instance of a class Restaurant

print("My favourite restaurant is " + favourateRestaurant.restaurantName.title() + ".") # callng attributes 
print("My favourite food is " + favourateRestaurant.cuisineType.title() + "\n")

favourateRestaurant.describeRestaurant() # calling method openRestaurant
favourateRestaurant.openRestaurant() 