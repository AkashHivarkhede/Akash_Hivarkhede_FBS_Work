# Convert distant given in feet and inches into meter and centimeter.   

feet = float(input('Enter distance in feet : '))
inch = float(input('Enter distance in inches :'))

cm_feet = feet * 30.48

cm_inch = inch * 2.54

total_cm = cm_feet + cm_inch

meter = total_cm / 100 

print(f'Distance in meters : {meter}')
print(f'Distance in centemeters : {total_cm}')