print("                        StudyBuddy CLI                  ")
enter = input("                Что бы продолжить нажмите Enter...")
if enter == "":
    pass
for _ in range(5):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("StudyBuddy CLI\n================\n\n\n")
print("1. Add card - добавить новую фразу (карточку).\n2. List cards - показать последние N карточек (по умолчанию 10)\n3. Train - тренировка по карточкам.\n4. Stats - статистика прогресса.\n5. Diary - добавить запись / посмотреть записи дневника.\n6. Export diary - экспорт дневника в diary.txt.\n7. Exit - выход.")
while True:
    menu = input("Выберите действие...")
    if menu == "7":
        print("Вы выбрали выйти из програмы!")
        exit()
    elif menu == "1":
        print("Add card - в разработке\n\n\n")
    elif menu == "2":
        print("List cards - в разработке\n\n\n")
    elif menu == "3":
        print("Train - в разработке\n\n\n")
    elif menu == "4":
        print("Stats - в разработке\n\n\n")
    elif menu == "5":
        print("Diary - в разработке\n\n\n")
    elif menu == "6":
        print("Export diary - в разработке\n\n\n")