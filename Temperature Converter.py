import customtkinter as ctk
from datetime import datetime

# Define the function to update the real-time clock
def update_time():
    # Get the current time and format it
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Update the real-time label with the current time
    real_time_label.configure(text=f"Current Time: {current_time}")
    
    # Schedule the next update
    window.after(1000, update_time)  # Update every second

# Define the function to convert temperatures
def convert_temperature():
    try:
        # Get the input temperature and selected conversion type
        temp_value = float(entry_temp.get())
        conversion_type = combo_conversion.get()

        # Perform conversion based on the selected type
        if conversion_type == "Celsius to Fahrenheit":
            result = (temp_value * 9 / 5) + 32
            result_label.configure(text=f"{result:.2f} °F")
        
        elif conversion_type == "Celsius to Kelvin":
            result = temp_value + 273.15
            result_label.configure(text=f"{result:.2f} K")
        
        elif conversion_type == "Fahrenheit to Celsius":
            result = (temp_value - 32) * 5 / 9
            result_label.configure(text=f"{result:.2f} °C")
        
        elif conversion_type == "Fahrenheit to Kelvin":
            result = (temp_value - 32) * 5 / 9 + 273.15
            result_label.configure(text=f"{result:.2f} K")
        
        elif conversion_type == "Kelvin to Celsius":
            result = temp_value - 273.15
            result_label.configure(text=f"{result:.2f} °C")
        
        elif conversion_type == "Kelvin to Fahrenheit":
            result = (temp_value - 273.15) * 9 / 5 + 32
            result_label.configure(text=f"{result:.2f} °F")

        # Clear any error messages
        error_label.configure(text="")

    except ValueError:
        error_label.configure(text="Please enter a valid number.")

# Create the CustomTkinter window
ctk.set_appearance_mode("light")  # Set to light mode for a lighter appearance

window = ctk.CTk()  # Create the window
window.title("Temperature Converter")
window.geometry("400x200")  # Smaller size, no calendar

# Create the combo box for conversion types
conversion_types = [
    "Celsius to Fahrenheit",
    "Celsius to Kelvin",
    "Fahrenheit to Celsius",
    "Fahrenheit to Kelvin",
    "Kelvin to Celsius",
    "Kelvin to Fahrenheit",
]
combo_conversion = ctk.CTkComboBox(window, values=conversion_types)
combo_conversion.grid(row=0, column=1, padx=10, pady=10)
combo_conversion.set("Celsius to Fahrenheit")  # Default option

# Create the input field for temperature
label_temp = ctk.CTkLabel(window, text="Enter Temperature:")
label_temp.grid(row=0, column=0, padx=10, pady=10)

entry_temp = ctk.CTkEntry(window)  # Input field for temperature
entry_temp.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create the Convert button
convert_button = ctk.CTkButton(window, text="Convert", command=convert_temperature)
convert_button.grid(row=1, column=2, padx=10, pady=10)

# Create the result label
result_label = ctk.CTkLabel(window, text="Result")
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Create a label for the real-time clock
real_time_label = ctk.CTkLabel(window, text="Current Time:")
real_time_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Create an error label for error messages
error_label = ctk.CTkLabel(window, text="", text_color="red")  # For error messages
error_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI application and real-time clock
window.after(1000, update_time)  # Start updating the clock every second
window.mainloop()
