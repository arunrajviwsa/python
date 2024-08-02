bill_thickness=0.11
tower_height=442
no_of_bill=1
days=1
while(no_of_bill*bill_thickness<tower_height):
    days+=1
    no_of_bill*=2
    print("No of days to reach tower Height",days)
    print("No of days to reach tower Height", no_of_bill*bill_thickness)