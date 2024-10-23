# Task 1
# Objective: Write a function the iterate over a list of tuples and return a formatted string of each tuple.

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Carrol", "Tablet", 2),
    ("David", "Smartphone", 3),
]

# Function to iterate over a list of tuples and return a formatted string of each tuple
def order_list(orders):

    # formatted_orders list to store formatted strings of each order
    formatted_orders = []

    # Loop through each order in the list and return an index ('index') and tuple ('order')
    for index, order in enumerate(orders):

        # Append formatted string to the list: "Order (order num): (name) ordered (quantity) of (item)"
        formatted_orders.append(f"Order {index+1}: {order[0]} ordered {order[2]} {order[1]}")

    # Return the formatted strings as a single string with new lines
    return "\n".join(formatted_orders)

print(order_list(orders))