# Stock Market Price Checker Documentation

## Overview
The **Stock Market Price Checker** application provides a convenient way to check real-time stock prices. It supports both international and Indian stock markets, using Yahoo Finance as the data source. The application is built with Python and Tkinter, ensuring an intuitive graphical user interface.

---

## Features
1. **Real-Time Stock Prices**: Fetches the latest stock prices for international stocks (in USD) and Indian stocks (in INR).
2. **Validation**: Ensures valid stock symbols are entered, providing error messages for invalid input.
3. **User-Friendly Interface**: Simple and clean GUI for easy usage.
4. **Help and About**: Built-in menu options to guide users and provide information about the application.

---

## How to Use
1. **Enter the Stock Symbol**:
   - For international stocks, enter symbols like `AMZN` for Amazon.
   - For Indian stocks, enter symbols like `TATASTEEL.BO` or `TCS.NS`.
   - Note: Stock symbols are case-sensitive but will automatically convert to uppercase in the application.

2. **Click "Show Price"**:
   - After entering the symbol, press the button to fetch the stock price.

3. **View the Result**:
   - The stock price will be displayed below the button, along with its currency.

4. **Check the Status**:
   - A status message will indicate whether the price was fetched successfully or if there was an error.

---

## Code Description
The application consists of the following main components:

1. **fetch_and_display_stock_price(stock_symbol)**:
   - Retrieves the stock price using the `yfinance` library.
   - Handles errors like invalid stock symbols or data unavailability.
   - Updates the GUI with the fetched price or an error message.

2. **stock_price()**:
   - Gets the user-input stock symbol, validates it, and calls the fetch function.

3. **force_uppercase()**:
   - Ensures the stock symbol entered is always converted to uppercase.

4. **Menu Options**:
   - **About**: Displays information about the application.
   - **Help**: Explains how to use the application.

5. **Graphical User Interface (GUI)**:
   - Built with Tkinter.
   - Includes input fields, buttons, labels, and menus styled for user-friendliness.

---

## Setup Instructions

1. **Install Required Libraries**:
   - Make sure Python is installed on your system.
   - Install the necessary Python library:
     ```bash
     pip install yfinance
     ```

2. **Run the Application**:
   - Save the code in a Python file (e.g., `stock_checker.py`).
   - Open a terminal or command prompt and execute:
     ```bash
     python stock_checker.py
     ```

3. **Usage**:
   - Follow the steps in the "How to Use" section to check stock prices.

---

## User Interface
- **Input Field**: A text box to enter the stock symbol.
- **Show Price Button**: A button to trigger the stock price retrieval.
- **Result Display**: A label to show the stock price and its currency.
- **Status Message**: A label to display the success or error message.
- **Menus**: Options for "Help" and "About."

---

## Error Handling
- **Empty Input**: Displays a warning if no stock symbol is entered.
- **Invalid Symbols**: Shows an error message for invalid or unrecognized symbols.
- **Other Errors**: Handles unexpected errors with an error dialog box.

---

## Example
- **Input**: `TATASTEEL.BO`
- **Output**: ₹`120.50 (INR)` (example value)

---

## Demo Video
For a detailed walkthrough and live demonstration of the application, watch the video on YouTube:
[Stock Market Price Checker Demo](https://youtu.be/jhMZlUGY2YY?si=nTUeAnwYzIm487lt)

---

## Credits
- **Developers**: A&J
- **Version**: 1.0
- **Library Used**: yfinance

---

For any issues or suggestions, please contact the developers. Happy stock tracking!

