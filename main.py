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
        foodImages = ["static/apple.jpg", "static/peaches.jpg", "static/pomegranate.jpg", "static/zucchini.png", "static/shrimp.jpg"]

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
        peaches = models.Food(food_name = "Peaches", recipe1Name = "Postre Chaja Peach Meringue Cake", recipe2Name = "Peach Cobbler", recipe3Name = "Gooey Peach Dumplings", recipe4Name = "Peach Chicken", recipe5Name = "Peach Phrini")
        pomegranates = models.Food(food_name = "Pomegranates", recipe1Name = "Pomegranate Granita", recipe2Name = "Grilled Scallops with Pomegranate Brown Butter", recipe3Name = "Indo-European Pomegranate Molasses", recipe4Name = "Pomegranate and Onion Salad", recipe5Name = "Squash and Pomegranate Salad")
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
    def get (self):
        # nameofrecipe=self.request.get(recipe1Name)
        # recipe_name=models.Food.query().filter(models.Food.)
        self.request.url
        if self.request.url=="/recipes/firstrecipe":
                namefood=apple_pie
        if self.request.url=="/recipes/secondrecipe":
                namefood=apple_empanadas
        if self.request.url=="/recipes/thirdrecipe":
                namefood="danish_apple_pie"
        if self.request.url=="/recipes/fourthrecipe":
                namefood="apple_slaw"
        if self.request.url=="/recipes/fifthrecipe":
                namefood="apple_tart"
        recipestuff=models.Recipe.query().filter(models.Recipe.food_name=="apple_slaw").fetch()
        recipeinfo=recipestuff[0]
        recipes=jinja_current_dir.get_template("templates/results.html")
        html=recipes.render({
        "recipename": recipeinfo.name_displayed,
        # BELOW IS THE LINE FOR THE RECIPEINFO THE CORRECT VERSION
        # "recipename": recipeinfo.name_displayed,
        "imagesource": recipeinfo.picture,
        #"search-input":self.request.get()
        "recipes":recipestuff,
        "directions_array": recipestuff
        })
        self.response.write(html)

class InfoEntryHandler(webapp2.RequestHandler):
    def get(self):
        food = models.Nutrition
####Apple
        apple_info = food(name_of_food="apple", food_name = "Apple", calories = "95", fats ="0.2 g", sodium = "2 mg", carbs = "25 g" )
        apple_pie_info = food(name_of_food="apple pie", food_name = "Apple Pie", calories = "230", fats ="10 g", sodium = "170 mg", carbs = "33 g" )
        apple_empanadas_info = food(name_of_food="apple empanadas", food_name = "Apple Empanadas", calories = "230", fats ="7 g", sodium = "200 mg", carbs = "40 g" )
        danish_apple_pie_info = food(name_of_food="danish apple pie", food_name = "Danish Apple Pie", calories = "380", fats = "15 g", sodium = "262 mg", carbs = "58 g")
        apple_slaw_info = food(name_of_food="apple slaw", food_name = "Apple Slaw", calories = "125", fats = "0 g", sodium = "0 mg", carbs = "0 g")
        southAfrica_apple_tart_info = food(name_of_food="south african apple tart", food_name = "South African Apple Tart", calories = "332", fats = "20.5 g", sodium = "5.3 mg", carbs = "39 g")

        apple_info.put()
        apple_pie_info.put()
        apple_empanadas_info.put()
        danish_apple_pie_info.put()
        apple_slaw_info.put()
        southAfrica_apple_tart_info.put()
####peaches
        peach_info = food(name_of_food="peach", food_name = "Peach", calories = "59", fats ="0.4 g", sodium = "0 mg", carbs = "14 g" )
        postre_chaja_peach_meringue_cake_info = food(name_of_food="postre chaja peach meringue cake", food_name = "Postre Chaja Peach Meringue Cake", calories = "422", fats ="28.3 g", sodium = "158.5 mg", carbs = "38.9 g" )
        peach_cobbler_info = food(name_of_food="peach cobbler", food_name = "Peach Cobbler", calories = "250", fats ="10 g", sodium = "150 mg", carbs = "38 g" )
        gooey_peach_dumpling_info = food(name_of_food="gooey peach dumpling", food_name = "Gooey Peach Dumplings", calories = "154.7", fats ="5.5 g", sodium = "313.7 mg", carbs = "24.8 g" )
        peach_chicken_info = food(name_of_food="peach chicken", food_name = "Peach Chicken", calories = "840", fats ="29 g", sodium = "1280 mg", carbs = "89 mg" )

        peach_info.put()
        postre_chaja_peach_meringue_cake_info.put()
        peach_cobbler_info.put()
        gooey_peach_dumpling_info.put()
        peach_chicken_info.put()

class InfoHandler(webapp2.RequestHandler):
    def get(self):
        food_list_template = jinja_current_dir.get_template("templates/foodlist.html")
        foodImageList = {"apple":"static/apple.jpg", "apple pie":"static/applepie.jpg" , "peach":"static/peaches.jpg"}
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
    ('/recipes', RecipeHandler),
    ('/recipeentry', RecipeEntryHandler)
    ], debug=True)
