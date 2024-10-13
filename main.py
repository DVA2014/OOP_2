with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        num_ingredients = int(file.readline().strip())
        ingredients = []
        for _ in range(num_ingredients):
            ingredient_info = file.readline().strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_info[0],
            'quantity': ingredient_info[1], 'measure': ingredient_info[2]})
        cook_book[dish] = ingredients
        file.readline()
    print(cook_book)