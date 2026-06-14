from datetime import datetime

def save_history(action):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"[{current_time}] {action}\n")