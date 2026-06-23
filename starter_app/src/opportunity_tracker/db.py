import os
import sqlite3
from pathlib import Path
from typing import Any

DEFAULT_DB_PATH = "starter_app/opportunities.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS opportunities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    source TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'idea',
    deadline TEXT,
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""


def get_db_path() -> str:
    """Return the SQLite database path from the environment or default."""

    return os.getenv("OPPORTUNITY_DB_PATH", DEFAULT_DB_PATH)


def connect() -> sqlite3.Connection:
    """Open a SQLite connection and make rows behave like dictionaries."""

    db_path = get_db_path()
    if db_path != ":memory:":
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    """Create the database table if it does not already exist."""

    with connect() as connection:
        connection.executescript(SCHEMA)


def row_to_dict(row: sqlite3.Row | None) -> dict[str, Any] | None:
    """Convert a SQLite row into a plain dictionary."""

    if row is None:
        return None
    return dict(row)


def create_opportunity(data: dict[str, Any]) -> dict[str, Any]:
    """Insert and return a new opportunity."""

    init_db()
    with connect() as connection:
        cursor = connection.execute(
            """
            INSERT INTO opportunities (title, source, status, deadline, notes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                data["title"],
                data["source"],
                data.get("status", "idea"),
                str(data["deadline"]) if data.get("deadline") else None,
                data.get("notes"),
            ),
        )
        opportunity_id = cursor.lastrowid
        connection.commit()
    opportunity = get_opportunity(opportunity_id)
    if opportunity is None:
        raise RuntimeError("Opportunity was created but could not be loaded")
    return opportunity


def list_opportunities(status: str | None = None) -> list[dict[str, Any]]:
    """Return all opportunities, optionally filtered by status."""

    init_db()
    with connect() as connection:
        if status:
            rows = connection.execute(
                "SELECT * FROM opportunities WHERE status = ? ORDER BY id DESC",
                (status,),
            ).fetchall()
        else:
            rows = connection.execute("SELECT * FROM opportunities ORDER BY id DESC").fetchall()
    return [dict(row) for row in rows]


def get_opportunity(opportunity_id: int) -> dict[str, Any] | None:
    """Return one opportunity by id."""

    init_db()
    with connect() as connection:
        row = connection.execute(
            "SELECT * FROM opportunities WHERE id = ?",
            (opportunity_id,),
        ).fetchone()
    return row_to_dict(row)


def update_opportunity_status(opportunity_id: int, status: str) -> dict[str, Any] | None:
    """Update an opportunity status and return the updated row."""

    init_db()
    with connect() as connection:
        cursor = connection.execute(
            "UPDATE opportunities SET status = ? WHERE id = ?",
            (status, opportunity_id),
        )
        connection.commit()
        if cursor.rowcount == 0:
            return None
    return get_opportunity(opportunity_id)
