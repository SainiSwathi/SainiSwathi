#5. A transport company charges the fare according to following table: 

#Distance     Charges 

#1-50             8 Rs./Km 

#51-100         10 Rs./Km

 #> 100           12 Rs/Km

distance = float(input("Enter the distance in kilometers: "))
if 1<=distance <= 50:
    fare = distance * 8
elif 51<=distance <= 100:
    fare=(50*8)+(distance-50)*10
else:
    fare=(50*8)+(50*10)+(distance-100)*12

print(f"Total fare for {distance} Km is Rs. {fare}")
