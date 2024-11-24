import tkinter as tk
from tkinter import messagebox

def open_dialog_with_slider_and_checkbox(options):
    # Create a new window (dialog)
    dialog = tk.Toplevel()
    dialog.title("Select an Option and Value")

    # Add a label for the slider
    label_slider = tk.Label(dialog, text="Select a value between 150 and 300:")
    label_slider.pack(pady=10)

    # Add a slider (scale widget)
    slider = tk.Scale(dialog, from_=150, to=300, orient="horizontal")
    slider.pack(pady=10)

    # Variable to store selected checkbox value
    selected_values = {}

    # Create checkboxes for each option in the list
    for option, value in options.items():
        selected_values[option] = tk.IntVar()
        checkbox = tk.Checkbutton(dialog, text=option, variable=selected_values[option], onvalue=value, offvalue=0)
        checkbox.pack(anchor="w", padx=20, pady=5)

    # Function to handle the submit action
    def on_submit():
        selected_option = None
        for option, value in selected_values.items():
            if value.get() == 1:
                selected_option = option
                break
        slider_value = slider.get()
        
        if selected_option:
            print(f"Selected option: {selected_option} (Value: 1)")
        else:
            print("No option selected (Value: 0)")

        print(f"Slider value selected: {slider_value}")

        # Display 'Wait' message on the dialog box
        wait_label.config(text="Wait...")

        # Close the dialog after 5 seconds (5000 ms)
        dialog.after(5000, dialog.destroy)

    # Add a label to show the "Wait..." message after submit
    wait_label = tk.Label(dialog, text="")
    wait_label.pack(pady=10)

    # Submit button to confirm the selection
    submit_button = tk.Button(dialog, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    # Wait for the user to close the dialog
    dialog.wait_window()

# Main application window (optional, can stay hidden)
root = tk.Tk()
root.withdraw()  # Hide the main window

# Array of strings with their corresponding internal values (1 or 0)
options = {
    "Option 1": 1,
    "Option 2": 0,
    "Option 3": 1
}

# Open dialog with both slider and checkboxes
open_dialog_with_slider_and_checkbox(options)
