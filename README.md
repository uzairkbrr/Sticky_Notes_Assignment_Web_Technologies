# Ideaflip Inspired Sticky Notes

A modern, beautifully designed Django web application that allows users to create, view, edit, and organize digital sticky notes. 

Built as a University Web Engineering Assignment, this project started as a simple CRUD app and evolved into a highly polished, Ideaflip-inspired interface featuring a meticulously centered canvas layout, authentic sticky-note visuals with folded corners, and dynamic contrast-adjusted typography.

## ✨ Features
- **Modern UI/UX**: Clean, centered canvas layout inspired by the Ideaflip web app utilizing custom Google Fonts (Montserrat).
- **Authentic Note Cards**: Sticky notes look and feel physical, complete with drop shadows, subtle border radiuses, and CSS-folded corners.
- **Dynamic Text Colors**: Uses backend luminance calculations to automatically switch note text between dark gray and white depending on the sticky note's background color, ensuring perfect readability.
- **Authentication**: Secure user registration, login, and logout. Users can only access their personal dashboard.
- **CRUD Operations**: Full Create, Read, Update, and Delete capabilities for notes.

## 🚀 Quick Start (Using bash script)

For your convenience, a bash script is included to automatically install dependencies, run migrations, and start the server.

If you are on Linux, macOS, or using Git Bash / WSL on Windows:

```bash
# Make the script executable
chmod +x run.sh

# Run the script
./run.sh
```

## 🛠 Manual Installation & Setup

If you prefer to run the commands manually or are using standard Windows Command Prompt/PowerShell:

1. **Install Django**
   ```bash
   pip install django
   ```

2. **Run Migrations** (To setup the SQLite database)
   ```bash
   python manage.py makemigrations notes
   python manage.py migrate
   ```

3. **Start the Server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```text
p229021_Uzair-Ahmad_Assignment-02/
    manage.py
    run.sh            <-- Quick start script
    README.md
    sticky_project/   <-- Main Django settings and routing
    notes/            <-- Core application (models, views, templates)
        models.py
        views.py
        templates/
            base.html
            note_list.html...
        static/
            styles.css
```

## 👤 Author
**Uzair Ahmad (p229021)** - Web Engineering Assignment
