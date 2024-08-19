<div align="center">
    
  # Personal Blog
  
  <img src="https://imgs.search.brave.com/AiAhPOHQRz2PE9_2QrvYcHSHtgwuHmNB-BgMRYley2Y/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMuZnJlZWltYWdl/cy5jb20vaW1hZ2Uv/cHJldmlld3MvN2Zh/L3BlbmNpbC1ydWxl/ci1zdHJva2UtaWNv/bi1wbmctZGVzaWdu/LTU2OTQ3NDMucG5n/P2ZtdA" height="100" alt="avatar" />
  
  [Overview](#🎯-overview) •
  [Features](#✨-features) •
  [Getting Started](#🚀-getting-started) •
  [Usage](#📘-usage) •
  [API](#📚-api)
  
  </div>
  
  ---
  
  ## 🎯 Overview
  
  This project is a personal blog application that allows users to view, create, edit, and delete articles. It includes two main sections: a guest section for browsing articles and an admin section for managing content. The main objective is to provide a platform for publishing and managing blog posts with basic authentication for admin functionality.
  
  ## ✨ Features
  
  - **Guest Section**:
    - **Home Page**: Displays a list of published articles.
    - **Article Page**: Shows the content of a selected article with its publication date.
  
  - **Admin Section**:
    - **Dashboard**: Lists articles with options to add, edit, or delete articles.
    - **Add Article Page**: Form to add new articles with title, content, and date.
    - **Edit Article Page**: Form to edit existing articles.
  
  - **Basic Authentication**: Secures admin access with a simple login mechanism.
  - **File-Based Storage**: Articles are stored as JSON files in the filesystem.
  
  ## 🚀 Getting Started
  
  To get a local copy up and running, follow these steps:
  
  ### Prerequisites
  
  Ensure you have the following installed:
  
  - Python 3
  - Flask
  
  ### Installation
  
  1. Clone the repository:
  
     ```bash
     git clone https://github.com/hamza-140/personal-blog.git
     cd personal-blog
     ```
  
  2. Install dependencies:
  
     ```bash
     pip install Flask
     ```
  
  3. Start the development server:
  
     ```bash
     python main.py
     ```
  
  ## 📘 Usage
  
  Navigate to `http://127.0.0.1:5000/` to view the blog. Use the following URLs for different functionalities:
  
  - **Home Page**: `http://127.0.0.1:5000/`
  - **Article Page**: `http://127.0.0.1:5000/article/<article_id>`
  - **Admin Login**: `http://127.0.0.1:5000/login`
  - **Admin Dashboard**: `http://127.0.0.1:5000/admin`
  - **New Article**: `http://127.0.0.1:5000/new`
  - **Edit Article**: `http://127.0.0.1:5000/article/edit/<article_id>`
  - **Logout**: `http://127.0.0.1:5000/logout`
  
  ## 📚 API
  
  This section documents the main routes of the application. Each route is described with its parameters and examples.
  
  ### `GET /`
  
  Displays the home page with a list of articles.
  
  **Example**:
  
  Navigate to `http://127.0.0.1:5000/`.
  
  ### `GET /article/<int:article_id>`
  
  Displays the content of a specific article.
  
  **Example**:
  
  Navigate to `http://127.0.0.1:5000/article/1`.
  
  ### `GET /admin`
  
  Displays the admin dashboard with article management options. Requires admin authentication.
  
  **Example**:
  
  Navigate to `http://127.0.0.1:5000/admin`.
  
  ### `POST /article/delete/<int:article_id>`
  
  Deletes the specified article. Requires admin authentication.
  
  **Example**:
  
  Send a POST request to `http://127.0.0.1:5000/article/delete/1`.
  
  ### `GET /login`
  ### `POST /login`
  
  Displays the login page and handles authentication.
  
  **Example**:
  
  Navigate to `http://127.0.0.1:5000/login` to log in.
  
  ### `GET /new`
  ### `POST /new`
  
  Displays the form to add a new article and handles submission.
  
  **Example**:
  
  Navigate to `http://127.0.0.1:5000/new` to add an article.
  
  ### `GET /article/edit/<int:article_id>`
  ### `POST /article/edit/<int:article_id>`
  
  Displays the form to edit an existing article and handles submission.
  
  **Example**:
  
  Navigate to `http://127.0.0.1:5000/article/edit/1` to edit an article.
## CC
https://roadmap.sh/projects/personal-blog