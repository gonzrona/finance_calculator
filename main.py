from interest_functions import apr_daily_compound, apr_monthly_compound

    
print(apr_daily_compound(10000.0, 200.0, .0423))
print(apr_daily_compound(10000.0, 200.0, .2049))
print(apr_monthly_compound(10000.0, 200.0, .2049))
print(apr_daily_compound_accrue(80000.0, 600, .0423))