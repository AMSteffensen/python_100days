MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 200,
    "money": 50
}

isMachineOff = False


# TODO: 2. Check if resources are sufficient to make drink order
# When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
def checkResources(drink):
    canMakeDrink = False
    water_cost = MENU[drink]['ingredients']['water']
    water_left = resources['water']
    milk_cost = MENU[drink]['ingredients']['milk']
    milk_left = resources['milk']
    coffee_cost = MENU[drink]['ingredients']['coffee']
    coffee_left = resources['coffee']
    drink_cost = MENU[drink]['cost']

    if drink == 'espresso':
        if water_cost < water_left and coffee_cost < coffee_left:
            print('Espresso can be made')
            canMakeDrink = True
        elif water_cost > water_left:
            print('There is not enough water left')
        elif coffee_cost > coffee_left:
            print('There is not coffee left')
    elif drink == 'latte':
        if water_cost < water_left and coffee_cost < coffee_left and milk_cost < milk_left:
            print('Latte can be made')
            canMakeDrink = True
        elif water_cost > water_left:
            print('There is not enough water left')
        elif coffee_cost > coffee_left:
            print('There is not enough coffee left')
        elif milk_cost > milk_left:
            print('There is not enough milk left')
    elif drink == 'cappuccino':
        if water_cost < water_left and coffee_cost < coffee_left and milk_cost < milk_left:
            print('Cappuccino can be made')
            canMakeDrink = True
        elif water_cost > water_left:
            print('There is not enough water left')
        elif coffee_cost > coffee_left:
            print('There is not enough coffee left')
        elif milk_cost > milk_left:
            print('There is not enough milk left')
    else:
        print('there is not enough resources left.')
        print(f'Water left: {water_left}, Milk left: {milk_left}, Coffee left: {coffee_left}')
    return canMakeDrink

def insertCoins(drink):
    print('Please insert coins')
    number_of_quarters = float(input('How many quarters?'))
    number_of_dimes = float(input('How many dimes?'))
    number_of_nickles = float(input('How many nickles?'))
    number_of_pennies = float(input('How many pennies?'))

    quarters = 0.25 * number_of_quarters
    dimes = 0.1 * number_of_dimes
    nickles = 0.05 * number_of_nickles
    pennies = 0.01 * number_of_pennies
    result = quarters + dimes + pennies + nickles

    drink_cost = MENU[drink]['cost']
    profit = drink_cost
    money_left = resources['money']
    if result < drink_cost:
        print('Sorry thats not enough money. Money refunded.')
    elif result > money_left:
        print('Sorry thats not enough money for a change. Money refunded.')
    elif result > drink_cost:
        change = result - drink_cost
        profit = result - change
        resources['money'] += profit
        print(f"Here is ${round(change, 2)} in change. {profit}")
    else:
        print('Making coffee...')
        resources['money'] += profit

def makeCoffee(drink):
    water_cost = MENU[drink]['ingredients']['water']
    coffee_cost = MENU[drink]['ingredients']['coffee']
    milk_cost = MENU[drink]['ingredients']['milk']
    print(f"Here is your {drink}. Enjoy!")

while not isMachineOff:
    espresso_resources = MENU['espresso']
    latte_resources = MENU['latte']
    cappuccino_resources = MENU['cappuccino']

    # TODO: 3. Prompt user for what Coffee they like
    answer = input(f'What would you like? (espresso/latte/cappuccino):')
    # TODO: 4. Add off switch
    if answer == 'off':
        break
    else:
        if answer == 'latte':
            print('user selected latte')
            if checkResources('latte'):
                insertCoins('latte')
                makeCoffee('latte')
        elif answer == 'espresso':
            print('user selected espresso')
            if checkResources('espresso'):
                insertCoins('espresso')
                makeCoffee('espresso')
        elif answer == 'cappuccino':
            print('user selected cappuccino')
            if checkResources('cappuccino'):
                insertCoins('cappuccino')
                makeCoffee('cappuccino')
        elif answer == 'report':
            print(f"Water: {resources['water']}")
            print(f"Milk: {resources['milk']}")
            print(f"Coffe: {resources['coffee']}")
            print(f"Money: {resources['money']}")



