# Steam API Investment Tracker

## Overview
The **Steam API Investment Tracker** is a streamlined tool designed to help you monitor and analyze your investment portfolio on the Steam Market. With just a simple CSV input, this program fetches the latest median prices for each of your items and calculates the total Profit and Loss (PNL) of your investments.

## Features
- **Easy Input**: Provide your investment data in a CSV file named `input.csv` using the format: `Item,QTY,Purchase price`.
- **Steam API Integration**: Seamlessly fetches the median price for each item directly from the Steam API.
- **Investment Insights**: Calculates the total PNL for your entire investment portfolio.
- **Detailed Output**: Generates an `output.csv` file with comprehensive details on each item's purchase price, current median price, and individual PNL.

## How It Works
1. **Prepare Your CSV**: List all your items in `input.csv` with the quantity and purchase price.
2. **Run the Tracker**: Execute the program to process your data.
3. **Review Your Investments**: Check `output.csv` for a detailed breakdown of your portfolio's performance.

## Output Format
The output CSV file will include the following columns for each item:
- `Item`: The name of the item.
- `QTY`: Quantity of the item purchased.
- `Purchase price`: The price at which the item was purchased.
- `Total purchase price`: The total amount spent on the item.
- `Steam Median price`: The current median price of the item on Steam.
- `Total price`: The total value of the item at the current median price.
- `PNL`: The profit or loss for the item.

## Getting Started
To use the Steam API Investment Tracker, ensure you have Python installed on your system and the necessary permissions to make requests to the Steam API.

## Disclaimer
This tool is not affiliated with or endorsed by Steam or Valve Corporation. The accuracy of the data is dependent on the Steam API's current responses and market conditions.

## License
This project is open-source and available under the MIT License.
