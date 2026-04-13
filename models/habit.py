from datetime import date
from typing import List, Dict

class Habit:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.created_at = date.today()
        self.completions: List[date] = []
    
    def complete(self) -> None:
        today = date.today()
        if today not in self.completions:
            self.completions.append(today)
    
    def get_streak(self) -> int:
        if not self.completions:
            return 0
        
        sorted_dates = sorted(self.completions, reverse=True)
        streak = 1
        expected_date = sorted_dates[0]
        
        for completion in sorted_dates[1:]:
            if (expected_date - completion).days == 1:
                streak += 1
                expected_date = completion
            else:
                break
        return streak
    
    def to_dict(self) -> Dict:
        return {
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'completions': [d.isoformat() for d in self.completions]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Habit':
        habit = cls(data['name'], data['description'])
        habit.created_at = date.fromisoformat(data['created_at'])
        habit.completions = [date.fromisoformat(d) for d in data['completions']]
        return habit