import re

def main():
    while True:
        date_input = input("Date: ").strip()
        
        months = {
            "January": "01", "February": "02", "March": "03",
            "April": "04", "May": "05", "June": "06",
            "July": "07", "August": "08", "September": "09",
            "October": "10", "November": "11", "December": "12"
        }
        
        try:
            # Try numeric format first (MM/DD/YYYY)
            if "/" in date_input:
                month, day, year = date_input.split("/")
                month = month.zfill(2)
                day = day.zfill(2)
            
            # Try text format (Month DD, YYYY)
            else:
                date_input = date_input.replace(",", "")
                parts = date_input.split()
                month_name = parts[0].title()
                
                if month_name not in months:
                    raise ValueError("Invalid month")
                
                month = months[month_name]
                day = parts[1].zfill(2)
                year = parts[2]
            
            # Validate ranges
            if not (1 <= int(month) <= 12):
                raise ValueError("Month out of range")
            if not (1 <= int(day) <= 31):
                raise ValueError("Day out of range")
            
            print(f"{year}-{month}-{day}")
            break
            
        except (ValueError, IndexError):
            # If error, loop continues and asks again
            pass

main()