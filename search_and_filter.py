def search_by_name(recipes, name):
    return [recipe for recipe in recipes if name.lower() in recipe['title'].lower()]

def filter_by_time(recipes, time):
    return [recipe for recipe in recipes if recipe['time'] <= time]

def filter_by_category(recipes, category):
    return [recipe for recipe in recipes if category.lower() in recipe['category'].lower()]