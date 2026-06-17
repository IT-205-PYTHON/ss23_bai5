"""
utils/battle_utils.py
-----------------------
Chứa logic chiến đấu với quái vật (chức năng 4).

Module chuẩn sử dụng: random (để random quái vật xuất hiện).
"""

import random

from utils.player_utils import find_player

# Danh sách quái vật có thể xuất hiện khi chiến đấu.
MONSTERS = [
    {"name": "Bug Python", "damage": 20, "reward_gold": 100},
    {"name": "Import Error", "damage": 35, "reward_gold": 150},
    {"name": "Module Not Found", "damage": 50, "reward_gold": 250}
]


def fight_monster(records):
    """
    Cho một người chơi chiến đấu với quái vật ngẫu nhiên.

    Input:
        records (list[dict]): danh sách người chơi (player_records), sẽ bị
                               thay đổi trực tiếp (in-place) sau khi chiến đấu.
    Output:
        None: hàm chỉ in kết quả ra màn hình và cập nhật records, không trả về giá trị.

    Pseudocode (Chức năng 4 - Chiến đấu với quái vật):
        - Nếu records rỗng -> in "Hệ thống chưa có dữ liệu người chơi." và return.
        - Nhập mã người chơi muốn chiến đấu.
        - Dùng find_player() để tìm index người chơi.
        - Nếu index == -1 -> in "Không tìm thấy người chơi!" và return.
        - Nếu hp của người chơi <= 0
            -> in "Người chơi đã gục ngã, không thể tiếp tục chiến đấu!" và return.
        - Random một quái vật trong MONSTERS bằng random.choice().
        - In tên quái vật xuất hiện.
        - Trừ hp của người chơi theo damage của quái vật.
        - In số HP bị mất.
        - Nếu hp sau khi trừ > 0:
            -> Người chơi thắng, cộng reward_gold vào gold.
            -> In "Chiến thắng!" và số vàng nhận được.
        - Ngược lại (hp <= 0):
            -> Người chơi thua, không cộng vàng.
            -> In "Thua trận!" (không nhận vàng).
            -> Đảm bảo hp không xuống dưới 0 (để hiển thị thân thiện, gán hp = 0 nếu âm).
        - In HP còn lại của người chơi.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    player_id = input("Nhập mã người chơi chiến đấu: ")
    index = find_player(records, player_id)

    if index == -1:
        print("Không tìm thấy người chơi!")
        return

    player = records[index]

    if player["hp"] <= 0:
        print("Người chơi đã gục ngã, không thể tiếp tục chiến đấu!")
        return

    monster = random.choice(MONSTERS)
    print(f">> Quái vật xuất hiện: {monster['name']}")

    player["hp"] -= monster["damage"]
    print(f">> {player['name']} bị mất {monster['damage']} HP.")

    if player["hp"] > 0:
        player["gold"] += monster["reward_gold"]
        print(f">> Chiến thắng! Bạn nhận được {monster['reward_gold']} vàng.")
    else:
        player["hp"] = 0
        print(">> Thua trận! Bạn không nhận được vàng.")

    print(f">> HP còn lại: {player['hp']}")
