#1)Demand - Supply Mismatch Analysis
zone_regional_zone_weights = {}
with open('FMCG_Data.csv', mode='r') as filereader:
    header_data = filereader.readline().strip().split(',')
    zone_index = header_data.index('zone')
    regional_zone_index = header_data.index('WH_regional_zone')
    product_weight_index = header_data.index('product_wg_ton')
    for line in filereader:
        file_datas = line.strip().split(',')
        zone = file_datas[zone_index]
        regional_zone = file_datas[regional_zone_index]
        try:
            product_weight = float(file_datas[product_weight_index])
        except ValueError:
            continue
        exp = (zone, regional_zone)
        if exp in zone_regional_zone_weights:
            zone_regional_zone_weights[exp] += product_weight
        else:
            zone_regional_zone_weights[exp] = product_weight
    for exp, total_weight in zone_regional_zone_weights.items():
        print(f'Zone: {exp[0]}, Regional Zone: {exp[1]}, Total Supply Weight: {total_weight}')

#2)Warehouse Refill Frequency Correlation
def convert_capacity_to_numeric(capacity_size):
    size_map = {
        'Small': 1,
        'Mid': 2,
        'Large': 3
    }
    return size_map.get(capacity_size, 0)
capacities = []
refill_requests = []
with open('FMCG_Data.csv', mode='r') as filereader:
    header_data = filereader.readline().strip().split(',')
    capacity_index = header_data.index('WH_capacity_size')
    refill_index = header_data.index('num_refill_req_l3m')
    for exp in filereader:
        file_datas = exp.strip().split(',')
        try:
            capacity = convert_capacity_to_numeric(file_datas[capacity_index])
            refill = float(file_datas[refill_index])
            capacities.append(capacity)
            refill_requests.append(refill)
        except ValueError:
            continue


def calculate_correlation_data(x, y):
    n = len(x)
    if n == 0:
        return False
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator_x = sum((xi - mean_x) ** 2 for xi in x) ** 0.5
    denominator_y = sum((yi - mean_y) ** 2 for yi in y) ** 0.5
    if denominator_x == 0 or denominator_y == 0:
        return False
    return numerator / (denominator_x * denominator_y)

correlation = calculate_correlation_data(capacities, refill_requests)
if correlation is not False:
    print(f"Correlation coefficient: {correlation}")
else:
    print(" data to compute correlation is insufficient.")

#3)Transport Issue Impact Analysis

issue_weights = {}
with open('FMCG_Data.csv', mode='r') as filereader:
    headers_data = filereader.readline().strip().split(',')
    issue_index = headers_data.index('transport_issue_l1y')
    product_weight_index = headers_data.index('product_wg_ton')
    for exp in filereader:
        values = exp.strip().split(',')
        issue_data = values[issue_index]
        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
            continue
        if issue_data in issue_weights:
            issue_weights[issue_data] += product_weight
        else:
            issue_weights[issue_data] = product_weight
    for exp, total_weight in issue_weights.items():
        print(f'Transport Issue: {exp}, Total Supply Weight: {total_weight}')

#4)Storage Issue Analysis

storage_issue_weights = {}
with open('FMCG_Data.csv', mode='r') as file:
    headers = file.readline().strip().split(',')
    issue_index = headers.index('storage_issue_reported_l3m')
    product_weight_index = headers.index('product_wg_ton')
    for line in file:
        values = line.strip().split(',')
        issue_data = values[issue_index]
        try:
            product_weight = float(values[product_weight_index])
        except ValueError:
             continue
        if issue_data in storage_issue_weights:
            storage_issue_weights[issue_data] += product_weight
        else:
            storage_issue_weights[issue_data] = product_weight
    for exp, total_weight in storage_issue_weights.items():
        print(f'Storage Issue: {exp}, Total Supply Weight: {total_weight}')