import models

# 1=apple Pie
# 2=apple Empanadas
# 3=danish apple Pie
# 4=apple Tart
# 5=apple Slaw
# 6=shrimp Paella
# 7=bacon buffalo shrimp


def get_recipes_directions ():
    directions_array=["Heat oven to 425F. Prepare Double-Crust Pastry",
    "Mix sugar, flour, cinnamon, nutmeg and salt in large bowl.",
    "Stir in apples. Turn into pastry-lined pie plate. Dot with butter. Trim overhanging edge of pastry 1/2 inch from rim of plate",
    "Roll other round of pastry. Fold into fourths and cut slits so steam can escape. Unfold top pastry over filling; trim overhanging edge 1 inch from rim of plate.",
    "Fold and roll top edge under lower edge, pressing on rim to seal; flute as desired. Cover edge with 3-inch strip of aluminum foil to prevent excessive browning.",
    "Remove foil during last 15 minutes of baking",
    "Bake 40 to 50 minutes or until crust is brown and juice begins to bubble through slits in crust. Serve warm if desired."]

    ingredients_array=["1/3 to 1/2 cup sugar", "1/4 cup Gold Medal all-purpose flour", "1/2 teaspoon ground cinnamon",
    "1/2 teaspoon ground nutmeg", "1/8 teaspoon salt", "8 cups thinly sliced peeled tart apples (8 medium)",
     "2 tablespoons butter or margarine"]

    apple_pie= models.Recipe(name_displayed="Apple Pie", food_name="apple_pie", ingredients=ingredients_array,
    directions=directions_array, picture="/static/applepie.jpeg")

    apple_pie.put()


    ingredients2_array=["2 cups flour", "2 egg yolks beaten", "1 whole egg", "1 tablespoon sugar",
    "1/2 cup Water", "1/2 teaspoon salt",
     "3 large apples",  "1/2 cup brown sugar", "1 tablespoon ground cinnamon",
    "1/4 teaspoon ground nutmeg", "powder sugar to sprinkle"]

    directions2_array=["Crack the 2 eggs and add the water, salt to the eggs, mixing them thoroughly.",
    "pour them into a mixing bowl along with the flour, use hands to knead the dough.",
    "Set aside the dough for 10-12 minutes to set.",
    "Start rolling out the dough on the cutting board as thin as you can about 1/8 inch or less.",
    "Using a round plate or a giant cookie cutter, cut the dough into 4-inch circles.",
    "place about a 2 tablespoons of apple filing in one side of the dough.",
    "place about a 2 tablespoons of apple filing in one side of the dough.",
    "Fold it in half and curl up the edges of the empanada to seal it.",
    "Crack the extra egg and whisk it up with a splash of cold water until pale yellow and perfectly mixed.",
    "Just before the empanadas go in the oven, use a pastry brush and paint them with a light, even coat of egg wash Bake for 8-10 minutes at 350 degrees."
    "In a saucepan cook the apples with the sugar, cinnamon and nutmeg on medium heat. Cook for about 5-7 minutes until apples are soft and translucent.",
    "Let it cool off and sprinkle with powdered sugar"]

    apple_empanadas=models.Recipe(name_displayed="Apple Empanadas", food_name="apple_empanadas", ingredients=ingredients2_array, directions=directions2_array, picture="/static/appleempanadas.jpg")


    apple_empanadas.put()

    ingredients3_array=["1 cup sugar", "8 ounces butter at room temperature",
    "4 large eggs room temperature", "2 cups all-purpose flour",
    "1 teaspoon baking powder", "1/2 teaspoon salt", "1 teaspoon vanilla extract", "6 apples",  "1/2 cup sugar", "1 tablespoon cinnamon"]

    directions3_array=["Preheat oven to 350F. Line the bottom of a 9-inch springform pan with parchment paper.",
    "Spray the pan with baking spray and rub with a paper towel to evenly coat.",
    "In a small bowl, combine 1/2 cup sugar with 1 tablespoon cinnamon.",
    "Combine flour,baking powder and salt. Stir well.",
    "Peel and core apples, cut into quarters and then cut each quarter into thin slices.",
    "In the bowl of an electric mixer, beat butter and sugar until thick and smooth. Add vanilla then add eggs, one at the time, beating for 30 seconds after each addition.",
    "Stop to scrape down sides of bowl once or twice.",
    "With mixer on low speed, add flour mixture and mix just until combined.",
    "Combine the apples with the cinnamon/sugar mixture. Add half of the apples to the prepared pan.",
    "Pour batter over apples and smooth batter to edges of pan. Starting in the center, add remaining apples in a circular pattern on top of the batter.",
    "Sprinkle any remaining cinnamon/sugar mixture over the top of the apples.",
    "Bake cake for one hour. Cover loosely with foil and bake another 15-20 minutes or until set in the center. Check to see if a toothpick inserted in the center comes out clean.",
    "Cool on a baking rack before removing outer ring. Serve warm or at room temperature with a dollop of whipped cream or ice cream. Enjoy!"]

    danish_apple_pie=models.Recipe(name_displayed="Danish Apple Pie", food_name="danish_apple_pie", ingredients=ingredients3_array, directions=directions3_array, picture="/static/danishapplepie.jpg")

    danish_apple_pie.put()

    ingredients4_array=["1/2 cup mayonnaise", "2 tablespoons apple cider vinegar",
    "1 tablespoon sugar", "1 tablespoon grainy mustard", "1/2 teaspoon salt",
    "1/2 teaspoon celery seed", "1/2 teaspoon black pepper", "4 cups shredded cabbage",
    "2 tart apples (cored, julienned or shredded)", "1 cup carrots shredded"]

    directions4_array=["Combine dressing ingredients in a small bowl & set aside", "Toss with slaw ingredients", "Allow to sit for at least 1 hour before serving"]

    apple_slaw=models.Recipe(name_displayed="Apple Slaw", food_name="apple_slaw", ingredients=ingredients4_array, directions=directions4_array, picture="/static/appleslaw.jpg")

    apple_slaw.put()

    ingredients5_array=["1 cup sugar", "3 tablespoons butter", "3 large eggs", "1 cup self raising flour", "2 ml baking powder", "pinch of salt",
    "1/4 cup (60 ml) milk", "1 small tin (385 g) of tart apples (unsweetened)", "1 Tin Cream", "1 Cup Sugar"]

    directions5_array=["Preheat oven to 180C", "Beat the butter and sugar until light and fluffy.", "Add the eggs one at a time", "Sift the flour, baking powder and salt and add to the mixture.",
    "Mix slightly and add the milk little by little", "Add the batter in prepared baking dish and place the apples on top.",
    "Bake for 30-40 minutes until light brown.", "Heat the Tin Cream in a saucepan with the sugar until sugar is completely dissolved. Pour over warm apple tart."]

    apple_tart=models.Recipe(name_displayed="Apple Tart", food_name="apple_tart", ingredients=ingredients5_array, directions=directions5_array, picture="/static/appletart.jpg")

    apple_tart.put()

    ingredients6_array=["1 pound frozen raw shrimp", "3 tablespoons achiote oil orolive oil", "1 large onion, chopped", "4 cloves garlic, chopped", "1 tablespoon aji amarillo chili pepper paste",
    "1 teaspoon cumin", "1 package Sazon Goya with azafron (saffron)", "1 teaspoon salt",
    "2 tomatoes, chopped", "3 cups rice", "1/2 cup white wine", "2 cups frozen green peas (optional)", "Salt and pepper, to taste", "2 tablespoons minced cilantro", "Juice of 1 lime"]

    directions6_array=["Bring a pot of salted water to a boil. Add the shrimp and cook for 2 minutes, until they just turn pink.", "Remove the shrimp from the water with a slotted spoon and place shrimp in a bowl of ice water.", "Put the oil in a skillet over medium heat.",
    "Add the chopped onion and garlic and cook until translucent and fragrant.", "Add the aji amarillo paste, cumin, Sazon Goya, salt and tomatoes to the onions and garlic.", "Continue cooking for several minutes more, until the onions are soft and golden.",
    "Add the rice and white wine and cook until the liquid is dissolved, stirring frequently.", "Add 2 to 3 cups of the shrimp cooking water to the rice.", "Cover and simmer over low heat until the rice has absorbed the water and is fully cooked, about 15 minutes. Add more liquid if needed.",
    "Just before the rice is done, add frozen peas if desired.", "Taste the mixture and season with salt and pepper as desired.", "Remove from the heat and add the cooked shrimp.", "Garnish with minced cilantro and lime juice.]

    shrimp_paella=models.Recipe(name_displayed="Peruvian Shrimp Paella", food_name="shrimp_paella", ingredients=ingredients6_array, directions=directions6_array, picture="/static/shrimppaella.png")

    ingredients7_array=["24 jumbo raw shrimp (about 2 pounds), peeled, deveined, and tails removed", "6 to 7 strips of bacon", "1 cup of Louisiana Hot Sauce (not Tabasco sauce)""]

    direction7_array=["Preheat the oven to 400 degrees F.", "Peel and devein the shrimp, remove the tails (if desired)", "Line a baking sheet with parchment paper and arrange bacon on the sheet. Bake the bacon until half-cooked (about 6 minutes). Remove from oven and let the bacon cool and slice each piece in half and then half the bacon pieces again.",
    "Wrap each bacon slice tightly around the center of each shrimp and secure with a toothpick.", "Arrange the shrimp back on baking sheet and bake until the bacon is cooked through and crispy, approximately 6 minutes. The shrimp will have also turned pink.", "Once cooked, transfer the shrimp to a large bowl and gently toss with the Louisiana Hot Sauce until each piece is well coated."]

    buffalo_shrimp=models.Recipe(name_displayed="Bacon Wrapped Buffalo Shrimp", food_name="buffalo_shrimp", ingredients=ingredients7_array, directions=direction7_array, picture="/static/buffalo_shrimp.png")

def get_link_url (url):
    if url=="/recipes/firstrecipe":
            namefood="apple_pie"
    if url=="/recipes/secondrecipe":
            namefood="apple_empanadas"
    if url=="/recipes/thirdrecipe":
            namefood="danish_apple_pie"
    if url=="/recipes/fourthrecipe":
            namefood="apple_slaw"
    if url=="/recipes/fifthrecipe":
            namefood="apple_tart"
    else:

    return namefood
