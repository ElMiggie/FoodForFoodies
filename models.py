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

from google.appengine.ext import ndb, ListProperty

class Food(ndb.Model):
  food_name = ndb.StringProperty(required=True)
  recipe1Name = ndb.StringProperty(required=True)
  recipe2Name = ndb.StringProperty(required=True)
  recipe3Name = ndb.StringProperty(required=True)
  recipe4Name = ndb.StringProperty(required=True)
  recipe5Name = ndb.StringProperty(required=True)


 class Recipe (ndb.Model):
    ingredients=ndb.ListProperty(required=True)
    directions=ndb.ListProperty(required=True)
class Nutrition(ndb.Model):
    calories = ndb.IntegerProperty(required=True)
    fats = ndb.IntegerProperty(required=True)
    carbs = ndb.IntegerProperty(required=True)
    sodium = ndb.IntegerProperty(required=True)
