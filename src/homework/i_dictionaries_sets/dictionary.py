# Global inventory dictionary to track widget quantities
inventory_dictionary = {}

def add_inventory(widget_name, quantity):
    """
    Adds a widget to the inventory or updates its quantity.
    """
    if widget_name in inventory_dictionary:
        inventory_dictionary[widget_name] += quantity
    else:
        inventory_dictionary[widget_name] = quantity

def remove_inventory_widget(widget_name):
    """
    Removes a widget from the inventory if it exists.
    Returns a message indicating result.
    """
    if widget_name in inventory_dictionary:
        del inventory_dictionary[widget_name]
        return 'Record deleted'
    else:
        return 'Item not found'
