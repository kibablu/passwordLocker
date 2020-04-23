#!/usr/bin/env python3
class Restaurant():
    def __init__(self, restaurantName, cuisineType):
        self.restaurantName = restaurantName # attributes
        self.cuisineType = cuisineType

    def describeRestaurant(self): # method
        print(self.restaurantName.title() + " is offering varieties of foods")

    def openRestaurant(self):
        print(self.restaurantName.title() + " is now opened at 5pm")

favourateRestaurant = Restaurant("sukhadia", "indian") # instance of a class Restaurant
bestRestaurant = Restaurant("osteria del chianti", "italian")
cheapRestaurant = Restaurant("La belle Époque french restaurant", "french")

print("\nMy favourite restaurant is " + favourateRestaurant.restaurantName.title() + ".") # callng attributes 
print("My favourite food is " + favourateRestaurant.cuisineType.title() + "\n")

print("\nMy best restaurant is " + bestRestaurant.restaurantName.title() + ".")
print("My best food is " + bestRestaurant.cuisineType.title() + "\n")

print("\nMy cheap restaurant is " + cheapRestaurant.restaurantName.title() + ".")
print("My cheap food is " + cheapRestaurant.cuisineType.title() + "\n")

favourateRestaurant.describeRestaurant() # calling method openRestaurant
bestRestaurant.describeRestaurant()
cheapRestaurant.describeRestaurant()