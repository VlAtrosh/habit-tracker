from models.habit import Habit
from storage.file_storage import FileStorage
from utils.helpers import clear_screen, print_header, get_user_input

storage = FileStorage()

def show_menu() -> None:
    clear_screen()
    print_header("HABIT TRACKER")
    print("\n1. Все привычки")
    print("2. Добавить привычку")
    print("3. Отметить выполнение")
    print("4. Удалить привычку")
    print("5. Статистика")
    print("0. Выход")

def list_habits() -> None:
    clear_screen()
    print_header("ВСЕ ПРИВЫЧКИ")
    
    if not storage.habits:
        print("\nНет привычек. Добавьте первую!")
    else:
        for habit in storage.habits:
            completions = len(habit.completions)
            streak = habit.get_streak()
            print(f"\n📌 {habit.name}")
            print(f"   Описание: {habit.description or '—'}")
            print(f"   Выполнено: {completions} раз(а)")
            print(f"   Текущая серия: {streak} дней")
    
    input("\nНажмите Enter для продолжения...")

def add_habit() -> None:
    clear_screen()
    print_header("ДОБАВЛЕНИЕ ПРИВЫЧКИ")
    
    name = input("\nНазвание привычки: ").strip()
    if not name:
        print("Название не может быть пустым!")
        input("Нажмите Enter...")
        return
    
    if storage.find_habit(name):
        print("Привычка с таким названием уже существует!")
        input("Нажмите Enter...")
        return
    
    description = input("Описание (необязательно): ").strip()
    habit = Habit(name, description)
    storage.add_habit(habit)
    
    print(f"\n✓ Привычка '{name}' добавлена!")
    input("Нажмите Enter...")

def complete_habit() -> None:
    clear_screen()
    print_header("ОТМЕТКА ВЫПОЛНЕНИЯ")
    
    if not storage.habits:
        print("\nНет привычек. Добавьте сначала привычку!")
        input("Нажмите Enter...")
        return
    
    print("\nДоступные привычки:")
    for i, habit in enumerate(storage.habits, 1):
        print(f"{i}. {habit.name}")
    
    try:
        choice = int(input("\nВыберите номер: ")) - 1
        if 0 <= choice < len(storage.habits):
            habit = storage.habits[choice]
            habit.complete()
            storage.save()
            print(f"\n✓ Отмечено выполнение '{habit.name}'!")
        else:
            print("Неверный номер!")
    except ValueError:
        print("Введите число!")
    
    input("Нажмите Enter...")

def delete_habit() -> None:
    clear_screen()
    print_header("УДАЛЕНИЕ ПРИВЫЧКИ")
    
    if not storage.habits:
        print("\nНет привычек для удаления!")
        input("Нажмите Enter...")
        return
    
    print("\nПривычки:")
    for i, habit in enumerate(storage.habits, 1):
        completions = len(habit.completions)
        print(f"{i}. {habit.name} (выполнено: {completions})")
    
    try:
        choice = int(input("\nВыберите номер для удаления: ")) - 1
        if 0 <= choice < len(storage.habits):
            habit = storage.habits[choice]
            confirm = input(f"Удалить '{habit.name}'? (y/n): ").lower()
            if confirm == 'y':
                storage.remove_habit(habit.name)
                print(f"\n✓ Привычка '{habit.name}' удалена!")
        else:
            print("Неверный номер!")
    except ValueError:
        print("Введите число!")
    
    input("Нажмите Enter...")

def show_statistics() -> None:
    clear_screen()
    print_header("СТАТИСТИКА")
    
    if not storage.habits:
        print("\nНет привычек для отображения статистики.")
    else:
        total_habits = len(storage.habits)
        total_completions = sum(len(h.completions) for h in storage.habits)
        best_streak = max((h.get_streak() for h in storage.habits), default=0)
        best_habit = max(storage.habits, key=lambda h: h.get_streak()) if storage.habits else None
        
        print(f"\n📊 Всего привычек: {total_habits}")
        print(f"✓ Всего выполнений: {total_completions}")
        print(f"🔥 Лучшая серия: {best_streak} дней")
        if best_habit:
            print(f"🏆 Привычка-лидер: {best_habit.name}")
        
        print("\n" + "-" * 40)
        print("Детали по привычкам:")
        for habit in storage.habits:
            completions = len(habit.completions)
            streak = habit.get_streak()
            print(f"\n• {habit.name}")
            print(f"  Выполнено: {completions}, Серия: {streak}")
    
    input("\nНажмите Enter для продолжения...")

def main() -> None:
    actions = {
        '1': list_habits,
        '2': add_habit,
        '3': complete_habit,
        '4': delete_habit,
        '5': show_statistics,
    }
    
    while True:
        show_menu()
        choice = get_user_input("\nВыберите действие: ", ['0', '1', '2', '3', '4', '5'])
        
        if choice == '0':
            print("\nДо свидания! Хорошего дня! 👋")
            break
        
        if choice in actions:
            actions[choice]()
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()