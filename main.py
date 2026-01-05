import json
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
            "meta": {"created_at": "2026-01-05", "version": "1.0", "last_id" : 0}
        }

print("                        StudyBuddy CLI                  ")
enter = input("                Что бы продолжить нажмите Enter...")
if enter == "":
    pass
print("\n"*50)
print("StudyBuddy CLI\n================\n\n\n")
print("1. Add card - добавить новую фразу (карточку).\n"
      "2. List cards - показать последние N карточек (по умолчанию 10)\n"
      "3. Train - тренировка по карточкам.\n"
      "4. Stats - статистика прогресса.\n"
      "5. Diary - добавить запись / посмотреть записи дневника.\n6. Export diary - экспорт дневника в diary.txt.\n"
      "7. Exit - выход.\n")



while True:


    menu = input("Выберите действие...")

    if menu == "7":

        exit("Вы выбрали выйти из програмы!")

    elif menu == "1":
        front = input("Английская слово: ")
        back = input("Перевод: ")
        last_id = data["meta"]["last_id"]
        new_id = last_id + 1
        card={
            "id": new_id,
            "front": front,
            "back": back
        }

        data["cards"].append(card)
        data["meta"]["last_id"] = new_id
        with file.open("w", encoding="utf-8") as f:
            json.dump(data, f,ensure_ascii=False,indent=2)
    elif menu == "2":
        print("List cards - в разработке\n")

    elif menu == "3":

        print("Train - в разработке\n")

    elif menu == "4":

        print("Stats - в разработке\n")

    elif menu == "5":

        print("Diary - в разработке\n")

    elif menu == "6":

        print("Export diary - в разработке\n")
    else:
        exit()