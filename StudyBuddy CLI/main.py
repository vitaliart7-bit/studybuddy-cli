import json
import time
from pathlib import Path
from datetime import date
file = Path("data.json")
if file.exists():
    with file.open("r",encoding="utf-8") as f:
        data = json.load(f)
else:
    with file.open("w",encoding="utf-8") as f:
        data = {
            "cards": [],
            "diary": [],
            "meta": {"created_at": str(date.today()), "version": "1.0", "last_id" : 0,}
        }
def Start_main_menu():
    print("                        StudyBuddy CLI                  ")
    enter = input("                Что бы продолжить нажмите Enter...")
    if enter == "":
        pass
Start_main_menu()
def Main_menu():
    print("StudyBuddy CLI\n================\n"
          "version 1.0\n================\n"
          "1. Add card - добавить новую фразу (карточку).\n"
          "2. List cards - показать последние N карточек (по умолчанию 10)\n"
          "3. Train - тренировка по карточкам.\n"
          "4. Stats - статистика прогресса.\n"
          "5. Diary - добавить запись / посмотреть записи дневника.\n"
          "6. Export diary - экспорт дневника в diary.txt.\n"
          "7. Exit - выход.\n"
          "8. Clear data.json - Очистить data.json"                 )
def print_n():
    print("\n"*50)
while True:
    Main_menu()
    time.sleep(2.5)
    menu = input("Выберите действие...")
    print_n()
    if menu == "1":
        front = input("Английская слово: ")
        back = input("Перевод: ")
        source = input("Источник: ")
        print("Операция успешно выполнена...")
        time.sleep(1.5)
        print_n()
        last_id = data["meta"]["last_id"]
        new_id = last_id + 1
        day = date.today()

        time.sleep(4)
        card= {
            "id": new_id,
            "front": front,
            "back": back,
            "source": source,
            "added_at": str(day)
        }
        data["cards"].append(card)
        data["meta"]["last_id"] = new_id
        with file.open("w", encoding="utf-8") as f:
            json.dump(data, f,ensure_ascii=False,indent=2)
    elif menu == "2":
        with file.open("r", encoding="utf-8") as f:
            file_verification = f.read().strip()
            if not file_verification:
                exit("У вас нету карточек...")
            else:
                with file.open("r",encoding="utf-8") as f:
                    verification = json.load(f)
                    for i in range(verification["meta"]["last_id"]):
                        print(f"Айди слова: id {verification["cards"][i]["id"]}","\n"
                              f" Английское слово: {verification["cards"][i]["front"]}","\n",
                              f"Перевод: {verification["cards"][i]["back"]}","\n",
                              f"Источник: {verification["cards"][i]["source"]}","\n==============="
                              f"{verification["cards"][i]["added_at"]}")
                    Start_main_menu()
                    print_n()
    elif menu == "3":
        print("Train - в разработке...\n")
    elif menu == "4":
        print("Stats - в разработке...\n")
    elif menu == "5":
        with file.open("r", encoding="utf-8") as f:
            diary_verification = f.read().strip()
            if not diary_verification:
                print(data["diary"])
                with file.open("w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)


            else:
                with file.open("r",encoding="utf-8") as f:
                    diary_verification = json.load(f)

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
    elif menu == "6":
        print("Export diary - в разработке...\n")
    elif menu == "8":
        file.unlink()
        exit("Удаление успешно прошло...\nВыход из програмы")
    else:
        exit("Попробуйте еще раз запустить програму...")