import sqlite3
from typing import List, TypedDict
from datetime import datetime, timedelta

class Chat(TypedDict):
    id: int
    chat_id: str

class Log(TypedDict):
    id: int
    mic_status: str
    timestamps: str


class DB:
    _conn: sqlite3.Connection

    def __init__(self) -> None:
        self._conn = sqlite3.connect("../class-monitoring-condition.db")

        # Check if tables exist, create them if not
        if "chat" not in self._conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall():
            self._conn.execute("CREATE TABLE IF NOT EXISTS chat (id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id TEXT)")
        
        if "log" not in self._conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall():
            self._conn.execute("CREATE TABLE IF NOT EXISTS log (id INTEGER PRIMARY KEY AUTOINCREMENT, mic_status TEXT, timestamps TEXT)")
    
    def insert_chat(self, chat_id: str):
        try:
            self._conn.execute("INSERT INTO chat (chat_id) VALUES (?)", (chat_id,))
            self._conn.commit()  # Commit the transaction
        except:
            raise Exception("ERROR: failed to insert chat id")
    
    def get_chat(self) -> List[Chat]:
        data: List[Chat] = []

        try:
            result = self._conn.execute("SELECT * FROM chat")
            for row in result:
                data.append({
                    "id": row[0],
                    "chat_id": row[1]
                })
            return data
        except:
            raise Exception("ERROR: Failed to get chat")
    def insert_log(self, mic_status: str):
        try:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._conn.execute("INSERT INTO log (mic_status, timestamps) VALUES (?, ?)", (mic_status, current_time))
            self._conn.commit()
        except:
            raise Exception("ERROR: failed to insert log")
    
    def get_logs_last_week(self) -> List[Log]:
        data: List[Log] = []

        try:
            one_week_ago = (datetime.now() - timedelta(weeks=1)).strftime('%Y-%m-%d %H:%M:%S')
            result = self._conn.execute("SELECT * FROM log WHERE timestamps >= ?", (one_week_ago,))
            for row in result:
                data.append({
                    "id": row[0],
                    "mic_status": row[1],
                    "timestamps": row[2]
                })
            return data
        except:
            raise Exception("ERROR: Failed to get logs")

