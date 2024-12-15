import requests

api_key = "83b2b1202ace49ebb26496ac998fedb4"  ##günlük kota 150
base_url = "https://api.spoonacular.com/recipes/"


def find_recipe(ingredients):
    # API'ye tarif bulma isteği gönder
    search_url = f"{base_url}findByIngredients"  #
    params = {
        "ingredients": ingredients,
        "number": 5,  # Gösterilecek tarif sayısı
        "apiKey": api_key
    }
    response = requests.get(search_url, params=params)
    recipes = response.json()
    return recipes


