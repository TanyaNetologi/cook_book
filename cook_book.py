def chitat_file(imya_faila):
    try:
        file = open(imya_faila, "r", encoding="utf-8")
        stroki = file.readlines()
        file.close()
        chistye_stroki = []
        for s in stroki:
            s = s.strip()
            if s != "":
                chistye_stroki.append(s)
        return chistye_stroki
    except:
        print("Не могу открыть файл!")
        return []


def sozdat_cook_book(stroki):
    cook_book = {}
    i = 0

    while i < len(stroki):
        nazvanie = stroki[i]
        i = i + 1
        if i >= len(stroki):
            break
        kol_vo = int(stroki[i])
        i = i + 1
        ingredienti = []
        for j in range(kol_vo):
            if i >= len(stroki):
                break

            stroka = stroki[i]
            chast = stroka.split("|")

            nazv_ing = chast[0].strip()
            kol = chast[1].strip()
            edinica = chast[2].strip()

            if "." in kol:
                kol = float(kol)
            else:
                kol = int(kol)

            ing = {"ingredient_name": nazv_ing, "quantity": kol, "measure": edinica}
            ingredienti.append(ing)
            i = i + 1

        cook_book[nazvanie] = ingredienti

    return cook_book


def pokazat_vse_recepty(cook_book):
    if len(cook_book) == 0:
        print("Нет рецептов!")
        return

    print("\n" + "=" * 40)
    print("ВСЕ РЕЦЕПТЫ")
    print("=" * 40)

    for nazvanie in cook_book:
        print("\nБлюдо:", nazvanie)
        print("-" * 20)

        ingredienti = cook_book[nazvanie]
        print("Ингредиенты:")
        for ing in ingredienti:
            print(f"  - {ing['ingredient_name']}: {ing['quantity']} {ing['measure']}")


def pokazat_spisok_blud(cook_book):
    if len(cook_book) == 0:
        print("Нет рецептов!")
        return

    print("\nСПИСОК БЛЮД:")
    print("-" * 30)

    nomer = 1
    for nazvanie in cook_book:
        kol_ing = len(cook_book[nazvanie])
        print(f"{nomer}. {nazvanie} ({kol_ing} ингр.)")
        nomer = nomer + 1


def poisk_recepta(cook_book):
    zapros = input("Введите название блюда: ")
    zapros = zapros.lower()

    naideno = False
    for nazvanie in cook_book:
        if zapros in nazvanie.lower():
            print(f"\nНайден рецепт: {nazvanie}")
            print("-" * 20)
            ingredienti = cook_book[nazvanie]
            for ing in ingredienti:
                print(
                    f"  - {ing['ingredient_name']}: {ing['quantity']} {ing['measure']}"
                )
            naideno = True

    if not naideno:
        print(f"Блюдо '{zapros}' не найдено!")


def pokazat_ingredienty_bluda(cook_book):
    nazvanie = input("Введите название блюда: ")

    if nazvanie in cook_book:
        print(f"\nРецепт: {nazvanie}")
        print("-" * 20)
        ingredienti = cook_book[nazvanie]
        for ing in ingredienti:
            print(f"  - {ing['ingredient_name']}: {ing['quantity']} {ing['measure']}")
    else:
        print(f"Блюдо '{nazvanie}' не найдено!")


def pokazat_slovar(cook_book):
    print("\n" + "=" * 50)
    print("СЛОВАРЬ COOK_BOOK:")
    print("=" * 50)
    print(cook_book)


def sdelat_spisok_pokupok(cook_book):
    vvod = input("Введите названия блюд через запятую: ")
    bluda = vvod.split(",")

    # Убираем лишние пробелы
    bluda_chistye = []
    for b in bluda:
        bluda_chistye.append(b.strip())

    kol_person = int(input("Введите количество персон: "))

    spisok = {}

    for bludo in bluda_chistye:
        if bludo in cook_book:
            ingredienti = cook_book[bludo]
            for ing in ingredienti:
                nazv = ing["ingredient_name"]
                kol = ing["quantity"] * kol_person
                ed = ing["measure"]

                if nazv in spisok:
                    spisok[nazv]["quantity"] = spisok[nazv]["quantity"] + kol
                else:
                    spisok[nazv] = {"measure": ed, "quantity": kol}
        else:
            print(f"Предупреждение: блюдо '{bludo}' не найдено!")

    if len(spisok) > 0:
        print("\n" + "=" * 50)
        print("СПИСОК ПОКУПОК:")
        print("=" * 50)
        print("{")

        vse_ing = list(spisok.items())
        for i in range(len(vse_ing)):
            ing, detal = vse_ing[i]
            if i < len(vse_ing) - 1:
                print(
                    f'    "{ing}": {{"measure": "{detal["measure"]}", "quantity": {detal["quantity"]}}},'
                )
            else:
                print(
                    f'    "{ing}": {{"measure": "{detal["measure"]}", "quantity": {detal["quantity"]}}}'
                )

        print("}")
        print("=" * 50)
    else:
        print("Список покупок пуст!")


def main():
    imya_faila = "recipes.txt"

    print("ЗАГРУЗКА КУЛИНАРНОЙ КНИГИ...")
    stroki = chitat_file(imya_faila)

    if len(stroki) == 0:
        print("Не удалось загрузить рецепты!")
        return

    cook_book = sozdat_cook_book(stroki)
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

        vibor = input("Выберите действие (1-7): ")

        if vibor == "1":
            pokazat_vse_recepty(cook_book)
        elif vibor == "2":
            pokazat_spisok_blud(cook_book)
        elif vibor == "3":
            poisk_recepta(cook_book)
        elif vibor == "4":
            pokazat_ingredienty_bluda(cook_book)
        elif vibor == "5":
            pokazat_slovar(cook_book)
        elif vibor == "6":
            sdelat_spisok_pokupok(cook_book)
        elif vibor == "7":
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Введите 1-7")


if __name__ == "__main__":
    main()
