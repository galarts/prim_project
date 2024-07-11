import json


class RecipeManager:
    def __init__(self, filename='recipes.json'):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.recipes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.recipes = []

    def add_recipe(self, recipe):
        required_fields = ["title", "ingredients", "steps", "time", "category"]
        if all(field in recipe for field in required_fields):
            self.recipes.append(recipe)
            with open(self.filename, 'w') as file:
                json.dump(self.recipes, file, indent=4)
        else:
            raise ValueError
                
    def get_recipes(self):
        return self.recipes
