from date_classes import current_year, next_month, Year

def apr_daily_compound(principal:float, payment:float, apr:float) -> int:
    """ computes the number of monthly payments required to pay off a loan with daily compounding APR """
    run = True
    year_count = 0
    payment_count = 0
    if payment < 31*principal*apr/365:
        print("Payment too small to pay off loan")
        return 0
    while run:
        year = Year(current_year(), next_month()) if year_count==0 else Year(current_year() + year_count)
        daily_apr = apr/365 if not year.leap else apr/366
        for month in year:
            for _ in range(month.days):
                principal += principal*daily_apr
            principal -= payment
            payment_count += 1
            if principal <= 0:
                run = False
                break
        year_count += 1
    return payment_count
    
def apr_monthly_compound(principal:float, payment:float, apr:float) -> int:
    """ computes the number of monthly payments required to pay off a loan with monthly compounding APR """
    run = True
    year_count = 0
    payment_count = 0
    if payment < 31*principal*apr/365:
        print("Payment too small to pay off loan")
        return 0
    while run:
        year = Year(current_year(), next_month()) if year_count==0 else Year(current_year() + year_count)
        daily_apr = apr/365 if not year.leap else apr/366
        for month in year:
            principal +=  month.days*principal*daily_apr - payment
            payment_count += 1
            if principal <= 0:
                run = False
                break
        year_count += 1
    return payment_count


def  apr_daily_compound_accrue(principal:float, payment:float, apr:float) -> float:
    """ computes the total interest over the remainder of the loan """
    run = True
    year_count = 0
    # payment_count = 0
    total_interest = 0
    if payment < 31*principal*apr/365:
        print("Payment too small to pay off loan")
        return 0
    while run:
        year = Year(current_year(), next_month()) if year_count==0 else Year(current_year() + year_count)
        daily_apr = apr/365 if not year.leap else apr/366
        for month in year:
            month_interest = month.days*principal*daily_apr
            principal += month_interest - payment
            total_interest += month_interest
            # payment_count += 1
            if principal <= 0:
                run = False
                break
        year_count += 1
    return total_interest
