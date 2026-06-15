import json
import requests
from pydantic import BaseModel, ValidationError
from requests.exceptions import HTTPError, ConnectTimeout

# Configuration
API_URL = "https://crudcrud.com/api/69d99b013d154da9b983f73cd313f740"


# Part 1: Pydantic Model
class Recipe(BaseModel):
    name: str
    cuisine: str
    time_minutes: str


def api_request(method, url, **kwargs):

    try:
        response = requests.request(method, url, timeout=10, **kwargs)
        response.raise_for_status()
        return response
    except HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
    except ConnectTimeout:
        print("ConnectTimeout: The server took too long to respond.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    return None


def main():
    # Part 2: POST - Add Recipes
    print("--- Part 2: Uploading from recipes.json ---")
    try:
        with open("recipes.json", "r") as f:
            data = json.load(f)

        for item in data:
            validated_recipe = Recipe(**item)
            api_request("POST", API_URL, json=validated_recipe.model_dump())
            print(f"Added: {validated_recipe.name}")
    except (ValidationError, FileNotFoundError) as e:
        print(f"Error: {e}")

    # Part 3: GET - Fetch All
    print("\n--- Part 3: Fetching All Recipes ---")
    all_recipes = []
    response = api_request("GET", API_URL)
    if response:
        all_recipes = response.json()
        try:
            for r in all_recipes:
                v = Recipe(**r)
                print(f"Recipe: {v.name} | Time: {v.time_minutes} min")
        except ValidationError as e:
            print(f"Data Validation Error: {e}")

    # Part 4: GET - Fetch by ID
    if all_recipes:
        print(f"\n--- Part 4: Fetching ID: {all_recipes[0]['_id']} ---")
        target_id = all_recipes[0]['_id']
        response = api_request("GET", f"{API_URL}/{target_id}")
        if response:
            print(f"Full Data: {response.json()}")

    # Part 5: PUT - Update
    if len(all_recipes) > 0:
        print("\n--- Part 5: Updating First Recipe ---")
        target_id = all_recipes[0]['_id']
        updated_info = {
            "name": "Updated Khachapuri",
            "cuisine": "Georgian-Modern",
            "time_minutes": "40"
        }

        try:
            valid_update = Recipe(**updated_info)
            res = api_request("PUT", f"{API_URL}/{target_id}", json=valid_update.model_dump())
            if res:
                print("Update successful. Saving to local file...")
                with open("updated_recipes.json", "w") as f:
                    json.dump(updated_info, f)
        except ValidationError as e:
            print(f"Validation Error on Update: {e}")

    #Part 6: DELETE - Last Recipe
    response = api_request("GET", API_URL)
    if response:
        current_list = response.json()
        if current_list:
            last_id = current_list[-1]['_id']
            print(f"\n--- Part 6: Deleting Last Recipe (ID: {last_id}) ---")

            del_res = api_request("DELETE", f"{API_URL}/{last_id}")
            if del_res:
                print("Deleted successfully. Verifying...")

                final_res = api_request("GET", API_URL)
                if final_res:
                    print(f"Remaining Recipes: {len(final_res.json())}")
                    for r in final_res.json():
                        print(f"- {r['name']}")


if __name__ == "__main__":
    main()