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
            'food_image_url': foodImages[foodIndex]
        })
        self.response.write(html)

class RandomFoodHandler(webapp2.RequestHandler):
    def get(self):
        apples = models.Food(food_name = "Apples", recipe1Name = "Apple Empanadas", recipe2Name = "All-American Apple Pie", recipe3Name = "Danish Apple Cake", recipe4Name = "Apple Slaw", recipe5Name = "South African Apple Tart")
        peaches = models.Food(food_name = "Peaches", recipe1Name = "Postre Chaja Peach Meringue Cake", recipe2Name = "Peach Cobbler", recipe3Name = "Gooey Peach Dumplings", recipe4Name = "Peach Chicken", recipe5Name = "Peach Phirini")
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
        if recipestuff:
            recipeinfo=recipestuff[0]
        else:
            self.response.write('%s Not Found' % recipe_name)
            return
        recipestemplate=jinja_current_dir.get_template("templates/results.html")
        html=recipestemplate.render({
        "recipename": recipeinfo.name_displayed,
        # BELOW IS THE LINE FOR THE RECIPEINFO THE CORRECT VERSION
        # "recipename": recipeinfo.name_displayed,
        "imagesource": recipeinfo.picture,
        #"search-input":self.request.get()
        "recipes":recipestuff,
        "search_food": recipe_name,
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
        apple_info = food(name_of_food="apple", food_name = "Apple", calories = 95, fats = 0.2, sodium = 2, carbs = 25, servingSize = "1 medium apple", calFromFat= 0, satFat= 0, transFat= 0, cholesterol= 0, dietaryFiber= 3, sugars= 8,
        protein= 0, vitaminA= 2, vitaminC= 14, calcium= 1, iron= 1 )

        apples_info = food(name_of_food="apples", food_name = "Apple", calories = 95, fats = 0.2, sodium = 2, carbs = 25, servingSize = "1 medium apple", calFromFat= 0, satFat= 0, transFat= 0, cholesterol= 0, dietaryFiber= 3, sugars= 8,
        protein= 0, vitaminA= 2, vitaminC= 14, calcium= 1, iron= 1 )
        apple_pie_info = food(name_of_food="apple pie", food_name = "Apple Pie", calories = 243, fats = 10, sodium = 111, carbs = 36.8, servingSize = "111 g", calFromFat= 90, satFat= 1.3, transFat= 0, cholesterol= 0, dietaryFiber= 5.1, sugars= 11.7,
        protein= 4.6, vitaminA= 3, vitaminC= 8, calcium= 1, iron= 9 )
        apple_empanadas_info = food(name_of_food="apple empanadas", food_name = "Apple Empanadas", calories = 280, fats =13, sodium = 260, carbs = 38, servingSize = " 1 empanada (85g)", calFromFat= 117, satFat= 3.5, transFat= 0, cholesterol= 5, dietaryFiber= 1, sugars= 15,
        protein= 3, vitaminA= 0, vitaminC= 6, calcium= 4, iron= 8 )
        danish_apple_cake_info = food(name_of_food="danish apple cake", food_name = "Danish Apple Cake", calories = 150, fats = 6, sodium = 190, carbs = 22, servingSize = "55 g", calFromFat= 24, satFat= 3, transFat= 0, cholesterol= 5, dietaryFiber= 1, sugars= 5,
        protein= 3, vitaminA= 0, vitaminC= 0, calcium= 2, iron= 4 )
        apple_slaw_info = food(name_of_food="apple slaw", food_name = "Apple Slaw", calories = 20, fats = 1, sodium = 12, carbs = 2, servingSize = "1 portion", calFromFat= 4, satFat= 0, transFat= 0, cholesterol= 0, dietaryFiber= 1, sugars= 1,
        protein= 0, vitaminA= 0, vitaminC= 0, calcium= 0, iron= 0 )
        southAfrica_apple_tart_info = food(name_of_food="south african apple tart", food_name = "South African Apple Tart", calories = 300, fats = 16, sodium = 60, carbs = 56, servingSize = "1 tart", calFromFat= 64, satFat= 8, transFat= 0, cholesterol= 85, dietaryFiber= 2, sugars= 26,
        protein= 6, vitaminA= 9, vitaminC= 4, calcium= 3, iron= 21 )

        apple_info.put()
        apple_pie_info.put()
        apple_empanadas_info.put()
        danish_apple_cake_info.put()
        apple_slaw_info.put()
        southAfrica_apple_tart_info.put()
####peaches
        peach_info = food(name_of_food="peach", food_name = "Peach", calories = 60, fats =0.4, sodium = 0, carbs = 16.7, servingSize = "1 peach", calFromFat= 1.6, satFat= 0, transFat= 0, cholesterol= 0, dietaryFiber= 2.3, sugars= 13,
        protein= 1.4, vitaminA= 7, vitaminC= 1, calcium= 1, iron= 1 )
        postre_chaja_peach_meringue_cake_info = food(name_of_food="postre chaja peach meringue cake", food_name = "Postre Chaja Peach Meringue Cake", calories = 490, fats =30, sodium = 19, carbs = 47, servingSize = "100 gram", calFromFat= 120, satFat= 11, transFat= 0, cholesterol= 56, dietaryFiber= 4, sugars= 40,
        protein= 6, vitaminA= 10, vitaminC= 2, calcium= 6, iron= 12 )
        peach_cobbler_info = food(name_of_food="peach cobbler", food_name = "Peach Cobbler", calories = 250, fats =10, sodium = 150, carbs = 38, servingSize = "4 oz.", calFromFat= 40, satFat= 5, transFat= 0, cholesterol= 0, dietaryFiber= 1, sugars= 25,
        protein= 2, vitaminA= 2, vitaminC= 6, calcium= 0, iron= 4 )
        gooey_peach_dumpling_info = food(name_of_food="gooey peach dumpling", food_name = "Gooey Peach Dumplings", calories = 70, fats =3, sodium = 116, carbs = 12, servingSize = "1 cup", calFromFat= 12, satFat= 0, transFat= 0, cholesterol= 0, dietaryFiber= 0, sugars= 0,
        protein= 1, vitaminA= 0, vitaminC= 0, calcium= 0, iron= 0 )
        peach_chicken_info = food(name_of_food="peach chicken", food_name = "Peach Chicken", calories = 144 , fats = 2, sodium = 275, carbs = 12, servingSize = "4 oz.", calFromFat= 8, satFat= 1, transFat= 0, cholesterol= 48, dietaryFiber= 1, sugars= 0,
        protein= 18, vitaminA= 2, vitaminC= 3, calcium= 0, iron= 3 )

        peach_info.put()
        postre_chaja_peach_meringue_cake_info.put()
        peach_cobbler_info.put()
        gooey_peach_dumpling_info.put()
        peach_chicken_info.put()
####Zucchini
        zucchini_info = food(name_of_food="zucchini", food_name = "Zucchini", calories = 33, fats = 0.6, sodium = 0, carbs = 5, servingSize = "1 medium zucchini", calFromFat= 0, satFat= 0, transFat= 0, cholesterol= 0, dietaryFiber= 2, sugars= 3,
        protein= 2, vitaminA= 10, vitaminC= 56, calcium= 13, iron= 12 )

        zucchini_info.put()
####Pizza
        cheese_pizza_info = food(name_of_food="cheese pizza", food_name = "Cheese Pizza", calories = 232, fats =10, sodium = 551, carbs = 33, servingSize = "1 slice", calFromFat= 40, satFat= 0, transFat= 0, cholesterol= 22, dietaryFiber= 2, sugars= 4,
        protein= 12, vitaminA= 10, vitaminC= 8, calcium= 25, iron= 10 )
        pepperoni_pizza_info = food(name_of_food="pepperoni pizza", food_name = "Pepperoni Pizza ", calories = 276, fats =17, sodium = 632, carbs = 32, servingSize = "1 slice", calFromFat= 68, satFat= 0, transFat= 0, cholesterol= 30, dietaryFiber= 3, sugars= 8,
        protein= 16, vitaminA= 6, vitaminC= 0, calcium= 26, iron= 12 )

        cheese_pizza_info.put()
        pepperoni_pizza_info.put()
####shrimp
        shrimp_info = food(name_of_food="shrimp", food_name = "Shrimp", calories = 76, fats = 1, sodium = 699, carbs = 1, servingSize = "3 oz.", calFromFat= 68, satFat= 0, transFat= 0, cholesterol= 30, dietaryFiber= 3, sugars= 8,
        protein= 15, vitaminA= 7, vitaminC= 0, calcium= 6, iron= 1 )
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
            "recipe_food_name": nutritionInfo.name_of_food,
            'food_calories': nutritionInfo.calories,
            'food_fats': nutritionInfo.fats,
            'food_sodium' : nutritionInfo.sodium,
            'food_carbs': nutritionInfo.carbs,
            'food_image_url': foodImageList[requestedFood]
            })
            self.response.write(html)
        else:
            self.response.write("Not Found!")

class InfoHandlerforLinks (webapp2.RequestHandler):
    def get(self, search_food):
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
        requestedFood = search_food
        nutritionInfoList = food.query().filter(models.Nutrition.food_name== requestedFood).fetch()
        if nutritionInfoList:
            nutritionInfo = nutritionInfoList[0]
            html = food_list_template.render({
            "search_food": nutritionInfo.food_name,
            'food_name': nutritionInfo.food_name,
            "recipe_food_name": nutritionInfo.name_of_food,
            'food_calories': nutritionInfo.calories,
            'food_fats': nutritionInfo.fats,
            'food_sodium' : nutritionInfo.sodium,
            'food_carbs': nutritionInfo.carbs,
            'food_image_url': foodImageList[nutritionInfo.name_of_food]
            })
            self.response.write(html)
        else:
            self.response.write("Not Found!")
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/random', RandomFoodHandler),
    ('/nutrition', InfoHandler),
    ('/nutritionentry',InfoEntryHandler),
    ('/info/(.*)', InfoHandlerforLinks),
    #('/recipes', RecipeHandler),
    ('/recipeentry', RecipeEntryHandler),
    ("/recipes/(.*)", RecipeHandler)
    ], debug=True)
