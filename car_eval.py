# The purpose of this program is to evaluate the best decision between three options
# Option 1: Purchase a car outright using an interest rate pegged to a mortage rate
# Option 2: Use a novated lease for a one year term
# Option 3: Use a novated lease for a two year term

# Key paramters
purchase_price_GST = 40000 # inclusive of GST
lease_price_NOGST = 36000
mortgate_int = 0.05
lease_costs_1 = np.array([350, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
lease_costs_2 = np.array([350, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# import appropriate packages
import numpy as np
# Calculate the NPV of purchasing the car outright
purchase = np.npv(-purchase_price_GST)



