CHEESES = ["camembert", "gouda", "cheddar"]

def roll_call_dwarves(names):
    i = 1
    for name in names:
        print(f'{i}. {name}')
        i += 1

def summon_captain_planet(planateer_calls):
    return [f'{call.title()}!' for call in planateer_calls]

def long_planeteer_calls(words):
    
    for word in words:
        if len(word) > 4:
            return True
    
    return False

def find_the_cheese(foods):
    for food in foods:
        if food in CHEESES:
            return food
