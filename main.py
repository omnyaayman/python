# main.py
# Run full analysis for Food Delivery project

from analysis import analyze_data

def display_results(results):
    print("📊 Food Delivery Analysis")
    print("-" * 35)
    print(f"Total Orders: {results['total_orders']}")
    print(f"Average Delivery Time: {results['avg_delivery_time']} minutes")
    print(f"Fastest Delivery: {results['fastest_delivery']} minutes")
    print(f"Slowest Delivery: {results['slowest_delivery']} minutes")
    print(f"Average Rating: {results['avg_rating']}")
    print(f"Average Price: {results['avg_price']} EGP")
    print("-" * 35)

if _name_ == "_main_":
    results = analyze_data()
    display_results(results)
