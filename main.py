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
        start_template = jinja_current_dir.get_template("Templates/welcome.html")
        randomFoodList = ["Apple", "Peaches", "Pomegranate"]
        foodIndex = random.randint(0, 2)
        foods = models.Food.query().fetch()
        start_template = jinja_current_dir.get_template("templates/welcome.html")
        html = start_template.render({
            'food_name': randomFoodList[foodIndex],
            'recipe1Name': foods[foodIndex].recipe1Name,
            'recipe2Name': foods[foodIndex].recipe2Name,
            'recipe3Name': foods[foodIndex].recipe3Name,
            'recipe4Name': foods[foodIndex].recipe4Name,
            'recipe5Name': foods[foodIndex].recipe5Name
        })
        self.response.write(html)

class RandomFoodHandler(webapp2.RequestHandler):
    def get(self):
        apple = models.Food(food_name = "Apple", recipe1Name = "Apple Empanadas", recipe2Name = "All-American Apple Pie", recipe3Name = "Danish Apple Cake", recipe4Name = "Apple Slaw", recipe5Name = "South African Apple Tart")
        peaches = models.Food(food_name = "Peaches", recipe1Name = "Postre Chaja Peach Meringue Cake", recipe2Name = "Peach Cobbler", recipe3Name = "Gooey Peach Dumplings", recipe4Name = "Peach Chicken", recipe5Name = "Peach Phrini")
        pomegranate = models.Food(food_name = "Pomegranate", recipe1Name = "Pomegranate Granita", recipe2Name = "Grilled Scalops with Pomegranate Brown Butter", recipe3Name = "Indo-European Pomegranate Molasses", recipe4Name = "Pomegranate and Onion Salad", recipe5Name = "Squash and Pomegranate Salad")

        apple.put()
        peaches.put()
        pomegranate.put()


class RecipeHandler (webapp2.RequestHandler):
    def get (self):
        recipes=jinja_current_dir.get_template("templates/results.html")
        html=recipes.render({})
        self.response.write(html)



class InfoHandler(webapp2.RequestHandler):
    def get(self):
        food_list_template = jinja_current_dir.get_template("templates/foodlist.html")
        apple_pie = models.Nutrition(calories = "230", fats ="10g", sodium = "170mg", carbs = "33g" )
        #food_query = model.Nutrition.query().order()
        #person_query = model.Facebook.query().filter(model.Nutrition.name == 'raw_input()')
        #all_food = person_query.fetch()
        #info = models.Nutrition.query().fetch()
        html = food_list_template.render({
        'food_name': "Apple Pie",
        'food_calories': apple_pie.calories,
        'food_fats': apple_pie.fats,
        'food_sodium' : apple_pie.sodium,
        'food_carbs': apple_pie.carbs,
        })
        self.response.write(html)
        apple_pie.put()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/random', RandomFoodHandler),
    ('/nutrition', InfoHandler),
    ('/recipes', RecipeHandler)
    ], debug=True)
