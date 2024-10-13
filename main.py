with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        num_ingredients = int(file.readline().strip())
        ingredients = []
        for _ in range(num_ingredients):
            ingredient_info = file.readline().strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_info[0],
            'quantity': int(ingredient_info[1]), 'measure': ingredient_info[2]})
        cook_book[dish] = ingredients
        file.readline()
    print(cook_book)

def get_shop_list_by_dishes(dishes: list, person_count: int):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += (
                        ingredient['quantity'] * person_count)
                else:
                    shop_list[ingredient['ingredient_name']] = (
{'measure': ingredient['measure'],'quantity': (ingredient['quantity'] * person_count)})
        else:
            print('Такого блюда нет в книге')
    print(shop_list)
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)