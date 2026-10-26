import json
import os
from datetime import datetime

FILE_NAME = "history.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_entry():
    data = load_data()

    food = input("Enter food name: ")
    cal_per_gram = float(input("Enter calories per gram: "))
    food_grams = float(input("Enter food grams consumed: "))

    total_calories = cal_per_gram * food_grams

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "food": food,
        "calories": total_calories,
        "grams": food_grams,
        "cal_per_gram": cal_per_gram
    }

    data.append(entry)
    save_data(data)

    print("\n----- RESULT -----")
    print(f"Food Name: {food}")
    print(f"Calories per gram: {cal_per_gram}")
    print(f"Food grams: {food_grams} g")
    print(f"Total Calories: {total_calories} kcal")
    print("Saved successfully!")


def view_history():
    data = load_data()

    if not data:
        print("No history found.")
        return

    print("\n------ HISTORY ------")
    for item in data:
        print(
            f"{item['date']} | "
            f"{item['food']} | "
            f"{item['grams']} g | "
            f"{item['calories']} kcal"
        )


while True:
    print("\n===== CALORIE TRACKER =====")
    print("1. Add Food")
    print("2. View History")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_history()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
