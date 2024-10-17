class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
def extract_date_data(date: str):
    part = date.split('/')
    day = int(part[0])
    month = int(part[1])
    year = int(part[2])
    
    return Data(day, month, year)

obj = extract_date_data('21/07/2010')
print(f'Day: ', obj.day)
print(f'Month: ', obj.month)
print(f'Year: ', obj.year)