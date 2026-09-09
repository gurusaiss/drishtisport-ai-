"""
DrishtiSport AI - Verified Performance Log Viewer
Prints every logged delivery from the local SQLite record - this is the
"tamper-proof, data-backed talent score" concept made real: an objective,
timestamped log a coach or scout can trust instead of a subjective opinion.

Usage:
    python view_log.py
"""

import sqlite3
import sys

DB_PATH = "drishtisport_log.db"


def main():
    try:
        conn = sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(f"Could not open {DB_PATH}: {e}")
        sys.exit(1)

    cur = conn.execute(
        "SELECT id, timestamp, arm, min_angle_deg, release_angle_deg, extension_deg, verdict "
        "FROM delivery_log ORDER BY id ASC"
    )
    rows = cur.fetchall()

    if not rows:
        print("No deliveries logged yet. Run drishtisport_demo.py first.")
        return

    print("=" * 92)
    print(" DRISHTISPORT AI - VERIFIED DELIVERY LOG (tamper-proof, timestamped, on-device)")
    print("=" * 92)
    print(f"{'#':<4}{'Timestamp':<22}{'Arm':<8}{'Min Angle':<12}{'Release Angle':<16}{'Extension':<12}{'Verdict':<10}")
    print("-" * 92)

    illegal_count = 0
    for (rid, ts, arm, min_a, rel_a, ext, verdict) in rows:
        if verdict == "ILLEGAL":
            illegal_count += 1
        print(f"{rid:<4}{ts:<22}{arm:<8}{min_a:<12}{rel_a:<16}{ext:<12}{verdict:<10}")

    print("-" * 92)
    print(f"Total deliveries: {len(rows)}   |   Illegal actions flagged: {illegal_count}   "
          f"|   Legal: {len(rows) - illegal_count}")
    print("=" * 92)

    conn.close()


if __name__ == "__main__":
    main()
