#Shippin Cost Calculater 

##Input package weight and shipping rate
weight = float(input("Enter rthe package weight in kilograms:"))
rate = float(input("Enter the shiping rate per kilogram:"))

##Calculate shipping cost
shipping_cost = weight * rate

##Display the result
print(f"Shipping Cost: {shipping_cost} USD")
