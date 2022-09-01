import os
from os import system
from re import S
system("clear")

name = input("Whats your name ") 
print("Hello " + name )




chips = ['lays orginal $3.48' , 'Classic Potato Chips Lay $4.78'  , 'Doritos: Cool Ranch $3.00' , 'Tostitos Scoops $5.oo' , 'Sun Chips$3.68' , 'Pringles BBQ$3.94' , 'Lays Chicken and Waffles Chips $5.95' , 'spicy munchies $2.99' , 'takies $2.91' , 'Taco Bell Nacho Cheddar Crisps Bag $11.93 ' ]
drinks = ['2%milk $5.22' , 'rootbeer $4.53' , 'apple juice $6.32' , 'grape juice $5.23' , 'ice tea $6.12' , 'sunkiss $5.25' , 'hawin punch $4.32' , 'orange juice 3.68' , 'water $1.99' , 'kool laid jamemers 5.25' , 'capresuns $2.50']
clothes = ['pantes 10.94' , 'short sleave shirt 21.32 ' , 'long sleave shirt 19.18' , 'jacket 40.54' , 'shortes 14.50' , 'Jeans 12.45' , 'tims 50.21' , 'raincoat 21.43' , 'glasses 10.99' , 'gloves 5.78' , 'socks 2.12']
elctonics = ['pc $1999' , 'Tv $200' , 'phone $200' , 'cellphone $500' , 'speaker $430' , 'alexsa $399' , 'airpods $400' , 'PS4 $300' , 'xbox $300' , 'smart TV $700' , 'fridge $456' , ]
tools = ['shovel $30' , 'pickaxe $40' , 'axe $30' , 'hammer $50' , 'clawhammer $46' , 'skewdriver $12' , 'flat head skewdriver $12' , 'drill $60', 'mower $150' , 'weedeater $300' , 'chain saw $ 350' , 'table saw $123']
planets = ['Spider Plant $10.12' , 'Epipremnum (Devils Ivy) $12.34' , 'Snake Plant - Mother-in-Laws Tongue $11.78' , 'Peace Lily $13.94' , 'Dracaena $14.67' , 'Croton $12.47 ' , 'Chinese Evergreen $13.67' , 'Fern $16.21' , 'Orchid $12.78' ]
candy = ['twix $1.40' , 'SKITTLES $2.43' , 'KIT KAT $1.78' , 'Starburst   $1.67' , 'Dots $2.56' , 'Milk Duds $1.56' , 'AirHeads $1.65' , 'Mike and Ike $1.33' , 'SNICKERS $2.11' , '3 musketeers $2.12' , 'milky way $2.45 ']

print("the sections are: Chips, Drinks, Clothes, Electronics, Tools, Planets, Candy")

usersection = input( "what section would you like ")

if usersection == "chips":
 print(chips) 
elif usersection == "drinks":
 print(drinks) 
elif usersection == "clothes":
 print(clothes)
elif usersection == "elctonics":
 print(elctonics)  
elif usersection == "tools":
 print(tools)  
elif usersection == "planets":
 print(planets)
elif usersection == "candy":
 print(candy)  
  

# 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

