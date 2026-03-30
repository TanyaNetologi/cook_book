def read_file(file_name):

    try:
        file = open(file_name, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()

        clean_lines = []
        for line in lines:
            line = line.strip()
            if line != "":
                clean_lines.append(line)

        return clean_lines

    except:
        print("Ошибка: не могу открыть файл!")
        return []


def create_cook_book(lines):

    cook_book = {}
    i = 0

    while i < len(lines):
        dish_name = lines[i]
        i = i + 1

        if i >= len(lines):
            break

        ingredient_count = int(lines[i])
        i = i + 1

        ingredients = []
        for j in range(ingredient_count):
            if i >= len(lines):
                break
            ingredient_line = lines[i]
            parts = ingredient_line.split("|")

            ingredient_name = parts[0].strip()
            quantity = parts[1].strip()
            measure = parts[2].strip()

            if "." in quantity:
                quantity = float(quantity)
            else:
                quantity = int(quantity)

            ingredient = {
                "ingredient_name": ingredient_name,
                "quantity": quantity,
                "measure": measure,
            }

            ingredients.append(ingredient)
            i = i + 1

        cook_book[dish_name] = ingredients

    return cook_book


def show_all_recipes(cook_book):
    if len(cook_book) == 0:
        print("Нет рецептов!")
        return

    print("\n" + "=" * 40)
    print("ВСЕ РЕЦЕПТЫ")
    print("=" * 40)

    for dish_name in cook_book:
        print("\nDish:", dish_name)
        print("-" * 20)
        print("Ингредиенты:")

        ingredients = cook_book[dish_name]
        for ingredient in ingredients:
            print(
                f"  - {ingredient['ingredient_name']}: "
                f"{ingredient['quantity']} {ingredient['measure']}"
            )


def show_dish_list(cook_book):
    if len(cook_book) == 0:
        print("Нет рецептов!")
        return

    print("\nСПИСОК БЛЮД:")
    print("-" * 30)

    number = 1
    for dish_name in cook_book:
        ingredients_count = len(cook_book[dish_name])
        print(f"{number}. {dish_name} ({ingredients_count} ingredients)")
        number = number + 1


def search_recipe(cook_book):
    search = input("Введите название блюда: ")
    search = search.lower()

    found = False

    for dish_name in cook_book:
        if search in dish_name.lower():
            print(f"\nНайден рецепт: {dish_name}")
            print("-" * 20)

            ingredients = cook_book[dish_name]
            for ingredient in ingredients:
                print(
                    f"  - {ingredient['ingredient_name']}: "
                    f"{ingredient['quantity']} {ingredient['measure']}"
                )

            found = True

    if not found:
        print(f"Блюдо '{search}' не найдено!")


def show_dish_ingredients(cook_book):
    dish_name = input("Введите название блюда: ")

    if dish_name in cook_book:
        print(f"\nRecipe: {dish_name}")
        print("-" * 20)

        ingredients = cook_book[dish_name]
        for ingredient in ingredients:
            print(
                f"  - {ingredient['ingredient_name']}: "
                f"{ingredient['quantity']} {ingredient['measure']}"
            )
    else:
        print(f"Блюдо '{dish_name}' не найдено!")


def show_cook_book(cook_book):
    print("\n" + "=" * 50)
    print("СЛОВАРЬ COOK_BOOK:")
    print("=" * 50)
    print(cook_book)


def make_shopping_list(cook_book):
    user_input = input("Введите название блюд через запятую: ")
    dishes = user_input.split(",")
    clean_dishes = []
    for dish in dishes:
        clean_dishes.append(dish.strip())

    persons = int(input("Введите количество персон: "))

    shopping_list = {}

    for dish in clean_dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]

            for ingredient in ingredients:
                name = ingredient["ingredient_name"]
                quantity = ingredient["quantity"] * persons
                measure = ingredient["measure"]

                if name in shopping_list:
                    shopping_list[name]["quantity"] = (
                        shopping_list[name]["quantity"] + quantity
                    )
                else:
                    shopping_list[name] = {"measure": measure, "quantity": quantity}
        else:
            print(f"Предупреждение: блюдо '{dish}' не найдено!")

    if len(shopping_list) > 0:
        print("\n" + "=" * 50)
        print("СПИСОК ПОКУПОК:")
        print("=" * 50)
        print("{")

        all_items = list(shopping_list.items())

        for i in range(len(all_items)):
            ingredient, details = all_items[i]

            if i < len(all_items) - 1:
                print(
                    f'    "{ingredient}": {{"measure": "{details["measure"]}", '
                    f'"quantity": {details["quantity"]}}},'
                )
            else:
                print(
                    f'    "{ingredient}": {{"measure": "{details["measure"]}", '
                    f'"quantity": {details["quantity"]}}}'
                )

        print("}")
        print("=" * 50)
    else:
        print("Список покупок пуст!")


def main():
    file_name = "recipes.txt"

    print("ЗАГРУЗКА КУЛИНАРНОЙ КНИГИ...")
    lines = read_file(file_name)

    if len(lines) == 0:
        print("Не удалось загрузить рецепты!")

    cook_book = create_cook_book(lines)
    print(f"Загружено {len(cook_book)} рецептов!")

    while True:
        print("\n" + "=" * 40)
        print("КУЛИНАРНАЯ КНИГА")
        print("=" * 40)
        print("1. Все рецепты")
        print("2. Список блюд")
        print("3. Поиск рецепта")
        print("4. Ингредиенты блюда")
        print("5. Показать словарь cook_book")
        print("6. Список покупок")
        print("7. Выход")
        print("-" * 40)

        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            show_all_recipes(cook_book)
        elif choice == "2":
            show_dish_list(cook_book)
        elif choice == "3":
            search_recipe(cook_book)
        elif choice == "4":
            show_dish_ingredients(cook_book)
        elif choice == "5":
            show_cook_book(cook_book)
        elif choice == "6":
            make_shopping_list(cook_book)
        elif choice == "7":
            print("До свиданья!")
            break
        else:
            print("Неверный выбор! Введите 1-7.")


if __name__ == "__main__":
    main()
