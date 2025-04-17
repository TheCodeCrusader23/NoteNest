import mysql.connector as mc

# Connect to MySQL
conn = mc.connect(
    host="localhost",
    user="root",
    password="parth@123",
    database="NoteApp"
)
cursor = conn.cursor()

def add_note():
    title = input("Enter title: ").strip()
    content = input("Enter content: ").strip()
    if title and content:
        cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
        conn.commit()
        print("✅ Note added successfully.\n")
    else:
        print("⚠️  Title and content cannot be empty.\n")

def view_notes():
    cursor.execute("SELECT id, title, created_at FROM notes")
    rows = cursor.fetchall()
    print("\n📋 All Notes:")
    for row in rows:
        print(f"ID: {row[0]} | Title: {row[1]} | Created At: {row[2]}")
    print()

def view_note_detail():
    note_id = input("Enter note ID to view: ")
    cursor.execute("SELECT title, content FROM notes WHERE id = %s", (note_id,))
    result = cursor.fetchone()
    if result:
        print(f"\n📝 {result[0]}\n{'-'*40}\n{result[1]}\n")
    else:
        print("❌ Note not found.\n")

def delete_note():
    note_id = input("Enter note ID to delete: ")
    cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    conn.commit()
    print(f"🗑️ Note ID {note_id} deleted.\n")

def update_note():
    note_id = input("Enter note ID to update: ")
    cursor.execute("SELECT title, content FROM notes WHERE id = %s", (note_id,))
    result = cursor.fetchone()
    if not result:
        print("❌ Note not found.\n")
        return
    new_title = input(f"Enter new title (Leave empty to keep '{result[0]}'): ") or result[0]
    new_content = input(f"Enter new content (Leave empty to keep existing content): ") or result[1]
    cursor.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (new_title, new_content, note_id))
    conn.commit()
    print("✏️ Note updated.\n")

def main():
    while True:
        print("==== Note Taking App ====")
        print("1. Add Note")
        print("2. View Notes (Summary)")
        print("3. View Note Detail")
        print("4. Update Note")
        print("5. Delete Note")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        print()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            view_note_detail()
        elif choice == "4":
            update_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            break
        else:
            print("❗ Invalid choice. Try again.\n")

    # Close DB connection on exit
    cursor.close()
    conn.close()
    print("👋 Exiting. Goodbye!")

if __name__ == "__main__":
    main()
