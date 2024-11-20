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
        text = json.load(file)
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
        if not found:
            print("Запись не найдена")
    elif nomer == 3:
        count += 1
        new = {}
        new['id'] = str(max(int(city['id']) for city in text) + 1 if text else 1)
        new['name'] = input("Введите название города: ")
        new['country'] = input("Введите название страны: ")
            
        while True:
            people_count = input("Введите население города: ")
            if people_count.isdigit():
                new['people_count'] = int(people_count)
                break
            else:
                print("Ошибка: население города должно быть числом.")
                    
        new['is_big'] = (True if new['people_count'] > 100000 else False)
        text.append(new)
            
        with open("city.json", "w", encoding="utf-8") as file:
            json.dump(text, file, indent=5)
                
        print("Запись добавлена")
        

    elif nomer == 4:
        count += 1
        pole = input("Введите поле для удаления: ")
        found = False
        for city in text:
            if city['id'] == pole:
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
