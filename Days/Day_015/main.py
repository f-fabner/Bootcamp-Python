from art import logo,options
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def report():
    if not resources:
        return None
    print("Relatório de Recursos:")
    for recurso, quantidade in resources.items():
        print(f"{recurso}: {quantidade} unidades")

def prepare_drink(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def charging():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print()
        print('~*~' * 10)
        print(f"Here is ${change} in change.")
        print('~*~' * 10)
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print()
    print('-"-' * 10)
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    print('-"-' * 10)

def sleeping():
    print('.⏳')
    time.sleep(1)
    print('..⏳')
    time.sleep(1)
    print('...✅')
    time.sleep(1)    
    
def coffee_machine():
    clear()
    print(logo)
    while True:
        option = input(f"What would you like?\n{options}\n").strip().lower()[0]
        clear()
        print(logo)
        if option == 'e' or option =='1':
            option = 'espresso'
            drink = MENU[option]
            if prepare_drink(drink["ingredients"]):
                payment = charging()
                sleeping()
                if transaction(payment, drink["💰Cost"]):
                    sleeping()
                    make_coffee(option, drink["ingredients"])
 
              
        elif option == 'l' or option =='2':
            option = 'latte'
            drink = MENU[option]            
            if prepare_drink(drink["ingredients"]):
                payment = charging()
                sleeping()
                if transaction(payment, drink["💰Cost"]):
                    sleeping()
                    make_coffee(option, drink["ingredients"])
 
            
        elif option == 'c' or option =='3':
            option = 'cappuccino'
            drink = MENU[option]
            if prepare_drink(drink["ingredients"]):
                payment = charging()
                sleeping()
                if transaction(payment, drink["💰Cost"]):
                    sleeping()
                    make_coffee(option, drink["ingredients"])
 
            
        elif option == 'r' or option =='4':
            clear()
            print(logo)
            sleeping()
            report() 
                 
        elif option == 't' or option =='5':
            sleeping()
            print("🛑  Coffee machine turning off!!. 🛑")
            print()
            break

        else:
            clear()
            print(logo)
            print("❌  Invalid option. Try again. ❌")
        print()
        
      

MENU = {
    "espresso": {
        "ingredients": {
            "💧 - Water": 50,
            "🟤 - Coffee": 18,
        },
        "💰Cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "💧 - Water": 200,
            "🥛 - Milk": 150,
            "🟤 - Coffee": 24,
        },
        "💰Cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "💧 - Water": 250,
            "🥛 - Milk": 100,
            "🟤 - Coffee": 24,
        },
        "💰Cost": 3.0,
    }
}
money = 0
resources = {
    "💧 - Water": 300,
    "🥛 - Milk": 200,
    "🟤 - Coffee": 100,
}

coffee_machine()    

#OK To Do: 1. Print Report of all coffe machine resourses
#OK To Do: 2. Check resources sufficient
#OK To Do: 3. Process coins
#OK To Do: 4. Check transaction successful
#OK To Do: 55. Make Coffe