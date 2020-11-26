def coffee_bot():
    print("Welcome to the cafe!")
    size = get_size()
    drink_type = get_drink_type()
    print(f"Alright, that's a {size} {drink_type}")
    name = input("Can I get your name please?")
    print(f"Thanks, {name}! Your drink will be ready shortly")

def get_size():
    response = input("What size drink would you like today? \n[a] Small \n[b] Medium \n[c] Large \n>")

    if response == "a":
        return "small"
    elif response == "b":
        return "medium"
    elif response == "c":
        return "large"
    else:
        print_message()
        return get_size()

def get_drink_type():
    response = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>")
    
    if response == "a":
        return "Brewed Coffee"
    elif response == "b":
        return "Mocha"
    elif response == "c":
        return order_latte()
    else:
        print_message()
        return get_drink_type()

def order_latte():
    response = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>")

    if response == "a":
        return "regular latte"
    elif response == "b":
        return "non-fat latte"
    elif response == "c":
        return "soy latte"
    else:
        print_message()
        return order_latte()

def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

coffee_bot()

