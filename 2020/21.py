def parse_foods(lines):
    ingredient_count = {}
    foods = []
    for line in lines:
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        allergens = allergens.replace(')', '').split(', ')
        foods.append((set(ingredients), set(allergens)))
        for ing in ingredients:            
            ingredient_count[ing] = ingredient_count.get(ing, 0) + 1
    return ingredient_count, foods
    
def possible_matches(foods):
    possible = {}
    for ingredients, allergens in foods:
        for a in allergens:
            if a not in possible:
                possible[a] = ingredients.copy()
            else:
                possible[a] = possible[a].intersection(ingredients)
    return possible

def part1(data):
    lines = [n for n in data.splitlines()]
    ingredient_count, foods = parse_foods(lines)
    possible = possible_matches(foods)
    
    allergen_free = set(ingredient_count.keys())
    for ingredients in possible.values():
        for ingredient in ingredients:
            if ingredient in allergen_free:
                allergen_free.remove(ingredient)
    total = 0
    for free in allergen_free:
        total += ingredient_count[free]
    return total

def part2(data):
    lines = [n for n in data.splitlines()]
    ingredient_count, foods = parse_foods(lines)
    possible = possible_matches(foods)
    confirmed = {}
    while len(confirmed) < len(possible):
        for allergen, ingredients in possible.items():
            if len(ingredients - set(confirmed.values())) == 1:
                ing = min(ingredients - set(confirmed.values()))
                confirmed[allergen] = ing
                break
    return ','.join([confirmed[k] for k in sorted(confirmed.keys())])
