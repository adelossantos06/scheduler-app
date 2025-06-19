import json
from datetime import datetime, time
from models import Employee, Shift, TimeOff, Schedule

def parse_time(t_str):
    return datetime.strptime(t_str.zfill(5), "%H:%M").time()


def load_employees(path: str) -> list[Employee]:
    with open(path, 'r') as f:
        data = json.load(f)
    employees - []
    for entry in data:
        shifts = []
        for shift_data in entry['default_shifts']:
            shifts.append(
                Shift(
                    day=shift_data['day'],
                    start_time=parse_time(shift_data['start_time']),
                    end_time=parse_time(shift_data['end_time']),
                    responsibility=shift_data['responsibility'],
                    assigned_to=entry['name']
                )
            )
        employees.append(Employee(name=entry['name'], default_shifts=shifts))
    return employees