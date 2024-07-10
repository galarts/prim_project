import json

class RecipeManager:
    def __init__(self, filename='recipes.json'):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.recipes = json.load(file)
        except FileNotFoundError:
            self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        with open(self.filename, 'w') as file:
            json.dump(self.recipes, file, indent=4)

    def get_recipes(self):
        return self.recipes