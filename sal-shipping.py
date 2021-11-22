weight =  8.4
#Groung shipping
if weight <= 2:
  cost = weight*1.5 + 20
elif weight > 2 and weight <= 6:
  cost = weight*3 + 20
elif weight > 6 and weight <= 10:
  cost = weight*4 + 20
else:
  cost = weight*4.75 + 20

#groung Shipping Premium
ground_premium_cost = 125.00
print("Ground shipping premium cost is: " + " $ " + str(ground_premium_cost))

#Drone Shipping
weight = 1.5
if weight <= 2:
  cost = weight*4.5 + 0.00
elif weight > 2 and weight <= 6:
  cost = weight*9 + 0.00
elif weight > 6 and weight <= 10:
  cost = weight*12 +0.00
else:
  cost = weight*14.25 + 0.00
print(cost)