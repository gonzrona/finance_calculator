from datetime import date


month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

class Month:
    def __init__(self, name: str, days: int = 31):
        self.days = days
        self.name = name
        self.short_name = name[0:3] if len(name)>=3 else "NA"
    def __str__(self):
        return "{} ({} days)".format(self.name, self.days)

class Year:
    def __init__(self, value: int = 2023, start: str = "January"):
        self.value = value
        self.leap = True if value%4==0 else False
        self.months = [Month("January"), Month("February", 29 if self.leap else 28), Month("March"), Month("April", 30), Month("May"), Month("June", 30), Month("July"), Month("August"), Month("September", 30), Month("October"), Month("November", 30), Month("December")]
        del self.months[:month_list.index(start)]
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a < len(self.months):
            x = self.a
            self.a += 1
            return self.months[x]
        else:
            raise StopIteration
#    def __str__(self):
#        s = "["
#        for m in self.months:
#            s += "{} {}, ".format(m.short_name,m.days)
#        s = s[:-2]
#        s += "]"
#        return s
    def __str__(self):
        return "{} Leap Year".format(self.value) if self.leap else "{}".format(self.value)


        
def next_month() -> str:
    return month_list[date.today().month%12]


def apr_daily_compound(principal:float, payment:float, apr:float) -> int:
    run = True
    year_count = 0
    payment_count = 0
    if payment < 31*principal*apr/365:
        print("Payment too small to pay off loan")
        return 0
    while run:
        year = Year(date.today().year,next_month()) if year_count==0 else Year(date.today().year + year_count)
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
    
    


#Years = [Year(year) for year in range(2023,2025)]
#Years = [Year(2023,"March"), Year(2024)]
#
#for year in Years:
#    for month in year:
#        print(month)
#    print(" ")
        

print(apr_daily_compound(10000.0, 200.0, .0423))
print(apr_daily_compound(10000.0, 200.0, .2049))
