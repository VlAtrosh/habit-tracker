def clear_screen() -> None:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title: str) -> None:
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)

def get_user_input(prompt: str, valid_options: list = None) -> str:
    while True:
        value = input(prompt).strip()
        if valid_options and value not in valid_options:
            print(f"Ошибка: выберите {', '.join(valid_options)}")
            continue
        return value