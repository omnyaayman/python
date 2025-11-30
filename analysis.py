# analysis.py
# Main analysis functions for Food Delivery Analysis project

from data import orders
from utils import average, max_value, min_value, count_items

def get_delivery_times():
    """Extract list of delivery times from orders."""
    return [order["delivery_time"] for order in orders]

def get_ratings():
    """Extract list of ratings from orders."""
    return [order["rating"] for order in orders]

def get_prices():
    """Extract list of prices from orders."""
    return [order["price"] for order in orders]

def analyze_data():
    """Perform full analysis and return results."""
    delivery_times = get_delivery_times()
    ratings = get_ratings()
    prices = get_prices()

    return {
        "total_orders": count_items(orders),
        "avg_delivery_time": average(delivery_times),
        "fastest_delivery": min_value(delivery_times),
        "slowest_delivery": max_value(delivery_times),
        "avg_rating": average(ratings),
        "avg_price": average(prices)
    }
