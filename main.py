import json
import time
from pathlib import Path

file = Path("data.json")
if file.exists():
    with file.open("r") as f:
        data = json.load(f)
else:
    with file.open("w") as f:
        data = {
            "cards": [],
            "diary": [],
            "meta": {"created_at": "2026-01-05", "version": "1.0", "last_id" : 0,}
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
          "5. Diary - добавить запись / посмотреть записи дневника.\n6. Export diary - экспорт дневника в diary.txt.\n"
          "7. Exit - выход.\n"
          "8. Clear data.json - Очистить data.json"                 )
def print_n():
    print("\n"*35)
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
        card= {
            "id": new_id,
            "front": front,
            "back": back,
            "source": source
        }
        data["cards"].append(card)
        data["meta"]["last_id"] = new_id
        with file.open("w", encoding="utf-8") as f:
            json.dump(data, f,ensure_ascii=False,indent=2)
    elif menu == "2":
        print("List cards - в разработке...\n")
    elif menu == "3":
        print("Train - в разработке...\n")
    elif menu == "4":
        print("Stats - в разработке...\n")
    elif menu == "5":
        print("Diary - в разработке...\n")
    elif menu == "6":
        print("Export diary - в разработке...\n")
    elif menu == "8":
        file.unlink()
        exit("Удаление успешно прошло...\nВыход из програмы")
    else:
        exit("Попробуйте еще раз запустить програму...")