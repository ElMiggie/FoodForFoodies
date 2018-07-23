from models import Food

def seed_data():
    apple = Food(food_name = "Apple", recipe1Name = "Apple Empanadas", recipe2Name = "All-American Apple Pie", recipe3Name = "Danish Apple Cake", recipe4Name = "Apple Slaw", recipe5Name = "South African Apple Tart")
    peaches = Food(food_name = "Peaches")
    spaghetti = Food(food_name = "Spaghetti")

    apple.put()
