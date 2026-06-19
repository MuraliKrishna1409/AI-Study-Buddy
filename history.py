from datetime import datetime

HISTORY_FILE = "history.txt"


def save_history(action):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {action}\n")


def read_history():

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return file.readlines()

    except FileNotFoundError:
        return []


def clear_history():

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        file.write("")