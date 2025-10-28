"""Inventory System Module
Provides functions to manage item stock information and demonstrates
basic inventory operations such as add, remove, and reporting.
"""

import json
from datetime import datetime

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a positive quantity of an item to stock_data and log the event.

    Args:
        item (str): Name of the item to add.
        qty (int): Quantity to add (must be positive).
        logs (list, optional): Log list to record the operation.
    """
    if logs is None:
        logs = []
    if not isinstance(item, str) or not item:
        return
    if not isinstance(qty, int) or qty <= 0:
        return  # Only allow positive quantities
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a positive quantity of an item from stock_data, delete if zero or negative.

    Args:
        item (str): Name of the item to remove.
        qty (int): Quantity to remove (must be positive).
    """
    if not isinstance(qty, int) or qty <= 0:
        return  # Only allow positive removals
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """Return the quantity of the given item in stock_data.

    Args:
        item (str): Item name to query.

    Returns:
        int: Quantity of the item, or 0 if not found.
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load stock_data from JSON file and update the global variable.

    Args:
        file (str): Filename to load from.

    Returns:
        dict: Updated stock_data.
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            loaded = json.load(f)
    except FileNotFoundError:
        return stock_data
    if isinstance(loaded, dict):
        stock_data.clear()
        stock_data.update(loaded)
    return stock_data


def save_data(file="inventory.json"):
    """Save stock_data to JSON file using safe open and encoding.

    Args:
        file (str): Filename to save into.
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, ensure_ascii=False)


def print_data():
    """Print a report of current items and quantities in stock_data."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """Return a list of items whose quantity falls below the threshold.

    Args:
        threshold (int): Quantity threshold.

    Returns:
        list: Items with quantity below threshold.
    """
    return [item for item, quantity in stock_data.items() if quantity < threshold]


def main():
    """Main function to demonstrate inventory system functionality."""
    logs = []
    add_item("apple", 10, logs)
    add_item("banana", 2, logs)  # Correct positive quantity
    add_item("grape", 7, logs)
    remove_item("apple", 3)
    remove_item("orange", 1)  # 'orange' does not exist, should not crash
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # eval removed for safety


if __name__ == "__main__":
    main()
