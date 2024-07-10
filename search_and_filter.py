def search_by_name(recipes, name):
    return [recipe for recipe in recipes if name.lower() in recipe['title'].lower()]


def filter_by_time(recipes, time):
    return [recipe for recipe in recipes if 'time' in recipe and recipe['time'] <= time]


def filter_by_category(recipes, category):
    return [recipe for recipe in recipes if 'category' in recipe and category.lower() in recipe['category'].lower()]


def filter_by_ingredients(recipes, available_ingredients):
    available_ingredients_set = set(
        ingredient.strip().lower() for ingredient in available_ingredients)
    return [
        recipe for recipe in recipes
        if available_ingredients_set.issubset(set(ingredient.strip().lower() for ingredient in recipe.get('ingredients', [])))
    ]
