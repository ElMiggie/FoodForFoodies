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


#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/welcome.html")
        randomFoodList = ["Apples", "Peaches", "Pomegranates", "Zucchini"]
        foodImages = ["static/apple.jpg", "static/peaches.jpg", "static/pomegranate.jpg", "static/zucchini.jpg"]

        foodIndex = random.randint(0, 3)
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
        zucchini = models.Food(food_name = "Zucchini", recipe1Name = "1", recipe2Name = "2", recipe3Name = "3", recipe4Name = "4", recipe5Name = "5")

        apples.put()
        peaches.put()
        pomegranates.put()
        zucchini.put()

class RecipeEntryHandler(webapp2.RequestHandler):
    def get(self):
        directions_array=["Heat oven to 425F. Prepare Double-Crust Pastry", "Mix sugar, flour, cinnamon, nutmeg and salt in large bowl. Stir in apples. Turn into pastry-lined pie plate. Dot with butter. Trim overhanging edge of pastry 1/2 inch from rim of plate", "Roll other round of pastry. Fold into fourths and cut slits so steam can escape. Unfold top pastry over filling; trim overhanging edge 1 inch from rim of plate. Fold and roll top edge under lower edge, pressing on rim to seal; flute as desired. Cover edge with 3-inch strip of aluminum foil to prevent excessive browning. Remove foil during last 15 minutes of baking", "Bake 40 to 50 minutes or until crust is brown and juice begins to bubble through slits in crust. Serve warm if desired."]
        ingredients_array=["1/3 to 1/2 cup sugar", "1/4 cup Gold Medal all-purpose flour", "1/2 teaspoon ground cinnamon", "1/2 teaspoon ground nutmeg", "1/8 teaspoon salt", "8 cups thinly sliced peeled tart apples (8 medium)", "2 tablespoons butter or margarine"]
        apple_pie= models.Recipe(food_name="apple_pie", ingredients=ingredients_array,
        directions=directions_array)
        apple_pie.put()

class RecipeHandler (webapp2.RequestHandler):
    def get (self):
        recipestuff=models.Recipe.query().filter(models.Recipe.food_name=="apple_pie").fetch()
        recipes=jinja_current_dir.get_template("templates/results.html")
        html=recipes.render({
        #"search-input":self.request.get()
        "recipes":recipestuff,
        "directions_array": recipestuff
        })
        self.response.write(html)

class InfoEntryHandler(webapp2.RequestHandler):
    def get(self):
        food = models.Nutrition
####Apple
        apple_info = food(food_name = "Apple", calories = "95", fats ="0.2 g", sodium = "2 mg", carbs = "25 g" )
        apple_pie_info = food(food_name = "Apple Pie", calories = "230", fats ="10 g", sodium = "170 mg", carbs = "33 g" )
        apple_empanadas_info = food(food_name = "Apple Empanadas", calories = "230", fats ="7 g", sodium = "200 mg", carbs = "40 g" )
        danish_apple_pie_info = food(food_name = "Danish Apple Pie", calories = "380", fats = "15 g", sodium = "262 mg", carbs = "58 g")
        apple_slaw_info = food(food_name = "Apple Slaw", calories = "125", fats = "0 g", sodium = "0 mg", carbs = "0 g")
        southAfrica_apple_tart_info = food(food_name = "South African Apple Tart", calories = "332", fats = "20.5 g", sodium = "5.3 mg", carbs = "39 g")

        apple_pie_info.put()
        apple_empanadas_info.put()
        danish_apple_pie_info.put()
        apple_slaw_info.put()
        southAfrica_apple_tart_info.put()
####peaches
        peach_info = food(food_name = "Peach", calories = "59", fats ="0.4 g", sodium = "0 mg", carbs = "14 g" )
        postre_chaja_peach_meringue_cake_info = food(food_name = "Postre Chaja Peach Meringue Cake", calories = "422", fats ="28.3 g", sodium = "158.5 mg", carbs = "38.9 g" )
        peach_cobbler_info = food(food_name = "Peach Cobbler", calories = "250", fats ="10 g", sodium = "150 mg", carbs = "38 g" )
        gooey_peach_dumpling_info = food(food_name = "Gooey Peach Dumplings", calories = "154.7", fats ="5.5 g", sodium = "313.7 mg", carbs = "24.8 g" )
        peach_chicken_info = food(food_name = "Peach Chicken", calories = "840", fats ="29 g", sodium = "1280 mg", carbs = "89 mg" )

        peach_info.put()
        postre_chaja_peach_meringue_cake_info.put()
        peach_cobbler_info.put()
        gooey_peach_dumpling_info.put()
        peach_chicken_info.put()

class InfoHandler(webapp2.RequestHandler):
    def get(self):
        food_list_template = jinja_current_dir.get_template("templates/foodlist.html")
        food = models.Nutrition
        #"search_food" : self.request.get("search_food")
        #apple_pie = food(food_name = "Apple Pie" , calories = "230", fats ="10g", sodium = "170mg", carbs = "33g" )
        #food_query = model.Nutrition.query().order()
        #person_query = model.Facebook.query().filter(model.Nutrition.name == 'raw_input()')
        #all_food = person_query.fetch()
        ###info = models.Nutrition.query().fetch()
        requestedFood = (self.request.get("search_food")).lower()
        nutritionInfoList = food.query().filter(models.Nutrition.food_name== requestedFood).fetch()
        if nutritionInfoList:
            nutritionInfo = nutritionInfoList[0]
            html = food_list_template.render({
            "search_food": nutritionInfo.food_name,
            'food_name': nutritionInfo.food_name,
            'food_calories': nutritionInfo.calories,
            'food_fats': nutritionInfo.fats,
            'food_sodium' : nutritionInfo.sodium,
            'food_carbs': nutritionInfo.carbs,
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
