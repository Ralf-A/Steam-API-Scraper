import csv
import requests

# Function to get median price from Steam
def get_median_price(item_name):
    item_name_encoded = item_name.replace(' ', '%20')
    url = f'https://steamcommunity.com/market/priceoverview/?currency=3&appid=730&market_hash_name={item_name_encoded}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'median_price' in data:
            # Remove currency symbol and convert to float
            return round(float(data['median_price'].strip('€').replace(',', '.')), 2) if data['median_price'] else "not available"
        else:
            return "Median price not available"
    else:
        return f"Failed to fetch data, status code: {response.status_code}"

# Function to process the CSV file and print total PNL
def process_csv(input_file, output_file):
    total_pnl = 0

    with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        items = list(reader)

    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Item', 'QTY', 'Purchase price', 'Total purchase price', 'Steam Median price', 'Total price', 'PNL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in items:
            median_price = get_median_price(item['Item'])
            if isinstance(median_price, float):
                total_purchase_price = round(int(item['QTY']) * float(item['Purchase price']), 2)
                total_price = round(int(item['QTY']) * median_price, 2)
                pnl = round(total_price - total_purchase_price, 2)
                total_pnl += pnl
                writer.writerow({
                    'Item': item['Item'],
                    'QTY': item['QTY'],
                    'Purchase price': item['Purchase price'],
                    'Total purchase price': total_purchase_price,
                    'Steam Median price': median_price,
                    'Total price': total_price,
                    'PNL': pnl
                })
            else:
                writer.writerow({
                    'Item': item['Item'],
                    'QTY': item['QTY'],
                    'Purchase price': item['Purchase price'],
                    'Total purchase price': "N/A",
                    'Steam Median price': median_price,
                    'Total price': "N/A",
                    'PNL': "N/A"
                })

    # Print the total PNL after processing all items
    print(f'Total PNL: {round(total_pnl, 2)}')

# Example usage
process_csv('input.csv', 'output.csv')
