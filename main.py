import json

count = 0

while True:
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")
    nomer = int(input("Выберете пункт: "))
    with open("city.json", "r", encoding = "utf-8") as file:
        soderjim = file.read()
        text = json.loads(soderjim)
    if nomer == 1:
        count += 1
        for zapis in text:
            print("=" * 20, f"Номер записи: {zapis['id']}", "=" * 20)
            print(f"Название города: {zapis['name']} \nНазвание страны в котором находится город: {zapis['country']} \nЯвляется ли население города больше 100 000 человек: {zapis['is_big']} \nНаселение города: {zapis['people_count']}")
    elif nomer == 2:
        count += 1
        pole = input("Введите поле: ")
        found = False
        for zapis in text:
            if zapis['id'] == pole:
                print("=" * 20, f"Номер записи: {zapis['id']}", "=" * 20,)
                print(f"Название города: {zapis['name']} \nНазвание страны в котором находится город: {zapis['country']} \nЯвляется ли население города больше 100 000 человек: {zapis['is_big']} \nНаселение города: {zapis['people_count']}")
                found = True
                break
        if found == False:
            print("Запись не найдена")
    elif nomer == 3:
        count +=1
        with open("city.json", "w", encoding = "utf-8") as file:
            new = {}
            new['d'] = input("Введите номер записи: ")
            new['name'] = input("Введите название города: ")
            new['country'] = input("Введите  название страны в котором находится город: ")
            new['is_big'] = input("Является ли население города больше 100 000 человек(True/False): ")
            new['people_count'] = input("Введите население города: ")
            text.append(new)
            print("Запись добавлена")
            json.dump(text, file, indent = 5)

    elif nomer == 4:
        count += 1
        nomer = input("Введите поле для удаления: ")
        found = False
        for city in text:
            if nomer == city['id']:
                text.remove(city)
                found = True
                break
        if found:
            with open("city.json", "w", encoding = "utf-8") as file:
                json.dump(text, file, indent = 5)
                print("Запись удалена")
        else:
            print("Запись не найдена")

    elif nomer == 5:
        print(f"{count} выполненных операций")
        break
    else:
        print("Нет такого пункта")
