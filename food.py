
import streamlit as st
from PIL import Image
from search_and_filter import search_by_name, filter_by_time, filter_by_category, filter_by_ingredients
from recipe_manager import RecipeManager

def main():
    st.title(":green[_Rețete Culinare_]")
    page_img = Image.open('food_ingredients.jpg')
    st.image(page_img)
   

    recipe_manager = RecipeManager()
    recipes = recipe_manager.get_recipes()
    with st.sidebar: 
        st.header("Adaugă o rețetă nouă")
        
        title = st.text_input("Titlul Rețetei")
        ingredients = st.text_area("Ingredientele", height=100)
        steps = st.text_area(":green[Pașii de preparare]", height=100)
        time = st.number_input(
            "Timp de preparare (minute)", min_value=0, step=5)
        category = st.selectbox("Categorie", options=[
                                "Desert", "Fel principal", "Aperitiv", "Salată"])
        
        uploaded_file = st.file_uploader("Încarcă o imagine pentru rețetă (Limită de 10MB • JPG, JPEG, PNG)", type=['jpg', 'jpeg', 'png'])
        
        if st.button("Adaugă Rețeta"):
            try:
                ingredients_list = [
                    ing.strip() for ing in ingredients.split('\n') if ing.strip()]
               
                if uploaded_file is not None:
                    image = Image.open(uploaded_file)
                    recipe_manager.add_recipe({
                        "title": title,
                        "ingredients": ingredients_list,
                        "steps": steps,
                        "time": time,
                        "category": category,
                        "image_path": uploaded_file.name,
                    }, image)
                else:
                    recipe_manager.add_recipe({
                    "title": title,
                    "ingredients": ingredients_list,
                    "steps": steps,
                    "time": time,
                    "category": category
                }, None)



                st.success("Rețetă adăugată cu succes!")
                recipes = recipe_manager.get_recipes()
            except ValueError as e:
                st.error(str(e))

    st.header("Căutare și filtrare rețete")
    search_term = st.text_input("Caută rețetă după nume")
    filter_time = st.slider(
        "Filtrează după timpul de preparare (minute)", 0, 240, 120)
    filter_category = st.selectbox("Filtrează după categorie", [
                                   "Toate", "Desert", "Fel principal", "Aperitiv", "Salată"])
    available_ingredients = st.text_input(
        "Rețetă după ingrediente disponibile (separați prin virgulă)")
    # recipes = recipe_manager.get_recipes()
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
        
        
        if 'image_path' in recipe:
            recipe_image = Image.open(recipe['image_path'])
            st.image(recipe_image, caption='Imagine rețetă', use_column_width=True)

if __name__ == "__main__":
    recipe_manager = RecipeManager()
    main()
