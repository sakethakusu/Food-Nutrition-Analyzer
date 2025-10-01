
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FoodNutritionAnalyzer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Food Nutrition Analyzer and Meal Planner")

        # Define the dataset path
        dataset_path = "C:/Users/DELL/Downloads/archive/food.csv"

        self.nutritional_df = pd.read_csv(dataset_path)
        self.food_items = self.nutritional_df["Description"].tolist()
        self.selected_items = []

        self.create_widgets()

    def create_widgets(self):
        self.food_label = ttk.Label(self, text="Select Food Item:")
        self.food_label.grid(row=0, column=0, padx=5, pady=5)

        self.food_combobox = ttk.Combobox(self, values=self.food_items, width=50)
        self.food_combobox.grid(row=0, column=1, padx=5, pady=5)

        self.add_button = ttk.Button(self, text="Add Food", command=self.add_food)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        self.selected_food_label = ttk.Label(self, text="Selected Food Items:")
        self.selected_food_label.grid(row=1, column=0, padx=5, pady=5)

        self.selected_food_listbox = tk.Listbox(self, width=60, height=10)
        self.selected_food_listbox.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.calculate_button = ttk.Button(self, text="Calculate Nutrition", command=self.calculate_nutrition)
        self.calculate_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    def add_food(self):
        food_item = self.food_combobox.get()
        if food_item:
            self.selected_food_listbox.insert(tk.END, food_item)
            self.selected_items.append(food_item)

    def calculate_nutrition(self):
        if not self.selected_items:
            messagebox.showwarning("No Food Items", "Please select at least one food item.")
            return

        selected_data = self.nutritional_df[self.nutritional_df['Description'].isin(self.selected_items)]
        total_nutrition = selected_data.sum()

        messagebox.showinfo("Total Nutrition", 
                            f"Total Kilocalories: {total_nutrition['Nutrient Data Bank Number']} kcal\n"
                            f"Total Protein: {total_nutrition['Data.Protein']} g\n"
                            f"Total Carbohydrates: {total_nutrition['Data.Carbohydrate']} g\n"
                            f"Total Fat: {total_nutrition['Data.Fat.Total Lipid']} g")


if __name__ == "__main__":
    app = FoodNutritionAnalyzer()
    app.mainloop()
