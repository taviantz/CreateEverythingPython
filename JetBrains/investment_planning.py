# Filename: investment_planning.py

def calculate_investment_value(principal, annual_rate, years):
    """

    Calculate the value of an investment with compound interest.

    Parameters:
    principal (float): The initial amount of money invested.
    annual_rate (float): The annual interest rate in percentage.
    years (int): The number of years the money is invested.

    Returns:
    float: Thefuture value of the investment.
    """
    future_value = principal* (1 + annual_rate / 100) ** years
    return future_value

def main():
    # Initial investment amount
    principal = 1000
    # Annual interest rate in percentage
    annual_rate = 5
    # Number of years
    years = 10

    # Calculate the future value of the investment
    future_value = calculate_investment_value(principal, annual_rate, years)

    # Printing the result
    print(f"The future value of the investment after {years} years is: ${future_value:.2f}")

# Relatable answer to the JetBrains problem
# X = 1000
# r = 5
# y = 10
# x = X
# investment = x * (1+ r / 100) ** y
# print(investment)
 
if __name__ == "__main__":
    main()