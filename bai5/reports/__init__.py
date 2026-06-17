"""
reports/__init__.py
---------------------
Biến thư mục reports/ thành một package Python.

Re-export hàm hiển thị/báo cáo để main.py có thể import gọn:

    from reports import display_players, show_leaderboard
"""

from reports.dungeon_report import (
    display_players,
    show_leaderboard,
    get_player_status,
    export_player_report,
)

__all__ = [
    "display_players",
    "show_leaderboard",
    "get_player_status",
    "export_player_report",
]
