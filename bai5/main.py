"""
main.py
--------
Chứa menu điều hướng chính của Rikkei Dungeon - Python Module Adventure System.

Đây là điểm khởi đầu (entry point) duy nhất của chương trình.
BẮT BUỘC chạy bằng:  python main.py
(chạy từ thư mục gốc project rikkei_dungeon/, KHÔNG chạy trực tiếp từng file con
 bên trong utils/ hoặc reports/, nếu không sẽ gặp lỗi ModuleNotFoundError).

--------------------------------------------------------------------------
CÁC KIỂU IMPORT ĐƯỢC SỬ DỤNG TRONG PROJECT (đáp ứng yêu cầu "ít nhất 3 kiểu import"):

    1. Import module chuẩn thông thường:
           import sys
           import random   (trong utils/item_utils.py, utils/battle_utils.py)
           import operator (trong reports/dungeon_report.py)

    2. Import có chọn lọc tên cụ thể (from ... import ...):
           from data.players import player_records
           from utils import find_player, open_treasure_chest, buy_item, fight_monster
           from reports import display_players, show_leaderboard, export_player_report

    3. Import third-party module:
           from tabulate import tabulate   (trong reports/dungeon_report.py)

    4. Import nâng cao - import động bằng importlib.import_module():
           Dùng để kiểm tra phiên bản Python lúc khởi động (xem hàm show_banner()).
--------------------------------------------------------------------------
"""

import sys
import importlib  # Import nâng cao: dùng importlib.import_module() để load module động.

from data.players import player_records
from utils import find_player, open_treasure_chest, buy_item, fight_monster
from reports import display_players, show_leaderboard, export_player_report


def show_banner():
    """
    Hiển thị banner chào mừng và thông tin phiên bản Python.

    Sử dụng import nâng cao (importlib.import_module) để load module "platform"
    một cách động ngay tại runtime, thay vì import tĩnh ở đầu file.

    Input: không có.
    Output: None, chỉ in thông tin ra màn hình.
    """
    platform_module = importlib.import_module("platform")
    print("=" * 60)
    print("   CHÀO MỪNG ĐẾN VỚI RIKKEI DUNGEON - PYTHON ADVENTURE")
    print(f"   (Python {platform_module.python_version()})")
    print("=" * 60)


def show_menu():
    """
    Hiển thị menu chức năng chính.

    Input: không có.
    Output: None, chỉ in menu ra màn hình.
    """
    print("\n===== RIKKEI DUNGEON - PYTHON MODULE ADVENTURE =====")
    print("1. Hiển thị danh sách người chơi")
    print("2. Mở rương báu ngẫu nhiên")
    print("3. Mua vật phẩm trong cửa hàng")
    print("4. Chiến đấu với quái vật")
    print("5. Xem bảng xếp hạng người chơi")
    print("6. Thoát chương trình")
    print("====================================================")


def main():
    """
    Hàm chính điều khiển toàn bộ luồng chương trình bằng vòng lặp while True.

    Input: không có.
    Output: None. Hàm chạy cho đến khi người dùng chọn chức năng 6 (thoát).

    Pseudocode:
        - Hiển thị banner chào mừng.
        - Lặp vô hạn (while True):
            -> Hiển thị menu.
            -> Nhập lựa chọn của người dùng.
            -> Nếu lựa chọn == "1" -> gọi display_players(player_records).
            -> Nếu lựa chọn == "2" -> gọi open_treasure_chest(player_records).
            -> Nếu lựa chọn == "3" -> gọi buy_item(player_records).
            -> Nếu lựa chọn == "4" -> gọi fight_monster(player_records).
            -> Nếu lựa chọn == "5" -> gọi show_leaderboard(player_records).
            -> Nếu lựa chọn == "6":
                -> In "Cảm ơn bạn đã tham gia Rikkei Dungeon!"
                -> Xuất báo cáo cuối cùng ra file bằng export_player_report().
                -> Thoát chương trình bằng sys.exit() (hoặc break).
            -> Nếu lựa chọn không hợp lệ -> in thông báo lỗi và lặp lại menu.
    """
    show_banner()

    while True:
        show_menu()
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            display_players(player_records)
        elif choice == "2":
            open_treasure_chest(player_records)
        elif choice == "3":
            buy_item(player_records)
        elif choice == "4":
            fight_monster(player_records)
        elif choice == "5":
            show_leaderboard(player_records)
        elif choice == "6":
            print("Cảm ơn bạn đã tham gia Rikkei Dungeon!")
            export_player_report(player_records)
            sys.exit(0)
        else:
            print(">> Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()
