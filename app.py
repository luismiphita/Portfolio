from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ConfiguraciÃ³n de la base de datos
def init_db():
    with sqlite3.connect("portfolio.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                image TEXT NOT NULL
            )
        """)
init_db()

@app.route('/')
def index():
    with sqlite3.connect("portfolio.db") as conn:
        projects = conn.execute("SELECT * FROM projects").fetchall()
    return render_template('index.html', projects=projects)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = request.files['image']
        
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)

            with sqlite3.connect("portfolio.db") as conn:
                conn.execute("INSERT INTO projects (title, description, image) VALUES (?, ?, ?)",
                             (title, description, filename))

            return redirect(url_for('index'))
    
    return render_template('upload.html')

@app.route('/delete/<int:project_id>', methods=['POST'])
def delete(project_id):
    with sqlite3.connect("portfolio.db") as conn:
        project = conn.execute("SELECT image FROM projects WHERE id = ?", (project_id,)).fetchone()
        
        if project:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], project[0])
            if os.path.exists(image_path):
                os.remove(image_path)
            conn.execute("DELETE FROM projects WHERE id = ?", (project_id,))
    
    return redirect(url_for('index'))

@app.route('/edit/<int:project_id>', methods=['GET', 'POST'])
def edit(project_id):
    with sqlite3.connect("portfolio.db") as conn:
        project = conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        with sqlite3.connect("portfolio.db") as conn:
            conn.execute("UPDATE projects SET title = ?, description = ? WHERE id = ?", (title, description, project_id))
        
        return redirect(url_for('index'))
    
    return render_template('edit.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)