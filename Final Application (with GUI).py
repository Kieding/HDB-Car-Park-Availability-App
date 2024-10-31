#Additional Feature #1 - GUI implementation using Python Tkinter
#Kieron Lim - CICTP02 (13/8/23)

import tkinter as tk
from tkinter import messagebox
import os

#Read carpark-information.csv and create data_list
with open('C:\\carpark-information.csv', 'r') as file: #Open and read the CSV file
    lines = file.readlines()

data_list = []

#Extracting column headers
headers = lines[0].strip().split(',')

#Loop through the remaining lines and create dictionaries
for line in lines[1:]:
    values = line.strip().split(',')
    carpark_dict = {}
    for x, header in enumerate(headers):
        carpark_dict[header] = values[x]
    data_list.append(carpark_dict)

#Create functions for the menu options
def display_total_carparks(): #Option 1
    total_carparks = len(data_list)
    update_result_text("Total Number of carparks: {}".format(total_carparks))

def display_basement_carparks(): #option 2
    basement_carparks = [carpark for carpark in data_list if carpark['Carpark Type'] == 'BASEMENT CAR PARK']
    result = "\n".join(carpark['Carpark Number'] + " - " + carpark['Address'] for carpark in basement_carparks)
    update_result_text("Basement Carparks:\n\n{}".format(result))

def read_carpark_availability_file(): #Option 3
    global total_carpark_list
    file_name = input_file_entry.get()

    if os.path.isfile('C:\\' + file_name):
        with open('C:\\' + file_name, 'r') as file:
            lines = file.readlines()
            total_carpark_list = [line.strip().split(',') for line in lines]
            update_result_text("File read successfully: {}\n{}".format(file_name, total_carpark_list[0][0]))
    else:
        update_result_text("File not found: {}".format(file_name))

def print_total_carparks(): #Optiion 4
    if total_carpark_list:
        total_carparks = len(total_carpark_list) - 2
        update_result_text("Total Number of Carparks in the file: {}".format(total_carparks))
    else:
        update_result_text("Please read a Carpark availability file first")

def display_carparks_without_available_lots(): #Option 5
    if not total_carpark_list:
        update_result_text("Please read a carpark availability file first")
        return

    carparks_without_available_lots = []
    for carpark_data in total_carpark_list[2:]:
        if carpark_data[2] == '0':
            carparks_without_available_lots.append(carpark_data[0])

    if carparks_without_available_lots:
        update_result_text("Carparks without available lots:\n{}".format(", ".join(carparks_without_available_lots)))
    else:
        update_result_text("No carparks without available lots found.")

def display_carparks_with_min_available_percentage(): #Option 6
    if not total_carpark_list:
        result_text.config(state=tk.NORMAL)  #enable edits
        result_text.delete("1.0", tk.END)     #clear the text
        result_text.insert(tk.END, "Please read a carpark availability file first")
        result_text.config(state=tk.DISABLED) #disable editing
        return

    try:
        min_available_percentage = float(min_available_percentage_entry.get())
        if min_available_percentage < 0 or min_available_percentage > 100:
            update_result_text("Invalid percentage. Please enter a number between 0 and 100.")
            return
    except ValueError:
        update_result_text("Invalid input. Please enter a valid numeric percentage.")
        return

    result_text.config(state=tk.NORMAL)  #enable editing
    result_text.delete("1.0", tk.END)     #Clear existing text

    result_text.insert(tk.END, "{}\t\t{}\t\t{}\t\t{}\n".format('Carpark No.', 'Total Lots', 'Lots Available', 'Percentage'))
    count = 0
    for carpark_data in total_carpark_list[2:]:
        carpark_no = carpark_data[0]
        total_lots = int(carpark_data[1])
        available_lots = int(carpark_data[2])
        available_percentage = (available_lots / total_lots) * 100 if total_lots != 0 else 0
        if available_percentage >= min_available_percentage:
            result_text.insert(tk.END, "{}\t\t{}\t\t{}\t\t{:.1f}\n".format(carpark_no, total_lots, available_lots, available_percentage))
            count += 1
    if count == 0:
        result_text.insert(tk.END, "No carparks meet the specified criteria.\n")
    else:
        result_text.insert(tk.END, 'Total Number: {}\n'.format(count))
    result_text.config(state=tk.DISABLED)

def display_carparks_with_min_available_percentage_with_address(): #Option 7
    if not total_carpark_list:
        result_text.config(state=tk.NORMAL)  #Enable editing
        result_text.delete("1.0", tk.END)     #Clear existing text
        result_text.insert(tk.END, "Please read a carpark availability file first")
        result_text.config(state=tk.DISABLED) #Disable editing after insertion
        return

    try:
        min_available_percentage = float(min_available_percentage_entry.get())
        if min_available_percentage < 0 or min_available_percentage > 100:
            update_result_text("Invalid percentage. Please enter a number between 0 and 100.")
            return
    except ValueError:
        update_result_text("Invalid input. Please enter a valid numeric percentage.")
        return

    result_text.config(state=tk.NORMAL)  #Enable editing
    result_text.delete("1.0", tk.END)     #Clear existing text

    result_text.insert(tk.END, "{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format('Carpark No.', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))
    count = 0
    for carpark_data in total_carpark_list[2:]:
        carpark_no = carpark_data[0]
        total_lots = int(carpark_data[1])
        available_lots = int(carpark_data[2])
        available_percentage = (available_lots / total_lots) * 100 if total_lots != 0 else 0
        address = next((item['Address'] for item in data_list if item['Carpark Number'] == carpark_no), 'Address not found')
        if available_percentage >= min_available_percentage:
            result_text.insert(tk.END, "{}\t\t{}\t\t{}\t\t{:.1f}\t\t{}\n".format(carpark_no, total_lots, available_lots, available_percentage, address))
            count += 1
    if count == 0:
        result_text.insert(tk.END, "No carparks meet the specified criteria.\n")
    else:
        result_text.insert(tk.END, 'Total Number: {}\n'.format(count))
    result_text.config(state=tk.DISABLED)


def display_carparks_at_location():  #Option 8
    location = input_location_entry.get().lower()  #Convert input to lowercase
    result_text.config(state=tk.NORMAL)  #Enable editing
    result_text.delete("1.0", tk.END)  #Clear existing text

    count = 0
    for carpark_data in total_carpark_list[2:]:
        carpark_no = carpark_data[0]
        total_lots = int(carpark_data[1])
        available_lots = int(carpark_data[2])
        available_percentage = (available_lots / total_lots) * 100 if total_lots != 0 else 0
        address = next((item['Address'] for item in data_list if item['Carpark Number'] == carpark_no),
                       'Address not found')
        if location in address.lower():
            if count == 0:
                result_text.insert(tk.END, "{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format('Carpark No.', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))
            result_text.insert(tk.END, "{:<}\t\t{:>}\t\t{:>}\t\t{:>.1f}\t\t{}\n".format(carpark_no, total_lots, available_lots, available_percentage, address))
            count += 1
    if count == 0:
        result_text.insert(tk.END, "Error: No carparks found at the specified location.\n")
    else:
        result_text.insert(tk.END, 'Total Number: {}\n'.format(count))

    result_text.config(state=tk.DISABLED)  #Disable editing after insertion


def display_carpark_with_most_available_lots():  #Option 9
    if not total_carpark_list:
        result_text.config(state=tk.NORMAL)  #Enable editing
        result_text.delete("1.0", tk.END)  #Clear existing text
        result_text.insert(tk.END, "Please read a carpark availability file first")
        result_text.config(state=tk.DISABLED)  #Disable editing after insertion
        return

    most_lots = 0
    most_lots_carpark = ''
    for carpark_data in total_carpark_list[2:]:
        available_lots = int(carpark_data[2])
        if available_lots > most_lots:
            most_lots = available_lots
            most_lots_carpark = carpark_data[0]

    result_text.config(state=tk.NORMAL)  #Enable editing
    result_text.delete("1.0", tk.END)  #Clear existing text

    if most_lots_carpark:
        header = "{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format('Carpark No.', 'Total Lots', 'Lots Available', 'Percentage','Address')
        result_text.insert(tk.END, header)  #Insert header

        carpark_data = next(item for item in total_carpark_list[2:] if item[0] == most_lots_carpark)
        total_lots = int(carpark_data[1])
        available_lots = int(carpark_data[2])
        available_percentage = (available_lots / total_lots) * 100 if total_lots != 0 else 0
        address = next((item['Address'] for item in data_list if item['Carpark Number'] == most_lots_carpark), 'Address not found')

        carpark_info = "{:<}\t\t{:>}\t\t{:>}\t\t{:>.1f}\t\t{}\n".format(most_lots_carpark, total_lots, available_lots, available_percentage, address)
        result_text.insert(tk.END, carpark_info)
    else:
        result_text.insert(tk.END, "No carparks found with available lots.\n")

    result_text.config(state=tk.DISABLED)


def save_sorted_carparks_with_addresses():  #Option 10
    if not total_carpark_list:
        result_text.config(state=tk.NORMAL)  #Enable editing
        result_text.delete("1.0", tk.END)  #Clear existing text
        result_text.insert(tk.END, "Please read a carpark availability file first")
        result_text.config(state=tk.DISABLED)  #Disable editing after insertion
        return

    output_file_name = 'carpark-availability-with-addresses.csv'
    try:
        with open(output_file_name, 'w') as output_file:
            output_file.write("Carpark No.,Total Lots,Lots Available,Percentage,Address\n")
            sorted_carparks = sorted(total_carpark_list[2:], key=lambda x: int(x[2]))  #sort by lots available
            for carpark_data in sorted_carparks:
                carpark_no = carpark_data[0]
                total_lots = int(carpark_data[1])
                available_lots = int(carpark_data[2])
                available_percentage = (available_lots / total_lots) * 100 if total_lots != 0 else 0
                address = next((item['Address'] for item in data_list if item['Carpark Number'] == carpark_no),
                               'Address not found')
                output_file.write(
                    "{},{},{},{:.1f},{}\n".format(carpark_no, total_lots, available_lots, available_percentage,
                                                  address))

        result_text.config(state=tk.NORMAL)  #Enable editing
        result_text.delete("1.0", tk.END)  #Clear existing text
        result_text.insert(tk.END, "Data written to '{}'. Total lines written: {}\n".format(output_file_name,
                                                                                            len(sorted_carparks)))
        result_text.config(state=tk.DISABLED)  #Disable editing after insertion
    except Exception as e:
        result_text.config(state=tk.NORMAL)  #Enable editing
        result_text.delete("1.0", tk.END)  #Clear existing text
        result_text.insert(tk.END, "Error writing to the output file: {}\n".format(e))
        result_text.config(state=tk.DISABLED)


def update_result_text(content):
    result_text.config(state=tk.NORMAL)  #Enable editing
    result_text.delete("1.0", tk.END)     #Clear existing text
    result_text.insert(tk.END, content)   #Insert new content
    result_text.config(state=tk.DISABLED) #Disable editing after insertion


#Input the title of program and other info
root = tk.Tk()
root.title("Carpark Information System")

title_label = tk.Label(root, text="Carpark Information System", font=("Helvetica", 35, "bold"))
title_label.pack(pady=20)

menu_label = tk.Label(root, text="MENU", font=("Helvetica", 18, "underline"))
menu_label.pack()

#Set fixed dimensions for window
window_width = 1000
window_height = 800
root.geometry(f"{window_width}x{window_height}")

#Set colours for window
root.configure(bg="#AEC6CF")
title_label.configure(bg="#AEC6CF")
menu_label.configure(bg="#AEC6CF")


#Create Buttons and entry field
button1 = tk.Button(root, text="1. Display Total Number of Carparks", command=display_total_carparks)
button1.pack()

button2 = tk.Button(root, text="2. Display All Basement Carparks", command=display_basement_carparks)
button2.pack()


input_file_label = tk.Label(root, text="Enter File Name (Then press 3.):") #reate a label and entry widget for entering the file name
input_file_label.pack()
input_file_label.configure(bg="#AEC6CF")

input_file_entry = tk.Entry(root)
input_file_entry.pack()

button3 = tk.Button(root, text="3. Read Carpark Availability Data File", command=read_carpark_availability_file)
button3.pack()

button4 = tk.Button(root, text="4. Print Total Number of Carparks", command=print_total_carparks)
button4.pack()

button5 = tk.Button(root, text="5. Display Carparks Without Available Lots", command=display_carparks_without_available_lots)
button5.pack()

min_available_percentage_label = tk.Label(root, text="Minimum Available Percentage (For 6 and 7):")
min_available_percentage_label.pack()
min_available_percentage_label.configure(bg="#AEC6CF")

min_available_percentage_entry = tk.Entry(root)
min_available_percentage_entry.pack()

button6 = tk.Button(root, text="6. Display Carparks With At Least x% Available Lots", command=display_carparks_with_min_available_percentage)
button6.pack()

button7 = tk.Button(root, text="7. Display Addresses of Carparks With At Least x% Available Lots", command=display_carparks_with_min_available_percentage_with_address)
button7.pack()

button8 = tk.Button(root, text="8. Display Carparks at Location", command=display_carparks_at_location)
button8.pack()

input_location_label = tk.Label(root, text="Enter Location:")
input_location_label.pack()

input_location_entry = tk.Entry(root)
input_location_entry.pack()

button9 = tk.Button(root, text="9. Display Carpark with Most Available Lots", command=display_carpark_with_most_available_lots)
button9.pack()

button10 = tk.Button(root, text="10. Save Sorted Carparks with Addresses", command=save_sorted_carparks_with_addresses)
button10.pack()

space_label = tk.Label(root, text="", font=("Helvetica", 4))
space_label.pack()
space_label.configure(bg="#AEC6CF")

exit_button = tk.Button(root, text="Exit", command=root.quit, width=5, height=2, font=("Helvetica", 10))  #Increase font size
exit_button.pack()


#Create a label to display the results
result_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=300)
result_label.pack()
result_label.configure(bg="#AEC6CF")

result_text = tk.Text(root, font=("Helvetica", 12), wrap=tk.WORD, height=20)
result_text.pack(fill=tk.BOTH, expand=True)
result_text.config(state=tk.DISABLED)

root.mainloop()