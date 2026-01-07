import json
import time
import os
import platform
from pathlib import Path
from datetime import date

def main():
    def clear_terminal() -> None:
        cmd = "cls" if platform.system() == "Windows" else "clear"
        os.system(cmd)


    file = Path("data.json")
    if file.exists():
        with file.open("r",encoding="utf-8") as f:
            global data
            data = json.load(f)
    else:
        with file.open("w",encoding="utf-8") as f:
            data = {
                "cards": [],
                "diary": [],
                "meta": {"created_at": str(date.today()), "version": "1.0", "last_id" : 0}
            }


    def start_main_menu():
        print("                        StudyBuddy CLI                  ")
        enter = input("                Что бы продолжить нажмите Enter...")
        if enter == "":
            pass

    start_main_menu()
    clear_terminal()


    def main_menu():
        print("StudyBuddy CLI\n================\n"
              "version 1.0\n================\n"
              "1. Add card - добавить новую фразу (карточку).\n"
              "2. List cards - показать последние N карточек (по умолчанию 10)\n"
              "3. Train - тренировка по карточкам.\n"
              "4. Stats - статистика прогресса.\n"
              "5. Diary - добавить запись / посмотреть записи дневника.\n"
              "6. Export diary - экспорт дневника в diary.txt.\n"
              "7. Exit - выход.\n")
        time.sleep(2.5)
        global menu
        menu = input("Выберите действие...")

    def menu_one():
        front = input("Английская слово: ")
        back = input("Перевод: ")
        source = input("Источник: ")
        print("Операция успешно выполнена...")
        time.sleep(1.5)
        clear_terminal()
        last_id = data["meta"]["last_id"]
        new_id = last_id + 1
        day = date.today()
        card = {
            "id": new_id,
            "front": front,
            "back": back,
            "source": source,
            "added_at": str(day)
        }
        data["cards"].append(card)
        data["meta"]["last_id"] = new_id
        with file.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


    def menu_two():
        with file.open("r", encoding="utf-8") as f:
            file_verification = f.read().strip()
            if not file_verification:
                exit("У вас нету карточек...")
            else:
                for i in range(data["meta"]["last_id"]):
                    print(f"Айди слова: id {data["cards"][i]["id"]}", "\n"
                          f" Английское слово: {data["cards"][i]["front"]}","\n",
                          f"Перевод: {data["cards"][i]["back"]}", "\n",
                          f"Источник: {data["cards"][i]["source"]}", "\n"
                          f"Дата создание: {data["cards"][i]["added_at"]}",
                          "\n===============")
                start_main_menu()
            clear_terminal()
    def menu_five():
        with file.open("r", encoding="utf-8") as f:
            diary_verification = f.read().strip()
            if not diary_verification:
                print(data["diary"])


            else:
                with file.open("r", encoding="utf-8") as f:
                    diary_verification = json.load(f)
                if not diary_verification:
                    print("У вас нету записей...")
                    enter = input("Что бы добавить запись нажмите Enter...")
                    text = input("Вы можете сюда писать что бы добавить пометку: ")
                    Diary = {
                        "date": str(date.today()),
                        "text": text
                    }

                data["diary"].append(Diary)
                with file.open("w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
    def menu_three():
        for i in range(0, data["meta"]["last_id"]):
            print(f"Английское слово: {data["cards"][i]["front"]}")
            translate = input("Введите перевод слова: ")
            if translate == data["cards"][i]["back"]:
                print("Вы ввели правильно...")
            else:
                print("Вы ввели неправильно...")
        time.sleep(2.5)
        clear_terminal()

    while True:
        main_menu()
        clear_terminal()


        if menu == "1":
            menu_one()

        elif menu == "2":
            menu_two()

        elif menu == "3":
             menu_three()

        elif menu == "4":
            print("Stats - в разработке...\n")

        elif menu == "5":
            menu_five()

        elif menu == "6":
            print("Export diary - в разработке...\n")
        elif menu == "7":
            exit("Вы выбрали выйти из программы")
        else:
            print("Вы ввели некоректное значение...")
            clear_terminal()
if __name__ == "__main__":
    main()