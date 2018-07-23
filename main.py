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


### give eah food a number and randomly pick a number and pull that id info
import webapp2
import random
import os
import jinja2
import models
from random_food_data import seed_data

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        randomFoodList = ["Apple", "Peaches", "Spaghetti"]
        foodOfDay = random.choice(randomFoodList)
        foods = models.Food.query().fetch()
        start_template = jinja_current_dir.get_template("templates/welcome.html")
        self.response.write(start_template.render({
        'food_name': foodOfDay,
        'recipe1Name': foods[0].recipe1Name,
        'recipe2Name': foods[0].recipe2Name,
        'recipe3Name': foods[0].recipe3Name,
        'recipe4Name': foods[0].recipe4Name,
        'recipe5Name': foods[0].recipe5Name,
        }))

class RandomFoodHandler(webapp2.RequestHandler):
    def get(self):
        apple = models.Food(food_name = "Apple", recipe1Name = "Apple Empanadas", recipe2Name = "All-American Apple Pie", recipe3Name = "Danish Apple Cake", recipe4Name = "Apple Slaw", recipe5Name = "South African Apple Tart")
        peaches = models.Food(food_name = "Peaches")
        spaghetti = models.Food(food_name = "Spaghetti")

        apple.put()

        pizza= models.Recipe(ingredients=["1/3 to 1/2 cup sugar", "1/4 cup Gold Medal all-purpose flour", "1/2 teaspoon ground cinnamon", "1/2 teaspoon ground nutmeg", "1/8 teaspoon salt", "8 cups thinly sliced peeled tart apples (8 medium)", "2 tablespoons butter or margarine"],
               directions=["Heat oven to 425ºF. Prepare Double-Crust Pastry", "Mix sugar, flour, cinnamon, nutmeg and salt in large bowl. Stir in apples. Turn into pastry-lined pie plate. Dot with butter. Trim overhanging edge of pastry 1/2 inch from rim of plate", "Roll other round of pastry. Fold into fourths and cut slits so steam can escape. Unfold top pastry over filling; trim overhanging edge 1 inch from rim of plate. Fold and roll top edge under lower edge, pressing on rim to seal; flute as desired. Cover edge with 3-inch strip of aluminum foil to prevent excessive browning. Remove foil during last 15 minutes of baking", "Bake 40 to 50 minutes or until crust is brown and juice begins to bubble through slits in crust. Serve warm if desired."]
         pizza.put()




# class FoodHandler(webapp2.RequestHandler):
#     def get(self):
#         start_template = jinja_current_dir.get_template("templates/welcome.html")
#         self.response.write(start_template.render())
#
#     def post(self):
#         the_fav_food = self.request.get('user-fav-food')
#
#         #put into database (optional)
#         food_record = Food(food_name = the_fav_food)
#         food_record.put()
#
#         #pass to the template via a dictionary
#         variable_dict = {'fav_food_for_view': the_fav_food}
#         end_template = jinja_current_dir.get_template("templates/results.html")
#         self.response.write(end_template.render(variable_dict))

# class ShowFoodHandler(webapp2.RequestHandler):
#     def get(self):
#         food_list_template = jinja_current_dir.get_template("templates/foodlist.html")
#         fav_foods = Food.query().order(-Food.food_name).fetch(3)
#         dict_for_template = {'top_fav_foods': fav_foods}
#         self.response.write(food_list_template.render(dict_for_template))


# class RecipeHandler(webapp2.RequestHandler):
#     def get(self):
#         food_list_template = jinja_current_dir.get_template("templates/foodlist.html")
#         # fav_foods = Food.query().order(-Food.food_name).fetch(3)
#         # dict_for_template = {'top_fav_foods': fav_foods}
#         # self.response.write(food_list_template.render(dict_for_template))
#         html = food_list_template.render({
#         'food_calories': self.response.,
#         'food_fats': self.response.,
#         'food_sodium': self.response.,
#         'food_carbs': self.response.,
#         )}

app = webapp2.WSGIApplication([
    ('/', FoodHandler),
    ('/nutrition', ShowFoodHandler)

          recipe_template=jinja_current_dir.get_template("templates/results.html")
          rendered_recipe=recipe_template.render({
          # 'recipe_picture': recipe_picture
          })
          self.response.write(rendered_recipe)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/random', RandomFoodHandler),
    # ('/', FoodHandler),
    # ('/showfavs', ShowFoodHandler),
    # ('/recipes', RecipeHandler)

], debug=True)
