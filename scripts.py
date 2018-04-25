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

# Calculate the value of two separate investments projecting FV for two interest rates note the negative (-) value for PV

import numpy as np

# Caculate investment_1
investment_1 = np.fv(rate=0.05, nper=15, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 15 years")

# Caculate investment_2
investment_2 = np.fv(rate=0.08, nper=15, pmt=0, pv=-10000)
print("Investment 2 will yield a total of $" + str(round(investment_2, 2)) + " in 15 years")

# Calculate the FV of an investment and then discount by projected inflation rate

import numpy as np

# Calculate investment_1
investment_1 = np.fv(rate=0.08, nper=10, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 10 years")

# Calculate investment_2
investment_1_discounted = np.pv(rate=0.03, nper=10, pmt=0, fv=investment_1)
print("After adjusting for inflation, investment 1 is worth $" + str(round(-investment_1_discounted, 2)) + " in today's dollars")

# Discount a series of cash flows to calculate NPV
import numpy as np

# Predefined array of cash flows
cash_flows = np.array([100, 100, 100, 100, 100])

# Calculate investment_1
investment_1 = np.npv(rate=0.03, values=cash_flows)
print("Investment 1's net present value is $" + str(round(investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = np.npv(rate=0.05, values=cash_flows)
print("Investment 2's net present value is $" + str(round(investment_2, 2)) + " in today's dollars")

# Calculate investment_3
investment_3 = np.npv(rate=0.07, values=cash_flows)
print("Investment 3's net present value is $" + str(round(investment_3, 2)) + " in today's dollars")

# Calculate the NPV value of a series of cash flows from arrays
import numpy as np

# Create an array of cash flows for project 1
cash_flows_1 = np.array([-250, 100, 200, 300, 400])

# Create an array of cash flows for project 2
cash_flows_2 = np.array([-250, 300, -250, 300, 300])

# Calculate the net present value of project 1
investment_1 = np.npv(rate=0.03, values=cash_flows_1)
print("The net present value of Investment 1 is worth $" + str(round(investment_1, 2)) + " in today's dollars")

# Calculate the net present value of project 2
investment_2 = np.npv(rate=0.03, values=cash_flows_2)
print("The net present value of Investment 2 is worth $" + str(round(investment_2, 2)) + " in today's dollars")

# Calculate the impact of discount at different thresholds of years
import numpy as np

# Calculate investment_1
investment_1 = np.pv(rate=0.03, nper=30, pmt=0, fv=100)
print("Investment 1 is worth $" + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = np.pv(rate=0.03, nper=50, pmt=0, fv=100)
print("Investment 2 is worth $" + str(round(-investment_2, 2)) + " in today's dollars")

# Calculate investment_3
investment_3 = np.pv(rate=0.03, nper=100, pmt=0, fv=100)
print("Investment 3 is worth $" + str(round(-investment_3, 2)) + " in today's dollars")

# Create arrays in multiples of 1000
import numpy as np

# Create a numpy array of cash flows for Project 1
cf_project_1 = np.array([-1000, 200, 250, 300, 350, 400, 450, 500, 550, 600])

# Create a numpy array of cash flows for Project 2
cf_project_2 = np.array([-1000, 150, 225, 300, 375, 425, 500, 575, 600, 625])

# Scale the original objects by 1000x
cf_project1 = cf_project_1 * 1000
cf_project2 = cf_project_2 * 1000


