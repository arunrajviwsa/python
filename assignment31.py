import sys
import csv
from collections import defaultdict

supply_file_path = 'FMCG_data.csv'

def read_and_aggregate_supply(file_path):
    supply_data = defaultdict(float)  # Initialize a dictionary to store aggregated supply

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = (row['zone'], row['WH_regional_zone'])
            value = float(row['product_wg_ton'])
            # Emit key-value pair: (zone, WH_regional_zone) as key and product_wg_ton as value
            print(f"{key}\t{value}")


    return supply_data

supply_data = read_and_aggregate_supply(supply_file_path)