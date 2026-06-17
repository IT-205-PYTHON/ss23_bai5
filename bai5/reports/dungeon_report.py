"""
reports/dungeon_report.py
---------------------------
Chứa logic hiển thị và xuất báo cáo:
- get_player_status(hp): xác định trạng thái người chơi dựa trên hp.
- display_players(records): hiển thị danh sách người chơi (chức năng 1).
- show_leaderboard(records): hiển thị bảng xếp hạng người chơi (chức năng 5).
- export_player_report(records, filename): xuất báo cáo người chơi ra file .txt
  (sử dụng third-party module "tabulate" để format bảng đẹp hơn).

Module chuẩn sử dụng: operator (itemgetter để sort theo nhiều tiêu chí).
Third-party module sử dụng: tabulate (format báo cáo dạng bảng khi xuất file).
"""

import operator

try:
    from tabulate import tabulate
    _HAS_TABULATE = True
except ImportError:
    # Nếu môi trường chưa cài tabulate, chương trình vẫn chạy được,
    # chỉ riêng export_player_report() sẽ dùng format bảng thủ công.
    _HAS_TABULATE = False


def get_player_status(hp):
    """
    Xác định trạng thái người chơi dựa trên hp hiện tại.

    Input:
        hp (int): máu hiện tại của người chơi.
    Output:
        str: trạng thái tương ứng:
             "Đã gục ngã"  nếu hp <= 0
             "Nguy hiểm"   nếu 1 <= hp < 50
             "Ổn định"     nếu 50 <= hp < 100
             "Sung sức"    nếu hp >= 100

    Pseudocode:
        - Nếu hp <= 0 -> trả về "Đã gục ngã".
        - Ngược lại nếu hp < 50 -> trả về "Nguy hiểm".
        - Ngược lại nếu hp < 100 -> trả về "Ổn định".
        - Ngược lại -> trả về "Sung sức".
    """
    if hp <= 0:
        return "Đã gục ngã"
    elif hp < 50:
        return "Nguy hiểm"
    elif hp < 100:
        return "Ổn định"
    else:
        return "Sung sức"


def display_players(records):
    """
    Hiển thị danh sách toàn bộ người chơi cùng trạng thái hiện tại.

    Input:
        records (list[dict]): danh sách người chơi (player_records).
    Output:
        None: hàm chỉ in kết quả ra màn hình, không trả về giá trị.

    Pseudocode:
        - Nếu records rỗng -> in "Hệ thống chưa có dữ liệu người chơi." và return.
        - In tiêu đề "--- DANH SÁCH NGƯỜI CHƠI ---".
        - Duyệt qua records bằng enumerate() (bắt đầu từ 1).
        - Với mỗi người chơi:
            -> Tính trạng thái bằng get_player_status(hp).
            -> In thông tin: số thứ tự, mã, tên, hp, mana, gold, level, trạng thái.
        - In dòng kết thúc.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    print("--- DANH SÁCH NGƯỜI CHƠI ---")
    for i, player in enumerate(records, start=1):
        status = get_player_status(player["hp"])
        print(
            f"{i}. Mã: {player['player_id']} | Tên: {player['name']} | "
            f"HP: {player['hp']} | Mana: {player['mana']} | "
            f"Gold: {player['gold']} | Level: {player['level']} | "
            f"Trạng thái: {status}"
        )
    print("------------------------------")


def show_leaderboard(records):
    """
    Hiển thị bảng xếp hạng người chơi, không làm thay đổi thứ tự gốc của records.

    Input:
        records (list[dict]): danh sách người chơi (player_records).
    Output:
        None: hàm chỉ in kết quả ra màn hình, không trả về giá trị.

    Pseudocode:
        - Nếu records rỗng -> in "Hệ thống chưa có dữ liệu người chơi." và return.
        - Tạo bản sao danh sách bằng list(records) hoặc records[:] để KHÔNG làm
          thay đổi thứ tự gốc của player_records.
        - Sắp xếp bản sao theo 3 tiêu chí, ưu tiên giảm dần (reverse=True):
            1. level (cao hơn xếp trước)
            2. gold (nếu cùng level, nhiều vàng hơn xếp trước)
            3. hp (nếu cùng level và cùng vàng, hp cao hơn xếp trước)
          Sử dụng operator.itemgetter("level", "gold", "hp") làm key cho sorted().
        - In tiêu đề "--- BẢNG XẾP HẠNG NGƯỜI CHƠI ---".
        - Duyệt qua danh sách đã sắp xếp, in thứ hạng, tên, level, gold, hp.
        - In dòng kết thúc.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    # Tạo bản sao để không ảnh hưởng đến thứ tự gốc của player_records.
    sorted_records = sorted(
        records[:],
        key=operator.itemgetter("level", "gold", "hp"),
        reverse=True
    )

    print("--- BẢNG XẾP HẠNG NGƯỜI CHƠI ---")
    for i, player in enumerate(sorted_records, start=1):
        print(
            f"{i}. {player['name']} | Level: {player['level']} | "
            f"Gold: {player['gold']} | HP: {player['hp']}"
        )
    print("--------------------------------")


def export_player_report(records, filename="player_report.txt"):
    """
    Xuất báo cáo danh sách người chơi ra file văn bản (.txt), có sử dụng
    third-party module "tabulate" để format dạng bảng cho dễ đọc.

    Input:
        records (list[dict]): danh sách người chơi (player_records).
        filename (str): tên file xuất ra (mặc định "player_report.txt").
    Output:
        None: hàm ghi dữ liệu ra file và in thông báo, không trả về giá trị.

    Pseudocode:
        - Nếu records rỗng -> in "Hệ thống chưa có dữ liệu người chơi." và return.
        - Chuẩn bị dữ liệu dạng bảng: mỗi dòng gồm mã, tên, hp, mana, gold,
          level, trạng thái (tính bằng get_player_status()).
        - Nếu có tabulate -> dùng tabulate() để format thành chuỗi bảng đẹp.
          Nếu không có tabulate -> tự ghép chuỗi bảng đơn giản bằng f-string.
        - Mở file ở chế độ ghi ("w", encoding="utf-8") và viết nội dung bảng vào.
        - In thông báo xuất báo cáo thành công kèm tên file.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    headers = ["Mã", "Tên", "HP", "Mana", "Gold", "Level", "Trạng thái"]
    rows = []
    for player in records:
        rows.append([
            player["player_id"],
            player["name"],
            player["hp"],
            player["mana"],
            player["gold"],
            player["level"],
            get_player_status(player["hp"]),
        ])

    if _HAS_TABULATE:
        table_text = tabulate(rows, headers=headers, tablefmt="grid")
    else:
        # Fallback đơn giản nếu chưa cài tabulate.
        table_text = " | ".join(headers) + "\n"
        for row in rows:
            table_text += " | ".join(str(cell) for cell in row) + "\n"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("BÁO CÁO NGƯỜI CHƠI - RIKKEI DUNGEON\n\n")
        f.write(table_text)
        f.write("\n")

    print(f">> Đã xuất báo cáo người chơi ra file: {filename}")
