import sqlite3
import os
from sqlite3 import Connection

# Database được lưu tại thư mục chứa script này
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(SCRIPT_DIR, "personnel.db")


def get_connection() -> Connection:
    return sqlite3.connect(DB_NAME)


def initialize_database() -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS personnel (
                cccd TEXT PRIMARY KEY,
                full_name TEXT NOT NULL,
                birth_date TEXT,
                gender TEXT,
                address TEXT
            )
            """
        )
        conn.commit()


def add_person(cccd: str, full_name: str, birth_date: str, gender: str, address: str) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO personnel (cccd, full_name, birth_date, gender, address) VALUES (?, ?, ?, ?, ?)",
            (cccd, full_name, birth_date, gender, address),
        )
        conn.commit()


def update_person(cccd: str, full_name: str, birth_date: str, gender: str, address: str) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE personnel SET full_name = ?, birth_date = ?, gender = ?, address = ? WHERE cccd = ?",
            (full_name, birth_date, gender, address, cccd),
        )
        conn.commit()


def delete_person(cccd: str) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM personnel WHERE cccd = ?", (cccd,))
        conn.commit()


def get_all_persons() -> list[tuple]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT cccd, full_name, birth_date, gender, address FROM personnel ORDER BY full_name")
        return cursor.fetchall()


def search_persons(cccd: str = "", full_name: str = "", address: str = "") -> list[tuple]:
    query = "SELECT cccd, full_name, birth_date, gender, address FROM personnel WHERE 1 = 1"
    params: list[str] = []

    if cccd.strip():
        query += " AND cccd LIKE ?"
        params.append(f"%{cccd.strip()}%")
    if full_name.strip():
        query += " AND full_name LIKE ?"
        params.append(f"%{full_name.strip()}%")
    if address.strip():
        query += " AND address LIKE ?"
        params.append(f"%{address.strip()}%")

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()


if __name__ == "__main__":
    initialize_database()
    print("Database initialized:", DB_NAME)
