def search_by_name(recipes, name):
    return [recipe for recipe in recipes if name.lower() in recipe['title'].lower()]


def filter_by_time(recipes, time):
    return [recipe for recipe in recipes if 'time' in recipe and recipe['time'] <= time]


def filter_by_category(recipes, category):
    return [recipe for recipe in recipes if 'category' in recipe and category.lower() in recipe['category'].lower()]


def filter_by_ingredients(recipes, keywords):
    filtered_recipes = []
    for recipe in recipes:
        ingredients = recipe.get('ingredients', [])
        if all(any(keyword.strip().lower() in ingredient.strip().lower() for ingredient in ingredients) for keyword in keywords):
            filtered_recipes.append(recipe)
    return filtered_recipes