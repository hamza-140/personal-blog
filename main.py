from flask import Flask, render_template, request, redirect, url_for, session
import os
import json
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'blog'
ARTICLES_DIR = 'articles'

def load_articles():
    articles = []
    for filename in os.listdir(ARTICLES_DIR):
        with open(os.path.join(ARTICLES_DIR, filename), 'r') as f:
            articles.append(json.load(f))
    return articles
@app.template_filter('format_date')
def format_date(value, format='%B %d, %Y'):
    if isinstance(value, str):
        value = datetime.strptime(value, '%Y-%m-%d')
    return value.strftime(format)
@app.route('/')
@app.route('/home')
def index():
    articles = load_articles()
    return render_template('home.html', articles=articles)

@app.route('/admin')
def admin():
    if session.get('admin') is not True:
        return redirect(url_for('forbid'))
    articles = load_articles()
    return render_template('admin.html', articles=articles)

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('index'))

@app.route('/article/delete/<int:article_id>', methods=['POST'])
def delete(article_id):
    article_filename = f"article{article_id}.json"
    file_path = os.path.join(ARTICLES_DIR, article_filename)

    if os.path.exists(file_path):
        os.remove(file_path)
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('forbid'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == 'admin@mail.com' and password == '123':
            session['admin'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error='Invalid credentials. Please try again.')
    return render_template('login.html')

@app.route('/403')
def forbid():
    return render_template('403.html')


@app.route('/new', methods=['GET', 'POST'])
def new():
    if session.get('admin') is not True:
        return redirect(url_for('forbid'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date = request.form['date']

        new_article = {
            'title': title,
            'content': content,
            'date': date
        }
        article_filename = f"article{len(os.listdir(ARTICLES_DIR)) + 1}.json"
        with open(os.path.join(ARTICLES_DIR, article_filename), 'w') as f:
            json.dump(new_article, f)

        return redirect('/admin')
    return render_template('new.html')

@app.route('/article/<int:article_id>')
def article(article_id):
    articles = load_articles()
    article = articles[article_id - 1]
    return render_template('article.html', article=article)


@app.route('/article/edit/<int:article_id>', methods=['GET', 'POST'])
def edit(article_id):
    if session.get('admin') is not True:
        return redirect(url_for('forbid'))

    article_filename = f"article{article_id}.json"
    file_path = os.path.join(ARTICLES_DIR, article_filename)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date = request.form['date']

        edit_article = {
            'title': title,
            'content': content,
            'date': date
        }

        # Update the article JSON file
        with open(file_path, 'w') as f:
            json.dump(edit_article, f)

        return redirect(url_for('admin'))

    # Ensure the article is loaded for GET requests
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            article = json.load(f)
        return render_template('edit.html', article=article,article_id = article_id)
    else:
        return redirect(url_for('forbid'))

if __name__ == "__main__":
	app.run()
