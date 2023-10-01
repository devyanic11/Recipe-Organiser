import json

# Initialize an empty recipe database
recipes = []

# Function to add a new recipe
def add_recipe():
    name = input("Enter the name of the recipe: ")
    ingredients = input("Enter the list of ingredients (comma-separated): ").split(",")
    instructions = input("Enter the cooking instructions: ")
    
    recipe = {
        "name": name,
        "ingredients": ingredients,
        "instructions": instructions
    }
    
    recipes.append(recipe)
    print(f"Recipe '{name}' added successfully!")

# Function to view all recipes
def view_all_recipes():
    if not recipes:
        print("No recipes found.")
    else:
        for index, recipe in enumerate(recipes):
            print(f"{index + 1}. {recipe['name']}")

# Function to search for a recipe by name
def search_recipe_by_name():
    search_term = input("Enter the name of the recipe to search: ")
    
    found_recipes = [recipe for recipe in recipes if search_term.lower() in recipe['name'].lower()]
    
    if not found_recipes:
        print(f"No recipes found matching '{search_term}'.")
    else:
        print("Found recipes:")
        for index, recipe in enumerate(found_recipes):
            print(f"{index + 1}. {recipe['name']}")

# Function to view the details of a specific recipe
def view_recipe_details():
    recipe_index = int(input("Enter the number of the recipe to view details: ")) - 1
    
    if 0 <= recipe_index < len(recipes):
        recipe = recipes[recipe_index]
        print(f"Recipe Name: {recipe['name']}")
        print("Ingredients:")
        for ingredient in recipe['ingredients']:
            print(f"- {ingredient.strip()}")
        print("Instructions:")
        print(recipe['instructions'])
    else:
        print("Invalid recipe number!")

# Main menu loop
while True:
    print("\nRecipe Management System")
    print("1. Add Recipe")
    print("2. View All Recipes")
    print("3. Search Recipe by Name")
    print("4. View Recipe Details")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_recipe()
    elif choice == "2":
        view_all_recipes()
    elif choice == "3":
        search_recipe_by_name()
    elif choice == "4":
        view_recipe_details()
    elif choice == "5":
        # Save recipes to a JSON file before exiting
        with open("recipes.json", "w") as file:
            json.dump(recipes, file)
        print("Recipes saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
