import tkinter as tk
from tkinter import messagebox

class CalorieCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Counter")
        
        self.age = tk.IntVar()
        self.weight = tk.DoubleVar()
        self.height = tk.DoubleVar()
        self.medical_condition = tk.StringVar()
        
        self.calorie_requirement = tk.StringVar()
        self.calorie_requirement.set("0")
        
        self.food_items = []
        self.calories_consumed = []
        
        self.medical_conditions = {
            "Inactive": 0,
            "Diabetes": -250,
            "Hypertension": -200,
            "Heart Disease": -300,
            "Obesity": -500,
            "Pregnancy": -100
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        # Label and entry field for age
        age_label = tk.Label(self.root, text="Age:")
        age_label.pack()
        
        age_entry = tk.Entry(self.root, textvariable=self.age)
        age_entry.pack()
        
        # Label and entry field for weight
        weight_label = tk.Label(self.root, text="Weight (in kg):")
        weight_label.pack()
        
        weight_entry = tk.Entry(self.root, textvariable=self.weight)
        weight_entry.pack()
        
        # Label and entry field for height
        height_label = tk.Label(self.root, text="Height (in cm):")
        height_label.pack()
        
        height_entry = tk.Entry(self.root, textvariable=self.height)
        height_entry.pack()
        
        # Label and drop-down menu for medical condition
        medical_condition_label = tk.Label(self.root, text="Medical Condition:")
        medical_condition_label.pack()
        
        medical_condition_menu = tk.OptionMenu(self.root, self.medical_condition, *self.medical_conditions.keys())
        medical_condition_menu.pack()
        
        # Button to calculate calorie requirement
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_calorie_requirement)
        calculate_button.pack()
        
        # Label for displaying the calorie requirement
        calorie_requirement_label = tk.Label(self.root, text="Calorie Requirement:")
        calorie_requirement_label.pack()
        
        calorie_requirement_display = tk.Label(self.root, textvariable=self.calorie_requirement)
        calorie_requirement_display.pack()
        
        # Button to submit the information
        submit_button = tk.Button(self.root, text="Submit", command=self.open_food_window)
        submit_button.pack()
    
    def calculate_calorie_requirement(self):
        age = self.age.get()
        weight = self.weight.get()
        height = self.height.get()
        
        if age <= 0 or weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Please enter valid information.")
            return
        
        medical_condition = self.medical_condition.get()
        calorie_adjustment = self.medical_conditions.get(medical_condition, 0)
        
        # Calculate the calorie requirement based on age and medical condition
        calorie_requirement = 10 * weight + 6.25 * height - 5 * age + calorie_adjustment
        
        self.calorie_requirement.set(str(calorie_requirement))
    
    def open_food_window(self):
        food_window = tk.Toplevel(self.root)
        food_window.title("Food Consumption")
        
        # Label and entry fields for food items and calories
        item_label = tk.Label(food_window, text="Food Item:")
        item_label.grid(row=0, column=0)
        
        calories_label = tk.Label(food_window, text="Calories:")
        calories_label.grid(row=0, column=1)
        
        item_entry = tk.Entry(food_window)
        item_entry.grid(row=1, column=0)
        
        calories_entry = tk.Entry(food_window)
        calories_entry.grid(row=1, column=1)
        
        # Button to add food item and calories
        add_button = tk.Button(food_window, text="Add", command=lambda: self.add_food(item_entry, calories_entry))
        add_button.grid(row=2, column=0, columnspan=2)
        
        # Label for displaying the entered food items and calories
        items_label = tk.Label(food_window, text="Food Items:")
        items_label.grid(row=3, column=0, sticky="w")
        
        calories_display_label = tk.Label(food_window, text="Calories:")
        calories_display_label.grid(row=3, column=1, sticky="w")
        
        # Button to check if consumed calories exceed the requirement
        check_button = tk.Button(food_window, text="Check Calories", command=self.check_calories)
        check_button.grid(row=4, column=0, columnspan=2)
        
        self.item_display_label = tk.Label(food_window, text="")
        self.item_display_label.grid(row=5, column=0, sticky="w")
        
        self.calories_display_label = tk.Label(food_window, text="")
        self.calories_display_label.grid(row=5, column=1, sticky="w")
    
    def add_food(self, item_entry, calories_entry):
        item = item_entry.get()
        calories = calories_entry.get()
        
        if item and calories:
            self.food_items.append(item)
            self.calories_consumed.append(int(calories))
            
            self.item_display_label["text"] = ", ".join(self.food_items)
            self.calories_display_label["text"] = ", ".join(map(str, self.calories_consumed))
            
            # Clear the entry fields
            item_entry.delete(0, tk.END)
            calories_entry.delete(0, tk.END)
    
    def check_calories(self):
        calorie_requirement = float(self.calorie_requirement.get())
        consumed_calories = sum(self.calories_consumed)
        
        if consumed_calories > calorie_requirement:
            messagebox.showwarning("Alert", "You have consumed more calories than required.")
        else:
            messagebox.showinfo("Information", "You have consumed a healthy number of calories.")

# Create the GUI window
root = tk.Tk()

# Create an instance of the CalorieCounter class
counter = CalorieCounter(root)

# Run the GUI event loop
root.mainloop()
