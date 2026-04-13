import json
import os
from typing import List, Dict
from models.habit import Habit

DATA_FILE = "habits.json"

class FileStorage:
    def __init__(self):
        self.habits: List[Habit] = []
        self.load()
    
    def load(self) -> None:
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.habits = [Habit.from_dict(h) for h in data]
            except (json.JSONDecodeError, KeyError):
                self.habits = []
    
    def save(self) -> None:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([h.to_dict() for h in self.habits], f, indent=2, ensure_ascii=False)
    
    def add_habit(self, habit: Habit) -> None:
        self.habits.append(habit)
        self.save()
    
    def remove_habit(self, name: str) -> bool:
        for habit in self.habits:
            if habit.name == name:
                self.habits.remove(habit)
                self.save()
                return True
        return False
    
    def find_habit(self, name: str) -> Habit | None:
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None