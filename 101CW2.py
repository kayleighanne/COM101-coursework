# This program will read in data from a text file containing food items
# and store the data within a list.
# The program will present the user with a set of menu options and will be
# able to sort the list, produce a report and query the list appropriately.

# Import the csv module to open the food_items.txt file.
import csv

# Define the main function
def main():

    # The program uses a single list into which the CSV values will be loaded from a file

    # Create an empty list to store the data from the input file.
    food_items = []

    # The CSV DictReader will convert each line of the csvfile into a dict
    # using the keys found on the first line.
    with open('food_items.txt', newline='') as csvfile:
        reader = csv.DictReader(csvfile, skipinitialspace=True)
        for item in reader:
            food_items.append(item)

    # skipinitialspace=True is used to control how the whitespace following the delimiter is
    # interpreted by the system.

    while True:
        # Print a seperator so that it is more user friendly if the program is run more
        # than once.
        print("\n\n------------------------------------------------------------")
        options = input("Menu:  Enter the number of the option you would like to select.\n"
                        "1. Output the number of meal records in the program.\n"
                        "2. Output a list of foods and details.\n"
                        "3. Output a report detailing the total calorie count of all foods.\n"
                        "4. Output all average serving weights.\n"
                        "5. Add a new food item.\n"
                        "6. Print a report of the number of items from each meal type.\n"
                        "7. Query the saturated fat threshold against food items.\n"
                        "8. Quit the program.\n"
                        "Enter option here: ")
        if options == '1':
            print("The number of meal records in the program is:", len(food_items))
            # Obtain the amount of records in the program using the len() function.
        elif options == '2':
            for item in food_items:
                # Print each food item within the program and their details
                print("Time: {0}, Type: {1}, Description: {2}, Serving: {3}, Calories: {4}, Saturated Fat: {5}"\
                      .format(item["TIME"], item["MTYPE"], item["DESC"], item["SERVING"], item["KCAL"], \
                        item["SFATg"]))
        elif options == '3':
            # Create a variable for calories.
            calories = 0
            for item in food_items:
                # Loop through each item within food_items and add up the KCAL of each record
                # to obtain the total calorie count of all foods.
                calories += int(item["KCAL"])
            print('Total calorie count of all foods: {0}'.format(calories))
        elif options == '4':
            # Create a variable for servings
            servings = 0
            for item in food_items:
                # Loop through each item within food_items and add up the serving weights of each
                # record to obtain the total serving weight of all items.
                servings += int(item["SERVING"])
                # Divide the total serving weight of all food items by the amount of records in
                # the program to obtain the average serving weight of all food items.
            print("Average serving weights for all food items: {0}".format(servings/len(food_items)))
        elif options == '5':
            # Create a new dictionary to store user input.
            ndict = {}

            # To add a new record to the program, add the users input to the corresponding key in the dictionary.
            ndict["TIME"] = input("Enter the meal time in the format HH:MM: ")
            ndict["MTYPE"] = input("Enter the meal type: ")
            ndict["DESC"] = input("Enter a description for the meal: ")
            ndict["SERVING"] = input("Enter the serving size in grams: ")
            ndict["KCAL"] = input("Enter the KCAL for the meal: ")
            ndict["SFATg"] = input("Enter the saturated fat per gram: ")
            food_items.append(ndict)
            print("Record added.")

            # Create a list into which records will be sorted by time.
            records = []
            for item in food_items:
                # Add the values to the list.
                records.append(list(item.values()))

            # Print the sorted record list
            for record in sorted(records):
                print(record)

        elif options == '6':
            # Create an empty dictionary to store the number of items for each meal type.
            aggregate = {}

            # Iterate over food_items and obtain a count for MTYPE
            for item in food_items:
                key = item['MTYPE']
                # If MTYPE appears in the aggregate dictionary, add 1 to the dictionary.
                if key in aggregate:
                    aggregate[key] += 1
                else:
                     aggregate[key] = 1
            # Print the number of items for each meal type.
            for k, v in aggregate.items():
                print("The number of items for {0} is {1}".format(k, v))

        elif options == '7':
            # The saturated fat threshold for an average food item is 3g.
            # If a food item has a saturated fat value greater than 3g, it will be returned by the function.

            results = []
            sfat_threshold = float(input("Please enter the saturated fat threshold in grams: "))

            for item in food_items:
                sfat = float(item["SFATg"])

                if sfat >  sfat_threshold:
                    results.append(item)

            for result in results:
                print("The food item",result["DESC"],"has a saturated fat value of",result["SFATg"],"g which is"
                        " above the threshold of", sfat_threshold, "g.")

        elif options == '8':
            # Print a message to let the user know that they are exiting the program.
            # Use the exit() function to end the program.
            print("Thank you for using this program.")
            exit()
        else:
            print("Please enter an option from the menu.")
        # Prompt the user to press a key to continue with the program.
        input("\nPress return to continue")

# Call the main function
main()
