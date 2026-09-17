"""
Financial Loan EMI Calculator Module
Provides functions to calculate EMI, total interest, and total payment for loans.
"""

import math

def calculate_emi(principal: float, annual_rate: float, tenure_months: int) -> float:
    """
    Calculate Equated Monthly Installment (EMI) for a loan.
    
    Args:
        principal: Loan amount (positive float)
        annual_rate: Annual interest rate in percentage (positive float)
        tenure_months: Loan tenure in months (positive integer)
    
    Returns:
        EMI amount rounded to 2 decimal places
    
    Raises:
        ValueError: If any input is non-positive
    """
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if annual_rate <= 0:
        raise ValueError("Annual interest rate must be positive")
    if tenure_months <= 0:
        raise ValueError("Tenure must be positive")
    
    # Convert annual rate to monthly decimal rate
    monthly_rate = annual_rate / 12 / 100
    
    # EMI formula: P * r * (1+r)^n / ((1+r)^n - 1)
    if monthly_rate == 0:
        emi = principal / tenure_months
    else:
        emi = (principal * monthly_rate * math.pow(1 + monthly_rate, tenure_months)) / \
              (math.pow(1 + monthly_rate, tenure_months) - 1)
    
    return round(emi, 2)

def calculate_total_interest(principal: float, annual_rate: float, tenure_months: int) -> float:
    """
    Calculate total interest payable over the loan tenure.
    
    Args:
        principal: Loan amount (positive float)
        annual_rate: Annual interest rate in percentage (positive float)
        tenure_months: Loan tenure in months (positive integer)
    
    Returns:
        Total interest amount rounded to 2 decimal places
    """
    emi = calculate_emi(principal, annual_rate, tenure_months)
    total_payment = emi * tenure_months
    total_interest = total_payment - principal
    return round(total_interest, 2)

def calculate_total_payment(principal: float, annual_rate: float, tenure_months: int) -> float:
    """
    Calculate total payment (principal + interest) over the loan tenure.
    
    Args:
        principal: Loan amount (positive float)
        annual_rate: Annual interest rate in percentage (positive float)
        tenure_months: Loan tenure in months (positive integer)
    
    Returns:
        Total payment amount rounded to 2 decimal places
    """
    emi = calculate_emi(principal, annual_rate, tenure_months)
    total_payment = emi * tenure_months
    return round(total_payment, 2)

def calculate_principal(emi: float, annual_rate: float, tenure_months: int) -> float:
    """
    Calculate principal amount from EMI, interest rate, and tenure.
    
    Args:
        emi: Monthly EMI amount (positive float)
        annual_rate: Annual interest rate in percentage (positive float)
        tenure_months: Loan tenure in months (positive integer)
    
    Returns:
        Principal amount rounded to 2 decimal places
    
    Raises:
        ValueError: If any input is non-positive
    """
    if emi <= 0:
        raise ValueError("EMI must be positive")
    if annual_rate <= 0:
        raise ValueError("Annual interest rate must be positive")
    if tenure_months <= 0:
        raise ValueError("Tenure must be positive")
    
    monthly_rate = annual_rate / 12 / 100
    
    if monthly_rate == 0:
        principal = emi * tenure_months
    else:
        principal = (emi * (math.pow(1 + monthly_rate, tenure_months) - 1)) / \
                    (monthly_rate * math.pow(1 + monthly_rate, tenure_months))
    
    return round(principal, 2)

def calculate_tenure(principal: float, annual_rate: float, emi: float) -> int:
    """
    Calculate loan tenure in months from principal, interest rate, and EMI.
    
    Args:
        principal: Loan amount (positive float)
        annual_rate: Annual interest rate in percentage (positive float)
        emi: Monthly EMI amount (positive float)
    
    Returns:
        Loan tenure in months (rounded up to nearest integer)
    
    Raises:
        ValueError: If any input is non-positive or if EMI is insufficient
    """
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if annual_rate <= 0:
        raise ValueError("Annual interest rate must be positive")
    if emi <= 0:
        raise ValueError("EMI must be positive")
    
    monthly_rate = annual_rate / 12 / 100
    
    # Check if EMI is sufficient to cover interest
    monthly_interest = principal * monthly_rate
    if emi <= monthly_interest:
        raise ValueError("EMI is insufficient to cover interest")
    
    # Calculate tenure using formula: n = log(EMI/(EMI - P*r)) / log(1+r)
    if monthly_rate == 0:
        tenure = principal / emi
    else:
        tenure = math.log(emi / (emi - principal * monthly_rate)) / math.log(1 + monthly_rate)
    
    # Round up to nearest integer (you can't have fractional months in practice)
    return math.ceil(tenure)

if __name__ == "__main__":
    # Example usage
    try:
        principal = 1000000
        rate = 8.5
        tenure = 120
        
        emi = calculate_emi(principal, rate, tenure)
        total_interest = calculate_total_interest(principal, rate, tenure)
        total_payment = calculate_total_payment(principal, rate, tenure)
        
        print(f"Loan Details:")
        print(f"Principal: ₹{principal:,.2f}")
        print(f"Annual Interest Rate: {rate}%")
        print(f"Tenure: {tenure} months ({tenure//12} years)")
        print(f"EMI: ₹{emi:,.2f}")
        print(f"Total Interest Payable: ₹{total_interest:,.2f}")
        print(f"Total Payment: ₹{total_payment:,.2f}")
        
        # Reverse calculation
        calc_principal = calculate_principal(emi, rate, tenure)
        calc_tenure = calculate_tenure(principal, rate, emi)
        
        print(f"\nReverse Calculations:")
        print(f"Calculated Principal from EMI: ₹{calc_principal:,.2f}")
        print(f"Calculated Tenure from EMI: {calc_tenure} months")
        
    except ValueError as e:
        print(f"Error: {e}")