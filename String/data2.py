def format_date(day, month, year):
    day_format = f"{day:02d}"
    month_format = f"{month:02d}"
    
    return f"{day_format}/{month_format}/{year}";


print(format_date(21, 7, 2010))   