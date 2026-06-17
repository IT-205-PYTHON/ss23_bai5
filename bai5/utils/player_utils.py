"""
utils/player_utils.py
----------------------
Chứa các hàm phụ trợ liên quan đến người chơi:
- normalize_player_id(player_id): chuẩn hóa mã người chơi (strip + upper).
- find_player(records, player_id): tìm vị trí (index) của người chơi trong danh sách.

Đây là module "lõi" được tái sử dụng bởi item_utils, battle_utils và dungeon_report,
giúp tránh lặp lại logic tìm kiếm người chơi ở nhiều nơi (Modular Design).
"""


def normalize_player_id(player_id):
    """
    Chuẩn hóa mã người chơi: loại bỏ khoảng trắng dư và viết hoa toàn bộ.

    Input:
        player_id (str): mã người chơi do người dùng nhập, có thể chưa chuẩn
                          (ví dụ: " pl01 ", "pl01", "Pl01").
    Output:
        str: mã người chơi đã chuẩn hóa (ví dụ: "PL01").

    Pseudocode:
        - Loại bỏ khoảng trắng đầu/cuối bằng strip().
        - Viết hoa toàn bộ chuỗi bằng upper().
        - Trả về kết quả.
    """
    return player_id.strip().upper()


def find_player(records, player_id):
    """
    Tìm vị trí (index) của người chơi trong danh sách records dựa trên player_id.

    Input:
        records (list[dict]): danh sách người chơi (player_records).
        player_id (str): mã người chơi cần tìm (chưa cần chuẩn hóa trước).
    Output:
        int: index của người chơi trong records nếu tìm thấy.
             -1 nếu không tìm thấy.

    Pseudocode:
        - Chuẩn hóa player_id bằng normalize_player_id() (strip + upper).
        - Duyệt qua danh sách records bằng enumerate().
        - So sánh player_id đã chuẩn hóa với mã người chơi (đã chuẩn hóa) trong
          từng dictionary.
        - Nếu tìm thấy, trả về index tương ứng.
        - Nếu duyệt hết danh sách mà không tìm thấy, trả về -1.
    """
    normalized_id = normalize_player_id(player_id)

    for index, player in enumerate(records):
        if normalize_player_id(player["player_id"]) == normalized_id:
            return index

    return -1
