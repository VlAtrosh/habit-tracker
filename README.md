# Habit Tracker

Простой трекер привычек для командной строки.

## Возможности
- Создание новых привычек
- Отметка выполнения привычек
- Просмотр статистики
- Удаление привычек

## Установка и запуск
```bash
python main.py
```
<img width="376" height="274" alt="Снимок экрана (5)" src="https://github.com/user-attachments/assets/efd85967-2dd6-413f-9b12-4b5a1dc2027c" />

<img width="370" height="253" alt="Снимок экрана (6)" src="https://github.com/user-attachments/assets/3fbbb603-ca75-429b-b7f7-bf4d8edc1426" />


## Структура проекта
```
habit-tracker/
├── .gitignore              # Игнорируемые файлы для Git
├── README.md               # Документация
├── main.py                 # Главный файл приложения
├── models/
│   ├── __init__.py
│   └── habit.py            # Класс Habit
├── storage/
│   ├── __init__.py
│   ├── file_storage.py     # Сохранение/загрузка данных
│   └── exporter.py         # Экспорт/импорт данных
└── utils/
    ├── __init__.py
    └── helpers.py          # Вспомогательные функции
```

## Форматы данных

## JSON (habits.json)

Данные автоматически сохраняются в файл habits.json:
```
[
  {
    "name": "Утренняя зарядка",
    "description": "15 минут упражнений",
    "created_at": "2026-04-13",
    "completions": ["2026-04-13", "2026-04-12"]
  }
]
```

## Экспорт
- JSON: полная копия всех данных

- CSV: таблица с названиями, описаниями и статистикой

## Команды Git
Основные ветки

- master - основная стабильная версия

- feature-storage - работа с хранилищем данных

- feature-ui - пользовательский интерфейс

- feature-export-import - экспорт/импорт данных


