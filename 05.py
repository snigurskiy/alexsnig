# Import decimal and getcontext from decimal module
from decimal import Decimal, getcontext

# Set the precision for decimal operations
getcontext().prec = 28
def complex_interest(A):
    # Calculate the interest rate as a Decimal
    r = Decimal(0.15)
    
    # Calculate the number of years as a Decimal
    t = Decimal(10)
    P = Decimal(A)  # Principal amount as a Decimal
    n = Decimal(12)  # Number of times interest is compounded per year

    # Calculate the final amount using the compound interest formula
    A = P * (1 + (r / n)) ** (n * t)

    return A