import json

# # Задача №1
# # Получение словаря заданного формата


with open('Recipes.txt') as f:
  cook_book = {}
  for line in f:
    dish = line.strip()
    ingridients_number = int(f.readline().strip())
    cook_book[dish] = []
    ingridient_dict = {}
    while ingridients_number:
      ingridient_line = f.readline().strip()
      ingridient = ingridient_line.split(' | ')
      ingridient_dict = {'ingridient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
      cook_book[dish].append(ingridient_dict)
      ingridients_number -= 1
    f.readline()
  print(json.dumps(cook_book, ensure_ascii=False, indent=2))


# Задача №2
# Получение словаря с названиями ингредиентов и их количества для приготовления блюд


def get_shop_list_by_dishes(dishes, person_count):
  grocery_dict = {}
  for dish in dishes:
      if dish in cook_book.keys():
          ingridient_list = cook_book[dish]
          for ingridient in ingridient_list:
              if ingridient['ingridient_name'] not in grocery_dict.keys():
                grocery_dict[ingridient['ingridient_name']] = \
                  {'measure': ingridient['measure'], 'quantity': int(ingridient['quantity']) * int(person_count)}
              else:
                previous_quantity = grocery_dict[ingridient['ingridient_name']].pop('quantity')
                grocery_dict[ingridient['ingridient_name']] = \
                  {'measure': ingridient['measure'], 'quantity': int(ingridient['quantity']) * int(person_count) + previous_quantity}
  return grocery_dict


def main():
  while True:
    dish_user_input = list(input('Введите блюда, которые нужно приготовить: ').split(', '))
    if dish_user_input == ['q']:
      print('До свидания')
      break
    person_user_input = input('Введите количество человек: ')
    if person_user_input == 'q':
      print('До свидания')
      break
    result = get_shop_list_by_dishes(dish_user_input, person_user_input)
    if result == {}:
      print('По вашему запросу ничего не найдено')
    else:
      print(json.dumps(result, ensure_ascii=False, indent=1))


main()