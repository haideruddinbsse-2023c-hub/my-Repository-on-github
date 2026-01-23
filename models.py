from database import get_connection

def add_bug(title, description, assigned_to, created_by):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bugs (title, description, status, assigned_to, created_by)
        VALUES (?, ?, 'Open', ?, ?)
    """, (title, description, assigned_to, created_by))

    conn.commit()
    conn.close()

def get_all_bugs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bugs")
    data = cursor.fetchall()

    conn.close()
    return data

def update_bug_status(bug_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE bugs SET status = ? WHERE id = ?", (status, bug_id))

    conn.commit()
    conn.close()
