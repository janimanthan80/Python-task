import json

# Load the JSON file
with open('Python-task.json', 'r') as file:
    data = json.load(file)

# Extract data from the 'assignment_results' key
assignment_results = data['assignment_results']

# Initialize variables to find the cheapest price
cheapest_price = float('inf')  # Start with an infinitely large number
cheapest_room_type = None
cheapest_number_of_guests = None

# Open a file to write the output
with open('output.txt', 'w') as output_file:
    for result in assignment_results:
        # Get the hotel information
        number_of_guests = result['number_of_guests']
        shown_price = result['shown_price']
        net_price = result['net_price']

        # Iterate through each room type to find the cheapest price
        for room_type, price_str in shown_price.items():
            price = float(price_str)
            if price < cheapest_price:
                cheapest_price = price
                cheapest_room_type = room_type
                cheapest_number_of_guests = number_of_guests

        # Calculate and write total prices for all room types
        for room_type, price_str in net_price.items():
            net_price_value = float(price_str)
            # Taxes are not provided, so just writing net price
            taxes = 0  # Default taxes to 0 if not provided
            total_price = net_price_value + taxes
            output_file.write(f"Room Type: {room_type}, Total Price: {total_price}\n")

    # Write the cheapest room details
    output_file.write(f"\nCheapest Room Type: {cheapest_room_type}, Number of Guests: {cheapest_number_of_guests}\n")
    output_file.write(f"Cheapest Price: {cheapest_price}\n")
