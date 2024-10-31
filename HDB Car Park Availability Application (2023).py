#IMPORTANT NOTE BEFORE RUNNING:
#Move all CSV files to your main OS drive (C:\\) or code will not run properly


#Basic Requirement 1, Kieron Lim - CICTP02 (30/7/23)
with open('C:\\carpark-information.csv', 'r') as file: #use the open function
                                                       #to open the CSV file in read
                                                       #mode ('r').

                                                       #'with' statement is used to
                                                       #ensure that the file is
                                                       #properly closed after reading

    lines = file.readlines() #readlines() function reads all the lines from the file
                             #and stores them as a list in the lines variable

data_list = [] #list will store dictionaries representing the data of a single carpark.

#Extracting column headers
headers = lines[0].strip().split(',')

#Loop through the remaining lines and create dictionaries
for line in lines[1:]:                      #script loops through using 'for' loop
    values = line.strip().split(',')        #'carpark_dict' is created inside
    carpark_dict = {}                       #the loop

    for x, header in enumerate(headers):    #'enumerate' function used to iterate
        carpark_dict[header] = values[x]    #over 'headers' list and 'values' list
    data_list.append(carpark_dict)

#Print to check if data is correct
#for carpark_dict in data_list:
   # print(carpark_dict)

total_carpark_list = [] #used later to store availability data fo0r option 3



#Basic Requirement 2, Kieron Lim - CICTP02 (30/7/23)
while True: #While loop so program doesn't stop until 0 is pressed
    print()
    print("MENU")
    print("====")
    print("[1]   Display Total Number of Carparks in 'carpark-information.csv'")
    print("[2]   Display All Basement Carparks in 'carpark-information.csv'")
    print("[3]   Read Carpark Availability Data File")
    print("[4]   Print Total Number of Carparks in the File Read in [3]")
    print("[5]   Display Carparks Without Available Lots")
    print("[6]   Display Carparks With At Least x% Available Lots")
    print("[7]   Display Addresses of Carparks With At Least x% Available Lots")
    print("[8]   Display all Carparks at given location")
    print("[9]   Display Carpark with the Most Parking Lots")
    print("[10]  Create an Output File with Carpark Availability with Addresses and Sort by Lots Available")
    print("[0]   Exit")

    try:     #'try' block to handle potential 'ValueError' exceptions if the input is not a valid integer.

        option = int(input("Enter your option: "))
        if option == 0:                     #if '0', the program displays exit message and
            print("Exiting Program...")     #breaks out of the loop, ending the program.
            break
    except ValueError:                                          #If input is not a valid integer or is not equal to 0,
        print()                                                 #an error message is displayed,
        print('Invalid option, please only input numbers.')     #and program prompts the user to press 'Enter' to return to the menu.
        input("Press Enter to return to the Menu")
        continue

    if option < 0 or option > 10:                                                #After validating that the input is an integer,
        print()                                                                  #the code checks if the input is within the valid range of options (1 to 10).
        print('Invalid Option, please enter an option from 0 to 10 only.')       #If the input is outside this range, an error message is displayed,
        input("Press Enter to to return to the Menu")                            #and the user is prompted to press Enter to return to the menu.
        continue



#Basic Requirement 3, Kieron Lim - CICTP02 (2/8/23)
    if option == 1:                                                                                     #calculates and displays the total number of carparks
        print()                                                                                         #present in the 'carpark-information.csv' file.
        print("Option 1: Display Total Number of Carparks in 'carpark-information.csv'")
        print("Total Number of carparks in 'carpark-information.csv': {}.".format(len(data_list)))      #use the len(data_list) function



#Basic Requirement 4, Kieron Lim - CICTP02 (2/8/23)
    carpark_list = [] #Read data again from 'carpark-information.csv'
    file_name = 'C:\\carpark-information.csv'

    file = open(file_name, 'r')  #Open File
    lines = file.readlines()  #Read File
    file.close()  #Close file

    for line in lines:
        temp = line.strip('\n').split(',', 3)   #for loop and processes the data using the 'strip' and 'split' functions. This splits
        carpark_list.append(temp)               #the line into a list of values, with a maximum of 3 splits, which is then appended to the carpark_list.

    #Create dictionary to store
    cp_dict = {}
    header = carpark_list[0]                #uses the first entry in carpark_list as keys and the corresponding values from other entries in carpark_list as values.
    for entry in carpark_list[1:]:
        cp_dict[entry[0]] = entry[1:]

    if option == 2:
        print()
        print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
        print("{}\t{}\t\t{}".format('Carpark No', 'Carpark Type','Address'))

        x = 0
        for i in range(len(carpark_list)):
            if carpark_list[i][1] == 'BASEMENT CAR PARK':
                x += 1
                print("{:<12}{:<20}{:<}".format(carpark_list[i][0], carpark_list[i][1], carpark_list[i][3]))
        print('Total Number: {}'.format(x))



#Basic Requirement 5, Kieron Lim - CICTP02 (4/8/23)
    if option == 3:
        print()
        total_carpark_list.clear()  #clear() method ensures any previously read data is removed before reading new data
        print("Option 3: Read Carpark Availability Data File")
        file_name = input("Enter the file name: ").strip()

        try:
            with open('C:\\' + file_name, 'r') as file:     #using a 'with' statement and the 'r' read mode,
                lines = file.readlines()                    #reads all lines from the file is read and processes each
                for line in lines:                          #line to extract the relevant information. The 'split'
                    x = line.strip('\n').split(',')         #function is used to split each line by commas, and the resulting values are stored in the x list.
                    total_carpark_list.append(x)
                print(total_carpark_list[0][0])
        except FileNotFoundError:
            print()                                                     #if file is not found, code uses the 'FileNotFoundError' exception
            print("File not found. Please enter a valid file name.")    #prints an error message
            input("Press Enter to return to the Menu")                  #prompts user to press Enter to return
            continue



#Basic Requirement 6, Kieron Lim - CICTP02 (5/8/23)
    if option == 4:
        print()
        if len(total_carpark_list) > 0:     #check if total_carpark_list has any data read and stored from option 3
            print("Option 4: Print Total Number of Carparks in the file Read in [3]")
            print('Total number of Carparks in this file:', len(total_carpark_list) - 2)   #total number of carparks obtained by len(total_carpark_list)
                                                                                           #subtracted by 2 to account for the two header lines in the data file
        else:
            print("Please read a carpark availability file first (Option 3).")      #user validation



#Basic Requirement 7, Kieron Lim - CICTP02 (6/8/23)
    if option == 5:
        print()
        if len(total_carpark_list) == 0:
            print('Please read a carpark availability file first (Option 3)')
        else:
            print("Option 5: Display Carparks without Available Lots")
            p = 0       #variable 'p' to keep track of the count of carparks without available lots.

            for x in range(2, len(total_carpark_list)):     #Iterate through elements of total_carpark_list starting from index 2 (first two lines are headers).

                if total_carpark_list[x][2] == '0':     #Check no. of lots that are not available
                    print("Carpark Number: {}".format(total_carpark_list[x][0]))
                    p += 1

            print("Total number: {}".format(p))     #Print no. of carparks using 'p'



#Basic Requirement 8, Kieron Lim - CICTP02 (11/8/23)
    if option == 6:
        print()
        if len(total_carpark_list) == 0:
            print('Please read a carpark availability file first (Option 3)')
        else:
            print("Option 6: Display Carparks With At Least x% Available Lots")
            try:
                min_available_percentage = float(input("Enter the percentage required: "))
                if min_available_percentage < 0 or min_available_percentage > 100:
                    print()
                    print("Invalid percentage. Please enter a number between 0 and 100.")
                    input("Press Enter to to return to the Menu")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid numeric percentage.")
                input("Press Enter to to return to the Menu")
                continue

            print()
            print("{}\t{}\t{}\t{}".format('Carpark No', 'Total Lots', 'Lots Available','Percentage'))
            count = 0
            for carpark_data in total_carpark_list[2:]: #use for loop to get data
                carpark_no = carpark_data[0] #Get the carpark no
                total_lots = int(carpark_data[1]) #Get the total lots in the Carpark
                available_lots = int(carpark_data[2]) #get the available lots in the Carpark
                if total_lots != 0:  #Check if total_lots is non-zero to avoid division by zero
                    available_percentage = (available_lots / total_lots) * 100
                    if available_percentage >= min_available_percentage:
                        print("{:<12}{:>10}{:>16}{:>12.1f}".format(carpark_no, total_lots, available_lots, available_percentage))
                        count += 1
            if count == 0:
                print("No carparks meet the specified criteria.")
            else:
                print('Total Number: {}'.format(count))



#Basic Requirement 9, Kieron Lim - CICTP02 (11/8/23)
    if option == 7:
        print()
        if len(total_carpark_list) == 0:
            print('Please read a carpark availability file first (Option 3)')
        else:
            print("Option 7: Display Addresses of Carparks With At Least x% Available Lots")
            try:
                min_available_percentage = float(input("Enter the percentage required: "))
                if min_available_percentage < 0 or min_available_percentage > 100:
                    print()
                    print("Invalid percentage. Please enter a number between 0 and 100.")
                    input("Press Enter to to return to the Menu")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid numeric percentage.")
                input("Press Enter to to return to the Menu")
                continue

            print()
            print("{}\t{}\t{}\t{}\t{}".format('Carpark No', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))
            count = 0
            for carpark_data in total_carpark_list[2:]:  #use for loop to get data
                carpark_no = carpark_data[0]  #Get the carpark no
                total_lots = int(carpark_data[1])  #Get the total lots in the Carpark
                available_lots = int(carpark_data[2])  #get the available lots in the Carpark
                if total_lots != 0:  #Check if total_lots is non-zero to avoid division by zero
                    available_percentage = (available_lots / total_lots) * 100
                    if available_percentage >= min_available_percentage:
                        address = next((item['Address'] for item in data_list if item['Carpark Number'] == carpark_no), 'Address not found')#generator expression to search through data_list
                                                                                                                                            #retrieves the corresponding address using a list
                                                                                                                                            #comprehension-like syntax.
                        print("{:<12}{:>10}{:>16}{:>12.1f}\t{}".format(carpark_no, total_lots, available_lots, available_percentage, address))
                        count += 1
            if count == 0:
                print("No carparks meet the specified criteria.")
            else:
                print('Total Number: {}'.format(count))



#Advanced Requirement 1, Kieron Lim - CICTP02 (12/8/23)
    if option == 8:
        if len(total_carpark_list) == 0:
            print()
            print('Please read a carpark availability file first (Option 3)')
        else:
            print()
            location = input("Enter a location to search for carparks: ")
            print('Displaying all Carparks at {}:'.format(location))
            count = 0
            for carpark_data in total_carpark_list[2:]:
                carpark_no = carpark_data[0]
                total_lots = int(carpark_data[1])
                available_lots = int(carpark_data[2])
                available_percentage = (available_lots / total_lots) * 100 if total_lots != 0 else 0
                address = next((item['Address'] for item in data_list if item['Carpark Number'] == carpark_no),
                               'Address not found')
                if location.lower() in address.lower():
                    if count == 0:
                        print("{}\t{}\t{}\t{}\t{}".format('Carpark No.', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))
                    print("{:<12}{:>10}{:>16}{:>12.1f}\t{}".format(carpark_no, total_lots, available_lots, available_percentage, address))
                    count += 1
            if count == 0:
                print("Error: No carparks found at the specified location.")
            else:
                print('Total Number: {}'.format(count))



    #Advanced Requirement 2, Kieron Lim - CICTP02 (12/8/23)
    if option == 9:
        if len(total_carpark_list) == 0:
            print()
            print('Please read a carpark availability file first (Option 3)')
        else:
            most_lots = 0
            most_lots_carpark = ''
            for carpark_data in total_carpark_list[2:]:
                carpark_no = carpark_data[0]
                available_lots = int(carpark_data[2])
                if available_lots > most_lots:
                    most_lots = available_lots
                    most_lots_carpark = carpark_no

            if most_lots_carpark:
                print()
                print("Carpark with the most available lots:")
                print("{}\t{}\t{}\t{}\t{}".format('Carpark No.', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))
                carpark_data = next(item for item in total_carpark_list[2:] if item[0] == most_lots_carpark)
                total_lots = int(carpark_data[1])
                available_lots = int(carpark_data[2])
                available_percentage = (available_lots / total_lots) * 100 if total_lots != 0 else 0
                address = next((item['Address'] for item in data_list if item['Carpark Number'] == most_lots_carpark), 'Address not found')
                print("{:<12}{:>10}{:>16}{:>12.1f}\t{}".format(most_lots_carpark, total_lots, available_lots, available_percentage, address))
            else:
                print()
                print("No carparks found with available lots.")



#Advanced Requirement 3, Kieron Lim - CICTP02 (12/8/23)
    if option == 10:
        if len(total_carpark_list) == 0:
            print()
            print('Please read a carpark availability file first (Option 3)')
        else:
            output_file_name = 'carpark-availability-with-addresses.csv'
            try:
                with open(output_file_name, 'w') as output_file:
                    output_file.write("Carpark No.,Total Lots,Lots Available,Percentage,Address\n")
                    sorted_carparks = sorted(total_carpark_list[2:], key=lambda x: int(x[2]))  #The key parameter with 'lambda' function that
                                                                                               #takes each sub-list x and returns int(x[2]),
                                                                                               #which is the integer value of the available lots.
                    for carpark_data in sorted_carparks:
                        carpark_no = carpark_data[0]
                        total_lots = int(carpark_data[1])
                        available_lots = int(carpark_data[2])
                        available_percentage = (available_lots / total_lots) * 100 if total_lots != 0 else 0
                        address = next((item['Address'] for item in data_list if item['Carpark Number'] == carpark_no), 'Address not found')
                        output_file.write(
                            "{},{},{},{:.1f},{}\n".format(carpark_no, total_lots, available_lots, available_percentage, address))
                print()
                print("Data written to '{}'. Total lines written: {}".format(output_file_name, len(sorted_carparks)))
            except Exception as e:
                print()
                print("Error writing to the output file: {}".format(e))

    print()
    #Wait for user input to continue
    input("Press Enter to continue...")
