# The purpose of this program is to evaluate the best decision between three options
# The decision considers a 5 year term with a $10,000 residual future state value
# Option 1: Purchase a car outright using an interest rate pegged to a mortage rate
# Option 2: Use a novated lease for a one year term
# Option 3: Use a novated lease for a two year term

# import appropriate packages
import numpy as np

# Key parameters
purchase_price_GST = 40000 # inclusive of GST
residual_value = 10000 # value of vehicle after 10 years (estimated)
lease_price_NOGST = 36000
mortgate_int = 0.05 / 12
periods = 5 * 12
lease_costs_1 = np.array([350, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
lease_costs_2 = np.array([350, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Calculate the NPV of purchasing the car outright
option_1 = np.pv(rate=mortgate_int, nper=periods, pmt=0, fv=residual_value)
print("Option 1 is worth " + str(round(-option_1, 2)) + " in today's dollars")




