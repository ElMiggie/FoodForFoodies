#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


### give each food a number and randomly pick a number and pull that id info
import webapp2
import random
import os
import jinja2
import models
import recipes


#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/welcome.html")
        randomFoodList = ["Apples", "Peaches", "Pomegranates", "Zucchini", "Shrimp"]
        foodImages = ["static/apples.png", "static/peaches.png", "static/pomegranate.png", "static/zucchini.png", "static/shrimp.png"]

        foodIndex = random.randint(0, 4)
        foods = models.Food.query().filter(models.Food.food_name==randomFoodList[foodIndex]).fetch()
        start_template = jinja_current_dir.get_template("templates/welcome.html")
        html = start_template.render({
            'food_name': randomFoodList[foodIndex],
            'recipe1Name': foods[0].recipe1Name,
            'recipe2Name': foods[0].recipe2Name,
            'recipe3Name': foods[0].recipe3Name,
            'recipe4Name': foods[0].recipe4Name,
            'recipe5Name': foods[0].recipe5Name,
            'food_image_url': foodImages[foodIndex],
            "goto1": recipes/foods[0].recipe1Name,
            "goto2": recipes/foods[0].recipe2Name,
            "goto3": recipes/foods[0].recipe3Name,
            "goto4": recipes/foods[0].recipe4Name,
            "goto5": recipes/foods[0].recipe5Name, 
        })
        self.response.write(html)

class RandomFoodHandler(webapp2.RequestHandler):
    def get(self):
        apples = models.Food(food_name = "Apples", recipe1Name = "Apple Empanadas", recipe2Name = "All-American Apple Pie", recipe3Name = "Danish Apple Cake", recipe4Name = "Apple Slaw", recipe5Name = "South African Apple Tart")
        peaches = models.Food(food_name = "Peaches", recipe1Name = "Postre Chaja Peach Meringue Cake", recipe2Name = "Peach Cobbler", recipe3Name = "Gooey Peach Dumplings", recipe4Name = "Peach Chicken", recipe5Name = "Peach Phrini")
        pomegranates = models.Food(food_name = "Pomegranates", recipe1Name = "Pomegranate Granita", recipe2Name = "Grilled Scallops with Pomegranate Brown Butter", recipe3Name = "Pomegranate Vinaigette Salad Dressing", recipe4Name = "Pomegranate and Onion Salad", recipe5Name = "Squash and Pomegranate Salad")
        zucchini = models.Food(food_name = "Zucchini", recipe1Name = "Corn and Zucchini Salad", recipe2Name = "Zucchini Stuffed with Lady Peas", recipe3Name = "Stuffed Italian Zucchini Boats", recipe4Name = "Spicy Asian Zucchini", recipe5Name = "Moroccan Chickpea and Zucchini Salad")
        shrimp = models.Food(food_name = "Shrimp", recipe1Name = "Peurvian Shrimp Paella", recipe2Name = "Bacon-Wrapped Buffalo Shrimp", recipe3Name = "Croatian Shrimp (Skampi Na Buzara)", recipe4Name = "Chinese Shrimp Stir Fry", recipe5Name = "Piri-Piri Style Shrimp")

        apples.put()
        peaches.put()
        pomegranates.put()
        zucchini.put()
        shrimp.put()

class RecipeEntryHandler(webapp2.RequestHandler):
    def get(self):
        recipes.get_recipes_directions()

class RecipeHandler (webapp2.RequestHandler):
    def get (self, recipe_name):
        # nameofrecipe=self.request.get(recipe1Name)
        # recipe_name=models.Food.query().filter(models.Food.)
        # nameoffood=recipes.get_link_url(self.request.url)
        recipestuff=models.Recipe.query().filter(models.Recipe.name_displayed==recipe_name).fetch()
        recipeinfo=recipestuff[0]
        recipestemplate=jinja_current_dir.get_template("templates/results.html")
        html=recipestemplate.render({
        "recipename": recipeinfo.name_displayed,
        # BELOW IS THE LINE FOR THE RECIPEINFO THE CORRECT VERSION
        # "recipename": recipeinfo.name_displayed,
        "imagesource": recipeinfo.picture,
        #"search-input":self.request.get()
        "recipes":recipestuff,
        "directions_array": recipestuff
        })
        self.response.write(html)
# class RecipeLinksHandler(webapp2.RequestHandler):
#     def get(self, recipe_name):
#         self.response.write("Hello " + recipe_name)

class InfoEntryHandler(webapp2.RequestHandler):
    def get(self):
        food = models.Nutrition
####Apple
        apple_info = food(name_of_food="apple", food_name = "Apple", calories = 95, fats = 0.2, sodium = 2, carbs = 25, servingSize = "1 apple", calFromFat= 0, satFat= 0, transFat= 0, cholesterol= 0, dietaryFiber= 3, sugars= 8,
        protein= 0, vitaminA= 10, vitaminC= 8, calcium= 20, iron= 45 )

        apples_info = food(name_of_food="apples", food_name = "Apple", calories = 95, fats = 0.2, sodium = 2, carbs = 25, servingSize = "1 apple", calFromFat= 0, satFat= 0, transFat= 0, cholesterol= 0, dietaryFiber= 3, sugars= 8,
        protein= 0, vitaminA= 10, vitaminC= 8, calcium= 20, iron= 45 )
##########Inputing the new nutrition facts
        apple_pie_info = food(name_of_food="apple pie", food_name = "Apple Pie", calories = 230, fats = 10, sodium = 170, carbs = 33 )
        apple_empanadas_info = food(name_of_food="apple empanadas", food_name = "Apple Empanadas", calories = 230, fats =7, sodium = 200, carbs = 40 )
        danish_apple_cake_info = food(name_of_food="danish apple cake", food_name = "Danish Apple Cake", calories = 380, fats = 15, sodium = 262, carbs = 58 )
        apple_slaw_info = food(name_of_food="apple slaw", food_name = "Apple Slaw", calories = 125, fats = 0 , sodium = 0, carbs = 0 )
        southAfrica_apple_tart_info = food(name_of_food="south african apple tart", food_name = "South African Apple Tart", calories = 332, fats = 20.5, sodium = 5.3, carbs = 39 )

        apple_info.put()
        apple_pie_info.put()
        apple_empanadas_info.put()
        danish_apple_cake_info.put()
        apple_slaw_info.put()
        southAfrica_apple_tart_info.put()
####peaches
        peach_info = food(name_of_food="peach", food_name = "Peach", calories = 59, fats =0.4, sodium = 0, carbs = 14 )
        postre_chaja_peach_meringue_cake_info = food(name_of_food="postre chaja peach meringue cake", food_name = "Postre Chaja Peach Meringue Cake", calories = 422, fats =28.3, sodium = 158.5, carbs = 38.9 )
        peach_cobbler_info = food(name_of_food="peach cobbler", food_name = "Peach Cobbler", calories = 250, fats =10, sodium = 150, carbs = 38 )
        gooey_peach_dumpling_info = food(name_of_food="gooey peach dumpling", food_name = "Gooey Peach Dumplings", calories = 154.7, fats =5.5, sodium = 313.7, carbs = 24.8 )
        peach_chicken_info = food(name_of_food="peach chicken", food_name = "Peach Chicken", calories = 840 , fats = 29, sodium = 1280, carbs = 9 )

        peach_info.put()
        postre_chaja_peach_meringue_cake_info.put()
        peach_cobbler_info.put()
        gooey_peach_dumpling_info.put()
        peach_chicken_info.put()
####Zucchini
        zucchini_info = food(name_of_food="zucchini", food_name = "Zucchini", calories = 33, fats = 0.6, sodium = 16, carbs = 6 )

        zucchini_info.put()
####Pizza
        cheese_pizza_info = food(name_of_food="cheese pizza", food_name = "Cheese Pizza", calories = 277, fats =10, sodium = 565, carbs = 36 )
        pepperoni_pizza_info = food(name_of_food="pepperoni pizza", food_name = "Pepperoni Pizza ", calories = 549, fats =21, sodium = 1538, carbs = 64 )

        cheese_pizza_info.put()
        pepperoni_pizza_info.put()
class InfoHandler(webapp2.RequestHandler):
    def get(self):
        food_list_template = jinja_current_dir.get_template("templates/foodlist.html")
        foodImageList = {
        "apple":"static/apples.png",
        "apples":"static/apples.png",
        "apple pie":"static/applepie.png",
        "apple empanadas":"static/appleempanadas.png",
        "danish apple cake":"static/danishapplecake.png",
        "apple slaw":"static/appleslaw.png",
        "south africa apple tart": "static/southafricaappletart.png",
####peach
        "peach":"static/peaches.png",
        "postre chaja peach meringue cake":"static/postrepeachmeringuecake.png",
        "peach cobbler":"static/peachcobbler.png",
        "gooey peach dumpling":"static/gooeypeachdumpling.png",
        "peach chicken":"static/peach chicken.png",
####Pizza
        "cheese pizza":"static/cheesepizza.png",
        "pepperoni pizza":"static/pepperonipizza.png",
        }

        food = models.Nutrition
        requestedFood = (self.request.get("search_food")).lower()
        nutritionInfoList = food.query().filter(models.Nutrition.name_of_food == requestedFood).fetch()
        if nutritionInfoList:
            nutritionInfo = nutritionInfoList[0]
            html = food_list_template.render({
            "search_food": nutritionInfo.food_name,
            'food_name': nutritionInfo.food_name,
            'food_calories': nutritionInfo.calories,
            'food_fats': nutritionInfo.fats,
            'food_sodium' : nutritionInfo.sodium,
            'food_carbs': nutritionInfo.carbs,
            'food_image_url': foodImageList[requestedFood]
            })
            self.response.write(html)
        else:
            self.response.write("Not Found!")



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/random', RandomFoodHandler),
    ('/nutrition', InfoHandler),
    ('/nutritionentry',InfoEntryHandler),
    #('/recipes', RecipeHandler),
    ('/recipeentry', RecipeEntryHandler),
    ("/recipes/(.*)", RecipeHandler)
    ], debug=True)
