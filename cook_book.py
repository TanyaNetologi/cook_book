import os
from typing import Dict, List


def parse_recipe_file(filepath: str) -> Dict[str, List[Dict[str, any]]]:
   
    cook_book = {}

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Файл {filepath} не найден")

    with open(filepath, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        dish_name = lines[i]
        i += 1

        if i >= len(lines):
            break

        try:
            ingredient_count = int(lines[i])
        except ValueError:
            raise ValueError(
                f"Ошибка в формате файла: ожидалось число ингредиентов, получено '{lines[i]}'"
            )
        i += 1
        ingredients = []
        for _ in range(ingredient_count):
            if i >= len(lines):
                raise ValueError(
                    f"Ошибка: недостаточно ингредиентов для блюда '{dish_name}'"
                )

            ingredient_line = lines[i]
            parts = [part.strip() for part in ingredient_line.split("|")]

            if len(parts) != 3:
                raise ValueError(f"Ошибка в формате ингредиента: '{ingredient_line}'")

            ingredient_name, quantity_str, measure = parts

            try:
                if "." in quantity_str:
                    quantity = float(quantity_str)
                else:
                    quantity = int(quantity_str)
            except ValueError:
                quantity = (
                    quantity_str  
                )

            ingredient_dict = {
                "ingredient_name": ingredient_name,
                "quantity": quantity,
                "measure": measure,
            }
            ingredients.append(ingredient_dict)
            i += 1

        cook_book[dish_name] = ingredients

    return cook_book


def display_recipes(cook_book: Dict[str, List[Dict[str, any]]]) -> None:
    
    if not cook_book:
        print("Список рецептов пуст.")
        return

    print("\n" + "=" * 50)
    print("КУЛИНАРНАЯ КНИГА")
    print("=" * 50)

    for dish_name, ingredients in cook_book.items():
        print(f"\n📖 {dish_name}")
        print("-" * 30)
        print(f"Количество ингредиентов: {len(ingredients)}")
        print("\nИнгредиенты:")
        for ingredient in ingredients:
            print(
                f"  • {ingredient['ingredient_name']}: "
                f"{ingredient['quantity']} {ingredient['measure']}"
            )
        print()


def display_cookbook_structure(cook_book: Dict[str, List[Dict[str, any]]]) -> None:
    
    print("\n" + "=" * 50)
    print("СТРУКТУРА СЛОВАРЯ COOK_BOOK:")
    print("=" * 50)
    print("cook_book = {")

    for dish_name, ingredients in cook_book.items():
        print(f'    "{dish_name}": [')
        for ingredient in ingredients:
            print(
                f'        {{"ingredient_name": "{ingredient["ingredient_name"]}", '
                f'"quantity": {ingredient["quantity"]},'
                f'"measure": "{ingredient["measure"]}"}},'
            )
        print("    ],")

    print("}")


def search_recipe(cook_book: Dict[str, List[Dict[str, any]]], search_term: str) -> None:
    
    search_term_lower = search_term.lower()
    found_recipes = {}

    for dish_name, ingredients in cook_book.items():
        if search_term_lower in dish_name.lower():
            found_recipes[dish_name] = ingredients

    if found_recipes:
        print(f"\n🔍 Найдено рецептов по запросу '{search_term}': {len(found_recipes)}")
        display_recipes(found_recipes)
    else:
        print(f"\n❌ Рецепты по запросу '{search_term}' не найдены.")


def get_recipe_ingredients(
    cook_book: Dict[str, List[Dict[str, any]]], dish_name: str
) -> None:
    
    dish_name_lower = dish_name.lower()

    for name, ingredients in cook_book.items():
        if name.lower() == dish_name_lower:
            print(f"\n📖 Рецепт: {name}")
            print("-" * 30)
            print("Ингредиенты:")
            for ingredient in ingredients:
                print(
                    f"  • {ingredient['ingredient_name']}: "
                    f"{ingredient['quantity']} {ingredient['measure']}"
                )
            return

    matching_recipes = [
        name for name in cook_book.keys() if dish_name_lower in name.lower()
    ]

    if matching_recipes:
        print(f"\n🔍 Блюдо '{dish_name}' точно не найдено. Возможно, вы имели в виду:")
        for recipe in matching_recipes:
            print(f"  • {recipe}")
        print("\nВведите точное название блюда для просмотра ингредиентов.")
    else:
        print(f"\n❌ Блюдо '{dish_name}' не найдено в кулинарной книге.")


def list_all_dishes(cook_book: Dict[str, List[Dict[str, any]]]) -> None:
    
    if not cook_book:
        print("Список рецептов пуст.")
        return

    print("\n📋 СПИСОК ВСЕХ БЛЮД:")
    print("-" * 30)
    for i, dish_name in enumerate(cook_book.keys(), 1):
        ingredient_count = len(cook_book[dish_name])
        print(f"{i:2d}. {dish_name} ({ingredient_count} ингр.)")


def get_shop_list_by_dishes(
    dishes: List[str],
    person_count: int,
    cook_book: Dict[str, List[Dict[str, Union[str, int, float]]]],
) -> Dict[str, Dict[str, Union[str, int, float]]]:
    
    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            print(
                f"⚠️ Предупреждение: Блюдо '{dish}' не найдено в кулинарной книге и будет пропущено."
            )
            continue

        ingredients = cook_book[dish]

        for ingredient in ingredients:
            ingredient_name = ingredient["ingredient_name"]
            quantity = ingredient["quantity"] * person_count
            measure = ingredient["measure"]

            if ingredient_name in shop_list:
                shop_list[ingredient_name]["quantity"] += quantity
            else:
                shop_list[ingredient_name] = {"measure": measure, "quantity": quantity}

    return shop_list


def display_shop_list(shop_list: Dict[str, Dict[str, Union[str, int, float]]]) -> None:
    
    if not shop_list:
        print("Список покупок пуст.")
        return

    print("\n" + "=" * 50)
    print("СПИСОК ПОКУПОК")
    print("=" * 50)

    print("{")
    for ingredient, details in shop_list.items():
        print(
            f'    "{ingredient}": {{"measure": "{details["measure"]}", "quantity": {details["quantity"]}}},'
        )
    print("}")
    print("=" * 50)

def main_example():

    cook_book = {
        "Омлет": [
            {"ingredient_name": "Яйцо", "quantity": 2, "measure": "шт"},
            {"ingredient_name": "Молоко", "quantity": 100, "measure": "мл"},
            {"ingredient_name": "Помидор", "quantity": 2, "measure": "шт"},
        ],
        "Запеченный картофель": [
            {"ingredient_name": "Картофель", "quantity": 1, "measure": "кг"},
            {"ingredient_name": "Чеснок", "quantity": 3, "measure": "зуб"},
            {"ingredient_name": "Сыр гуада", "quantity": 100, "measure": "г"},
        ],
    }

    dishes = ["Запеченный картофель", "Омлет"]
    person_count = 2

    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)

    print(f"\n📝 Список покупок для блюд: {dishes}")
    print(f"👥 Количество персон: {person_count}")
    display_shop_list(shop_list)

    print("\n" + "=" * 50)
    print("СЛОВАРЬ В ФОРМАТЕ ЗАДАНИЯ:")
    print("=" * 50)
    print(shop_list)


if __name__ == "__main__":
    main_example()


def main():
    filepath = "recipes.txt"
    try:
        cook_book = parse_recipe_file(filepath)
        print(f"✅ Успешно загружено {len(cook_book)} рецептов из файла '{filepath}'")

        display_cookbook_structure(cook_book)

        while True:
            print("\n" + "=" * 40)
            print("КУЛИНАРНАЯ КНИГА - МЕНЮ")
            print("=" * 40)
            print("1. Показать все рецепты")
            print("2. Показать список блюд")
            print("3. Поиск рецепта по названию")
            print("4. Показать ингредиенты блюда")
            print("5. Показать структуру словаря cook_book")
            print("6. Сформировать список покупок")
            print("7. Выход")
            print("-" * 40)

            choice = input("Выберите действие (1-6): ").strip()

            if choice == "1":
                display_recipes(cook_book)
            elif choice == "2":
                list_all_dishes(cook_book)
            elif choice == "3":
                search_term = input("Введите название блюда для поиска: ").strip()
                if search_term:
                    search_recipe(cook_book, search_term)
                else:
                    print("❌ Поисковый запрос не может быть пустым.")
            elif choice == "4":
                dish_name = input("Введите название блюда: ").strip()
                if dish_name:
                    get_recipe_ingredients(cook_book, dish_name)
                else:
                    print("❌ Название блюда не может быть пустым.")
            elif choice == "5":
                display_cookbook_structure(cook_book)
            elif choice == "6":
                dishes_input = input("Введите названия блюд через запятую: ").strip()
                dishes = [dish.strip() for dish in dishes_input.split(",")]
                person_count = int(input("Введите количество персон: "))
                shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
                display_shop_list(shop_list)
            elif choice == "7":
                print("👋 До свидания!")
                break
            else:
                print("❌ Неверный выбор. Пожалуйста, выберите 1-6.")

    except FileNotFoundError as e:
        print(f"❌ Ошибка: {e}")
        print(f"Создайте файл '{filepath}' в той же папке, что и программа.")
    except ValueError as e:
        print(f"❌ Ошибка при чтении файла: {e}")
    except Exception as e:
        print(f"❌ Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
