

# import streamlit as st
from search_and_filter import search_by_name, filter_by_time, filter_by_category, filter_by_ingredients
from recipe_manager import RecipeManager
import streamlit as st
from PIL import Image


# st.title("FOOD  :green[& _Recepies_ ]")




def main():
    st.title(":green[_Rețete Culinare_]")
    page_img = Image.open('food_ingredients.jpg')
    st.image(page_img)
    

    with st.sidebar:
        st.header("Adaugă o rețetă nouă")
        title = st.text_input("Titlul Rețetei")
        ingredients = st.text_area("Ingredientele", height=100)
        steps = st.text_area(":green[Pașii de preparare]", height=100)
        time = st.number_input(
            "Timp de preparare (minute)", min_value=1, step=1)
        category = st.selectbox("Categorie", options=[
                                "Desert", "Fel principal", "Aperitiv", "Salată"])
        if st.button("Adaugă Rețeta"):
            try:
                ingredients_list = [
                    ing.strip() for ing in ingredients.split('\n') if ing.strip()]
                recipe_manager.add_recipe({
                    "title": title,
                    "ingredients": [ing.strip() for ing in ingredients.split(',')],
                    "steps": steps,
                    "time": time,
                    "category": category
                })
                st.success("Rețetă adăugată cu succes!")
            except ValueError as e:
                st.error(str(e))

    st.header("Căutare și filtrare rețete")
    search_term = st.text_input("Caută rețetă după nume")
    filter_time = st.slider(
        "Filtrează după timpul de preparare (minute)", 0, 240, 120)
    filter_category = st.selectbox("Filtrează după categorie", [
                                   "Toate", "Desert", "Fel principal", "Aperitiv", "Salată"])
    available_ingredients = st.text_input(
        "Ingrediente disponibile (separate prin virgulă)")
    recipes = recipe_manager.get_recipes()
    if search_term:
        recipes = search_by_name(recipes, search_term)
    if filter_time < 240:
        recipes = filter_by_time(recipes, filter_time)
    if filter_category != "Toate":
        recipes = filter_by_category(recipes, filter_category)
    if available_ingredients:

        ingredients_list = [
            ing.strip() for ing in available_ingredients.split(',') if ing.strip()]

        recipes = filter_by_ingredients(recipes, ingredients_list)
    for recipe in recipes:
        st.subheader(recipe['title'])
        st.write("Ingredientele:", ", ".join(recipe['ingredients']))
        st.write("Pașii de preparare:", recipe['steps'])
        st.write("Timp de preparare:", str(recipe['time']) + " minute")
        st.write("Categorie:", recipe['category'])


if __name__ == "__main__":
    recipe_manager = RecipeManager()
    main()
