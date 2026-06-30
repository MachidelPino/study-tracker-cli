import json
from pathlib import Path

DATA_FILE = Path("data/study_data.json")

def get_empty_data():
    data: json = {
            "subjects": {},
            "sessions": [],
            "tasks": [],
            "next_session_id": 1,
            "next_task_id": 1
        }
    return data


def load_data(path=DATA_FILE):
    path = Path(path)

    if not path.exists():
        return get_empty_data
    
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data, path=DATA_FILE):
    path = Path(path)

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)