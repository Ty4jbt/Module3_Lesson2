# Task 1
# Take a list of tuples and write a function to return a string that lists each itinerary in the list.
# eg) [("Alice", "New York", "London"), ("Bob", "Tokyo", "Sanfrancisco")]
# Should return: "Itinerary 1: Alice - New York to London, Itinerary 2: Bob - Tokyo to Sanfrancisco"

# itinerary_list function that takes a list of tuples as an argument
def itinerary_list(itinerary):

    # formatted_itineraries list to store formatted strings of each itinerary
    formatted_itineraries = []

    # Loop through each itinerary in the list and return an index ('index') and tuple ('trip')
    for index, (name, origin, destination) in enumerate(itinerary):

        # Append formatted string to the list: "Itinerary (itinerary num): (name) - (origin) to (destination)"
        formatted_itineraries.append(f"Itinerary {index+1}: {name} - {origin} to {destination}")

    # Return the formatted strings as a single string with new lines
    return "\n".join(formatted_itineraries)

print(itinerary_list([("Alice", "New York", "London"), ("Bob", "Tokyo", "Sanfrancisco")]))