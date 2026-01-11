import json
import time
import os
import platform
from pathlib import Path
from datetime import date

def main():
    try:
        def clear_terminal() -> None:
            cmd = "cls" if platform.system() == "Windows" else "clear"
            os.system(cmd)

        try:
            global file
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
                        "meta": {"created_at": str(date.today()), "last_id" : 0}
                    }
        except json.decoder.JSONDecodeError:
            with file.open("w", encoding="utf-8") as f:
                data = {
                    "cards": [],
                    "diary": [],
                    "meta": {"created_at": str(date.today()), "last_id": 0}
                }
        try:
            global diary_txt
            diary_txt = Path("diary.txt")
            if diary_txt.exists():
                with diary_txt.open("r", encoding="utf-8") as f:
                    global diaryD
                    diaryD = json.load(f)
            else:
                with diary_txt.open("w", encoding="utf-8") as f:
                    diaryD = {
                        "date": [],
                        "text": [],
                    }
        except json.decoder.JSONDecodeError:
            with diary_txt.open("w", encoding="utf-8") as f:
                diaryD = {
                    "date": [],
                    "text": [],
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
        def save():
            with file.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

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
            save()


        def menu_two():
            with file.open("r", encoding="utf-8") as f:
                file_verification = f.read().strip()
                if not file_verification:
                    print("У вас нету карточек...")
                    start_main_menu()
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
            print("Если вы хотите добавить записать нажмите 0: \n"
                  "Если вы хотите просмотреть записи нажмите 1: ")
            number = input("Введите выбор: ")
            if number == "0":
                if os.path.getsize("data.json") == 0:
                    text = input("Вы можете сюда писать что бы добавить пометку: ")
                    last_id = 0
                    new_id = last_id + 1
                    Diary = {
                        "id": new_id,
                        "date": str(date.today()),
                        "text": text
                    }
                    last_diary_id ={
                        "last_diary_id": new_id

                    }


                    data["diary"].append(Diary)
                    data["meta"]["last_diary_id"] = new_id
                    save()
                    print("Успешно сохраненно...")
                    time.sleep(2)
                    clear_terminal()


                elif [] != data["diary"]:
                    text = input("Вы можете сюда писать что бы добавить пометку: ")
                    last_id = data["diary"][-1]["id"]
                    new_id = last_id + 1
                    Diary = {
                        "id": new_id,
                        "date": str(date.today()),
                        "text": text
                    }
                    data["diary"].append(Diary)
                    save()

            elif number == "1":
                if [] == data["diary"]:
                    print("Хей, извините но у вас не записей дневника!")
                    time.sleep(2)
                    clear_terminal()
                    start_main_menu()
                    clear_terminal()


                    text = input("Вы можете сюда писать что бы добавить пометку: ")
                    last_id = 0
                    new_id = last_id + 1
                    Diary = {
                        "id": new_id,
                        "date": str(date.today()),
                        "text": text
                    }
                    data["diary"].append(Diary)
                    save()
                    print("Успешно сохраненно...")
                    time.sleep(2)
                    clear_terminal()
                else:
                    clear_terminal()
                    for i in range(data["meta"]["last_diary_id"]):
                        print(f"Ваш список: {data["diary"][i]["text"]}\n"
                              f"Дата создание: {data["diary"][i]["date"]}")
                    start_main_menu()
                    clear_terminal()
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
                print("Export Diary в разработке...")
                # text = data["diary"][1]["text"]
                # diary_text = {
                #     "texter": text
                #
                # }
                # diary_txt["text"] = diary_text
                # print("test")


            elif menu == "7":
                exit("Вы выбрали выйти из программы")
            else:
                print("Вы ввели некоректное значение...")
                clear_terminal()
    except KeyboardInterrupt:
        clear_terminal()
        print("Exit...")
if __name__ == "__main__":
    main()
else:
    print("Запускайте с main.py")