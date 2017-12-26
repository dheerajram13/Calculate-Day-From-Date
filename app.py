# author : Srirama Dheeraj
# Language: Python
#Project: Calculate Day From Date


date = str(input("Enter/Date as dd/mm/yy: "))
date.split('/')
date_Number = date[0:2]
month_Number = date[3:5]
year_Number = date[6:10]
year_cen = date[6:8]
year_temp = date[8:10]
div = int(year_temp)//4
add_div = int(year_temp)+div
year_code = add_div%7

if month_Number == '01':
    month_code = 0
elif month_Number == '02':
    month_code = 3
elif month_Number == '03':
    month_code = 3
elif month_Number == '04':
    month_code = 6
elif month_Number == '05':
    month_code = 1
elif month_Number == '06':
    month_code = 4
elif month_Number == '07':
    month_code = 6
elif month_Number == '08':
    month_code = 2
elif month_Number == '09':
    month_code = 5
elif month_Number == '10':
    month_code = 0
elif month_Number == '11':
    month_code = 3
elif month_Number == '12':
    month_code = 5

if year_cen == '17':
    century_code = 4
elif year_cen == '18':
    century_code = 2
elif year_cen == '19':
    century_code = 0
elif year_cen == '20':
    century_code = 6
elif year_cen == '21':
    century_code = 4
elif year_cen == '22':
    century_code = 2
elif year_cen == '23':
    century_code = 0

if int(year_Number)%4==0 and int(year_Number%400)==0 or int(year_Number)%100!=0:
    leap_code = 0
else:
    leap_code = 1

#(Year Code + Month Code + Century Code + Date Number – Leap Year Code) mod 7

final = (year_code+month_code+century_code+int(date_Number)-leap_code)%7
if final == 0:
    print("It's Sunday")
elif final == 1:
    print("It's Monday")
elif final == 2:
    print("It's Tuesday")
elif final == 3:
    print("It's Wednesday")
elif final == 4:
    print("It's Thursday")
elif final == 5:
    print("It's Friday")
elif final == 6:
    print("It's Saturday")


