"""
data/players.py
----------------
Chứa dữ liệu người chơi ban đầu (player_records) cho Rikkei Dungeon.
Đây là "nguồn dữ liệu" duy nhất được import vào main.py khi khởi động chương trình.
"""

player_records = [
    {
        "player_id": "PL01",
        "name": "Nguyễn Văn Module",
        "hp": 100,
        "mana": 50,
        "gold": 300,
        "inventory": ["Potion", "Wooden Sword"],
        "level": 1
    },
    {
        "player_id": "PL02",
        "name": "Trần Thị Package",
        "hp": 80,
        "mana": 70,
        "gold": 150,
        "inventory": ["Magic Book"],
        "level": 2
    },
    {
        "player_id": "PL03",
        "name": "Lê Văn Import",
        "hp": 120,
        "mana": 30,
        "gold": 500,
        "inventory": [],
        "level": 3
    }
]
