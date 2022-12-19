#Contents
shop = [
{'Code': 'A1',
'Name': 'Pepsi',
'Price': '3 Aed'
},
{'Code': 'B2',
'Name': 'Piatos',
'Price': '5 Aed'
},
{'Code': 'C3',
'Name': 'Aquafina',
'Price': '2 Aed'
},
{'Code': 'D4',
'Name': 'Kitkat',
'Price': '3 Aed'
},
{'Code': 'E5',
'Name': 'Tuna Sandwich',
'Price': '10 Aed'
},
{'Code': 'F6',
'Name': 'CapriSun',
'Price': '3 Aed'
},
{'Code': 'G7',
'Name': 'V-Fresh',
'Price': '1 Aed'
}
]

import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
for list in shop:
    print(f"Code: {list['Code']}|Name: {list['Name']}|Price: {list['Price']}")
#Intro and input of money    
print("Welcome to the vending machine, please insert amount here::")
amount_in = (int(input()))

#Conditions; wrote menu manually since previous attempts included brackets in the terminal
if amount_in >= 1:
  print(
"\nCode: A1----Name: Pepsi----Price: 3 Aed",

"\nCode: B2----Name: Piatos---Price: 5 Aed",

"\nCode: C3----Name: Aquafina---Price: 2 Aed"

"\nCode: D4----Name: Kitkat---Price: 3 Aed",

"\nCode: E5----Name: Tuna Sandwich---Price: 10 Aed"

"\nCode: F6----Name: CapriSun---Price: 3 Aed"

"\nCode: G7----Name: V-Fresh---Price: 1 Aed"

)
  print("Please enter item code to order")
  order_code = input()
else:
  print("Insert valid amount")

#Menu
if order_code == "A1":
  if amount_in >= 3:
    amount_return = amount_in - 3
    print("Dispensing now.. Please claim item and change", amount_return)
  else:
    print("Not enough money!")
if order_code == "B2":
  if amount_in >= 5:
    amount_return = amount_in - 5
    print("Dispensing now.. Please claim item and change", amount_return)
  else:
    print("Not enough money!")
if order_code == "C3":
  if amount_in >= 2:
    amount_return = amount_in - 2
    print("Dispensing now.. Please claim item and change", amount_return)
  else:
    print("Not enough money!")
if order_code == "D4":
  if amount_in >= 3:
    amount_return = amount_in - 3
    print("Dispensing now.. Please claim item and change", amount_return)
  else:
    print("Not enough money!")
if order_code == "E5":
  if amount_in >= 10:
    amount_return = amount_in - 10
    print("Dispensing now.. Please claim item and change", amount_return)
  else:
    print("Not enough money!")
if order_code == "F6":
  if amount_in >= 2:
    amount_return = amount_in - 3
    print("Dispensing now.. Please claim item and change", amount_return)
  else:
    print("Not enough money!")
if order_code == "G7":
  if amount_in >= 2:
    amount_return = amount_in - 1
    print("Dispensing now.. Please claim item and change", amount_return)
  else:
    print("Not enough money!")