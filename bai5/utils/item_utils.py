"""
utils/item_utils.py
---------------------
Chứa logic liên quan đến vật phẩm:
- open_treasure_chest(records): mở rương báu ngẫu nhiên (chức năng 2).
- buy_item(records): mua vật phẩm trong cửa hàng (chức năng 3).

Module chuẩn sử dụng: random (để random phần thưởng khi mở rương).
"""

import random

from utils.player_utils import find_player

# Danh sách phần thưởng có thể nhận được khi mở rương báu.
REWARDS = ["Potion", "Iron Sword", "Magic Scroll", "100 Gold", "Mana Stone"]

# Danh sách vật phẩm và giá tiền trong cửa hàng.
SHOP_ITEMS = {
    "Potion": 50,
    "Iron Sword": 200,
    "Magic Book": 300,
    "Mana Stone": 150
}


def open_treasure_chest(records):
    """
    Mở rương báu ngẫu nhiên cho một người chơi.

    Input:
        records (list[dict]): danh sách người chơi (player_records), sẽ bị
                               thay đổi trực tiếp (in-place) nếu mở rương thành công.
    Output:
        None: hàm chỉ in kết quả ra màn hình và cập nhật records, không trả về giá trị.

    Pseudocode:
        - Nếu records rỗng -> in "Hệ thống chưa có dữ liệu người chơi." và return.
        - Nhập mã người chơi muốn mở rương.
        - Dùng find_player() để tìm index người chơi (đã tự chuẩn hóa mã).
        - Nếu index == -1 -> in "Không tìm thấy người chơi!" và return.
        - Random một phần thưởng trong REWARDS bằng random.choice().
        - Nếu phần thưởng là "100 Gold" -> cộng 100 vào gold của người chơi.
        - Ngược lại -> thêm phần thưởng vào inventory của người chơi.
        - In thông báo kết quả mở rương.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    player_id = input("Nhập mã người chơi mở rương: ")
    index = find_player(records, player_id)

    if index == -1:
        print("Không tìm thấy người chơi!")
        return

    player = records[index]
    reward = random.choice(REWARDS)

    print(f">> Người chơi {player['name']} đã mở rương!")
    print(f">> Phần thưởng nhận được: {reward}")

    if reward == "100 Gold":
        player["gold"] += 100
        print(">> Đã cộng 100 Gold vào tài khoản.")
    else:
        player["inventory"].append(reward)
        print(f">> Đã thêm {reward} vào túi đồ.")


def buy_item(records):
    """
    Mua vật phẩm trong cửa hàng cho một người chơi.

    Input:
        records (list[dict]): danh sách người chơi (player_records), sẽ bị
                               thay đổi trực tiếp (in-place) nếu mua thành công.
    Output:
        None: hàm chỉ in kết quả ra màn hình và cập nhật records, không trả về giá trị.

    Pseudocode (Chức năng 3 - Mua vật phẩm):
        - Nếu records rỗng -> in "Hệ thống chưa có dữ liệu người chơi." và return.
        - Nhập mã người chơi.
        - Dùng find_player() để tìm index người chơi.
        - Nếu index == -1 -> in "Không tìm thấy người chơi!" và return.
        - Nhập tên vật phẩm muốn mua.
        - Nếu tên vật phẩm không tồn tại trong SHOP_ITEMS
            -> in "Vật phẩm không tồn tại trong cửa hàng!" và return.
        - Lấy giá vật phẩm từ SHOP_ITEMS.
        - Nếu gold của người chơi < giá vật phẩm
            -> in "Không đủ vàng để mua vật phẩm này!" và return.
        - Ngược lại:
            -> Trừ gold của người chơi theo giá vật phẩm.
            -> Thêm vật phẩm vào inventory của người chơi.
            -> In thông báo mua thành công và số vàng còn lại.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    player_id = input("Nhập mã người chơi: ")
    index = find_player(records, player_id)

    if index == -1:
        print("Không tìm thấy người chơi!")
        return

    player = records[index]
    item_name = input("Nhập tên vật phẩm muốn mua: ").strip()

    # Chuẩn hóa tên vật phẩm để so khớp không phân biệt hoa thường, nhưng vẫn
    # hiển thị/lưu theo đúng tên gốc trong SHOP_ITEMS.
    matched_item = None
    for shop_item_name in SHOP_ITEMS:
        if shop_item_name.lower() == item_name.lower():
            matched_item = shop_item_name
            break

    if matched_item is None:
        print("Vật phẩm không tồn tại trong cửa hàng!")
        return

    price = SHOP_ITEMS[matched_item]

    if player["gold"] < price:
        print("Không đủ vàng để mua vật phẩm này!")
        return

    player["gold"] -= price
    player["inventory"].append(matched_item)

    print(f">> Mua thành công {matched_item}!")
    print(f">> Số vàng còn lại: {player['gold']}")
