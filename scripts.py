# File contains random script from various tutorials

# Calculate the future value of the investment and print it out
# Below calculation assumes a $100 investment at 6% for 30 years
future_value = 100*(1+0.06)**30
print("Future Value of Investment: " + str(round(future_value, 2)))

# Calculating compound interest
# Predefined variables
initial_investment = 100
growth_periods = 30
growth_rate = 0.06

# Calculate the value for the investment compounded once per year
compound_periods_1 = 1
investment_1 = initial_investment*(1+growth_rate / compound_periods_1)**(growth_periods * compound_periods_1)
print("Investment 1: " + str(round(investment_1, 2)))

# Calculate the value for the investment compounded quarterly
compound_periods_2 = 4
investment_2 = initial_investment*(1+growth_rate / compound_periods_2)**(growth_periods * compound_periods_2)
print("Investment 2: " + str(round(investment_2, 2)))

# Calculate the value for the investment compounded monthly
compound_periods_3 = 12
investment_3 = initial_investment*(1+growth_rate / compound_periods_3)**(growth_periods * compound_periods_3)
print("Investment 3: " + str(round(investment_3, 2)))

# Discount factors and depreciation
# Calculate the future value
initial_investment = 100
growth_rate = -0.05
growth_periods = 10
future_value = initial_investment * (1 + growth_rate) ** growth_periods
print("Future value: " + str(round(future_value, 2)))

# Calculate the discount factor
discount_factor = 1 / (1 + growth_rate) ** growth_periods
print("Discount factor: " + str(round(discount_factor, 2)))

# Derive the initial value of the investment
initial_investment_again = future_value * discount_factor
print("Initial value: " + str(round(initial_investment_again, 2)))

# Using numpy packages to calculate financial values
# Import numpy as np
import numpy as np

# Calculate investment_1
investment_1 = np.pv(rate=0.03, nper=15, pmt=0, fv=10000)

# Note that the present value returned is negative, so we multiply the result by -1
print("Investment 1 is worth " + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = np.pv(rate=0.05, nper=10, pmt=0, fv=10000)
print("Investment 2 is worth " + str(round(-investment_2, 2)) + " in today's dollars")


