imena_faylov = ["1.txt", "2.txt", "3.txt"]

rezultat = "result.txt"

print("=== НАЧИНАЕМ ОБЪЕДИНЕНИЕ ФАЙЛОВ ===")
print(f"Найдено файлов: {len(imena_faylov)}")
print(f"Список файлов: {imena_faylov}")
print()

info_o_faylah = []

for imya in imena_faylov:
    try:
        fayl = open(imya, "r", encoding="utf-8")

        kolichestvo_strok = 0
        for stroka in fayl:
            kolichestvo_strok = kolichestvo_strok + 1

        fayl.close()
        info_o_faylah.append([imya, kolichestvo_strok])
        print(f"✓ Файл {imya} содержит {kolichestvo_strok} строк(и)")

    except FileNotFoundError:
        print(f"✗ ОШИБКА: Файл {imya} не найден!")
        print(f"  Убедитесь, что файл {imya} находится в той же папке.")

print()
print(f"Обработано файлов: {len(info_o_faylah)}")
print()

for i in range(len(info_o_faylah)):
    for j in range(len(info_o_faylah) - 1 - i):
        if info_o_faylah[j][1] > info_o_faylah[j + 1][1]:
            vrem_hranenie = info_o_faylah[j]
            info_o_faylah[j] = info_o_faylah[j + 1]
            info_o_faylah[j + 1] = vrem_hranenie

print("Файлы после сортировки (от меньшего к большему):")
for imya, kolvo in info_o_faylah:
    print(f"  {imya} - {kolvo} строк(и)")
print()

vihodnoi_fayl = open(rezultat, "w", encoding="utf-8")
zapicano_faylov = 0

for imya_fayla, kolichestvo_strok in info_o_faylah:
    vihodnoi_fayl.write(imya_fayla + "\n")
    vihodnoi_fayl.write(str(kolichestvo_strok) + "\n")
    ishodnii_fayl = open(imya_fayla, "r", encoding="utf-8")

    for stroka in ishodnii_fayl:
        vihodnoi_fayl.write(stroka)

    ishodnii_fayl.close()

    zapicano_faylov = zapicano_faylov + 1
    print(
        f"✓ Файл {imya_fayla} добавлен в результат "
        f"(записано {zapicano_faylov} из {len(info_o_faylah)})"
    )
vihodnoi_fayl.close()

print()
print("=== ГОТОВО! ===")
print(f"Все {zapicano_faylov} файлов объединены в {rezultat}")

print()
print("--- СОДЕРЖИМОЕ ИТОГОВОГО ФАЙЛА ---")

try:
    fayl_rezultat = open(rezultat, "r", encoding="utf-8")
    nomer_stroki = 1
    for stroka in fayl_rezultat:
        print(f"{nomer_stroki:2}. {stroka}", end="")
        nomer_stroki = nomer_stroki + 1
    fayl_rezultat.close()
except FileNotFoundError:
    print(f"Файл {rezultat} не создан, возможно произошла ошибка.")
