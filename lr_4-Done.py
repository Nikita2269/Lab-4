import itertools

# Данные предметов
items = [
    {"name": "rifle", "abbr": "r", "size": 3, "survival_points": 25},
    {"name": "pistol", "abbr": "p", "size": 2, "survival_points": 15},
    {"name": "ammo", "abbr": "a", "size": 2, "survival_points": 15},
    {"name": "medkit", "abbr": "m", "size": 2, "survival_points": 20},
    {"name": "inhaler", "abbr": "i", "size": 1, "survival_points": 5},
    {"name": "knife", "abbr": "k", "size": 1, "survival_points": 15},
    {"name": "axe", "abbr": "x", "size": 3, "survival_points": 20},
    {"name": "talisman", "abbr": "t", "size": 1, "survival_points": 25},
    {"name": "flask", "abbr": "f", "size": 1, "survival_points": 15},
    {"name": "antidot", "abbr": "d", "size": 1, "survival_points": 10},
    {"name": "supplies", "abbr": "s", "size": 2, "survival_points": 20},
    {"name": "crossbow", "abbr": "c", "size": 2, "survival_points": 20}
]

# Входные данные
backpack_size = 8  # Размер рюкзака (в ячейках)
disease = "infection"  # Болезнь (заражение)
initial_points = 10  # Начальные очки выживания

# Учитываем обязательный предмет
mandatory_items = []
if disease == "infection":
    mandatory_items.append(next(item for item in items if item["name"] == "antidot"))
elif disease == "asthma":
    mandatory_items.append(next(item for item in items if item["name"] == "inhaler"))

# Размер и очки для обязательных предметов
mandatory_size = sum(item["size"] for item in mandatory_items)
mandatory_points = sum(item["survival_points"] for item in mandatory_items)

# Проверяем, что места достаточно
if mandatory_size > backpack_size:
    print("Невозможно уместить обязательные предметы в рюкзак.")
    exit()

# Доступное место после обязательных предметов
remaining_size = backpack_size - mandatory_size

# Оптимизация набора предметов
best_combination = None
max_points = float('-inf')

# Все комбинации предметов, которые помещаются в оставшееся место
optional_items = [item for item in items if item not in mandatory_items]
for r in range(len(optional_items) + 1):
    for combination in itertools.combinations(optional_items, r):
        total_size = sum(item["size"] for item in combination)
        total_points = sum(item["survival_points"] for item in combination)

        # Учитываем штраф за отсутствие предметов
        missing_items = [item for item in optional_items if item not in combination]
        penalty_points = sum(-item["survival_points"] for item in missing_items)

        if total_size <= remaining_size:
            final_points = initial_points + mandatory_points + total_points + penalty_points
            if final_points > max_points:
                max_points = final_points
                best_combination = mandatory_items + list(combination)

# Формирование двумерного инвентаря
inventory = []
current_row = []
for item in best_combination:
    for _ in range(item["size"]):
        if len(current_row) == 4:
            inventory.append(current_row)
            current_row = []
        current_row.append(f"[{item['abbr']}]")
if current_row:
    inventory.append(current_row)

# Вывод результатов
for row in inventory:
    print(",".join(row))
print(f"\nИтоговые очки выживания: {max_points}")
