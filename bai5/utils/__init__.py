"""
utils/__init__.py
------------------
Biến thư mục utils/ thành một package Python.

Đồng thời file này thực hiện "import nâng cao": re-export các hàm quan trọng
từ các module con (player_utils, item_utils, battle_utils) ngay tại cấp package,
giúp main.py có thể gọi:

    from utils import find_player, open_treasure_chest, buy_item, fight_monster

thay vì phải import dài dòng từng module con một.
"""

from utils.player_utils import find_player, normalize_player_id
from utils.item_utils import open_treasure_chest, buy_item
from utils.battle_utils import fight_monster

__all__ = [
    "find_player",
    "normalize_player_id",
    "open_treasure_chest",
    "buy_item",
    "fight_monster",
]
