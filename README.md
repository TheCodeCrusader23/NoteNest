# 🗒️ NoteNest

A lightweight, terminal-based note taking application built with **Python** and **MySQL**. `NoteNest` allows you to quickly create, view, update, and delete notes via a clean command line interface, with data securely stored in a relational database.

---

## 🚀 Features

- ✅ Add new notes with a title and content
- 📋 View all notes (summary with timestamps)
- 🔍 View individual note details
- ✏️ Update existing notes (full or partial)
- 🗑️ Delete notes by ID
- 🗄️ Notes persist via MySQL database
- ⚙️ Input validation for empty values
- 🧠 Modular and readable Python code

---

## 🛠️ Tech Stack

| Layer      | Technology               |
|------------|--------------------------|
| Language   | Python (v3.13.5)         |
| Database   | MySQL (8.0.42)           |
| Connector  | mysql-connector-python   |
| Interface  | Command Line (CLI)       |

---

## 📸 Preview

> Curious how NoteNest works? Check out the full walkthrough with screenshots in the document below:

📄 **[View Complete Screenshot Walkthrough](https://1drv.ms/w/c/0f846526dc5ff851/EbhKA0Nwp8BBrP938HAU700B2r6dY6pWEKiAoBiLNG4Scg?e=AJdMBN)**  
*(Includes main menu, add/view/edit/delete notes, and full CLI flow)*

> The document showcases every feature of the app step by step ideal for visual learners or quick demos.

---

## 🧱 Database Schema

```sql
CREATE DATABASE IF NOT EXISTS NoteApp;
USE NoteApp;

CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
