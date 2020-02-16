import pyinputplus as py

PriceList={"Wheat":100,"White":80,"Sourdough":120,"Chicken":200,"Turkey":250,
           "Ham":220,"Tofu":150,"Cheddar":50,"Swiss":60,"Mozzarella":40,
           "Mayo":20,"Mustard":15,"Lettuce":25,"Tomato":15}
Price=0


print("CUSTOMIZE YOUR SANDWICH")
print("")
print("")

print("What Type of Bread do you want?")
Bread = py.inputMenu(["Wheat","White","Sourdough"],numbered=True)
Price+=PriceList[Bread]
print(Price)

print("What Type of Protein do you want?")
Protein = py.inputMenu(["Chicken","Turkey","Ham","Tofu"],numbered=True)
Price+=PriceList[Protein]
print(Price)

CheeseChoice = py.inputYesNo(prompt="Do you want Cheese in your Sandwich\n")

if CheeseChoice == "yes":
    print("What Type of Cheese do you want?")
    Cheese = py.inputMenu(["Cheddar","Swiss","Mozzarella"],numbered=True)
    Price+=PriceList[Cheese]
    #print(Price)
else :
    print("")

Mayo1 = py.inputYesNo(prompt="Do you want Mayo in your Sandwich\n")
Mustard1 = py.inputYesNo(prompt="Do you want Mustard in your Sandwich\n")
Lettuce1 = py.inputYesNo(prompt="Do you want Lettuce in your Sandwich\n")
Tomato1 = py.inputYesNo(prompt="Do you want Tomato in your Sandwich\n")

if Mayo1 == "yes":
    Price+=PriceList["Mayo"]
    #print(Price)
else:
    print("")
    
if Mustard1 == "yes":
    Price+=PriceList["Mustard"]
    #print(Price)
else:
    print("")
    
if Lettuce1 == "yes":
    Price+=PriceList["Lettuce"]
    #print(Price)
else:
    print("")
    
if Tomato1 == "yes":
    Price+=PriceList["Tomato"]
    #print(Price)
else:
    print("")

Number = py.inputInt(prompt="How many of such Sandwiches do you want?\n")

TotalPrice = Price*Number
print("Total Price of your Order is INR" +" "+str(TotalPrice))



   
    
