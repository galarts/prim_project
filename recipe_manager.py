import json
import os

class RecipeManager:
    def __init__(self, filename='recipes.json',image_folder='recipe_images'):
        self.filename = filename
        self.image_folder = image_folder
        
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)
        try:
            with open(self.filename, 'r') as file:
                self.recipes = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.recipes = []

    def add_recipe(self, recipe,image):
        required_fields = ["title", "ingredients", "steps", "time", "category"]
        if all(field in recipe for field in required_fields):
            image_filename = os.path.join(self.image_folder, recipe['title'].replace(' ', '_') + '.jpg')
            image.save(image_filename)
            recipe['image_path'] = image_filename
            self.recipes.append(recipe)
            with open(self.filename, 'w') as file:
                json.dump(self.recipes, file, indent=4)
        else:
            raise ValueError
                
    def get_recipes(self):
        return self.recipes
