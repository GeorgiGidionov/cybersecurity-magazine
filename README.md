Technologies Used
 Backend: Django 6.0.2, Python 3.13
Project Structure
text

cybersecurity-magazine/
├── cybersecurity_magazine/       # Project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py                  # Home, About, Contact views
│   └── wsgi.py
├── articles/                      # Articles app
│   ├── migrations/
│   ├── templatetags/              # Custom template tags
│   │   ├── __init__.py
│   │   └── magazine_extras.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── store/                          # Store app
│   ├── ... (similar structure)
├── subscriptions/                  # Subscriptions app
│   ├── ... (similar structure)
├── templates/                      # Global templates
│   ├── base.html
│   ├── 404.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── partials/                   # Reusable snippets
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   ├── pagination.html
│   │   └── latest_articles.html
│   ├── articles/
│   ├── store/
│   └── subscriptions/
├── static/                          # Static files
│   ├── css/
│   ├── js/
│   └── images/                      # Background image, logos
├── media/                            # User uploads (optional)
├── requirements.txt
├── manage.py
├── .env.example                      # Example environment variables
└── README.md                         # You are here!
Installation & Setup




Create a database and user:
sql

CREATE DATABASE cybersecurity_magazine;
CREATE USER postgres 
WITH PASSWORD 123456;
GRANT ALL PRIVILEGES ON DATABASE cybersecurity_magazine TO postgres;

Set environment variables

Create a .env file in the project root (use .env.example as a template):
env

SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=cybersecurity_magazine
DB_USER=postgres
DB_PASSWORD=123456
DB_HOST=localhost
DB_PORT=5432



Run the development server

python manage.py runserver

Visit http://127.0.0.1:8000/
Home Page

  Displays featured articles and latest products.

  Background image sets the cybersecurity theme.

Articles

  List all articles – /articles/ (filterable by category via URL).

  View article details – /articles/<slug>/.

  Create new article – /articles/create/ (form with validation).

  Edit article – /articles/<slug>/edit/ (status becomes read‑only if published).

  Delete article – /articles/<slug>/delete/ (confirmation required).

Store

  List all products – /store/ (sort by price or newest).

  View product details – /store/<slug>/.

  Create product – /store/create/.

  Edit product – /store/<slug>/edit/.

  Delete product – /store/<slug>/delete/.

  Place an order – /store/order/<slug>/ (simple order form).

Subscriptions

  View subscription plans – /subscriptions/.

  Subscribe – /subscriptions/subscribe/ (form with date validation).

  Success page – /subscriptions/success/.

Other pages

  About – /about/

  ontact – /contact/

  Custom 404 – triggers automatically for non‑existent pages.
  Custom Template Tags & Filters
The project includes several custom template tags/filters located in articles/templatetags/magazine_extras.py:

  {{ text|markdown_to_html }} – converts Markdown to safe HTML.

  {{ text|truncate_chars:100 }} – truncates text to a given number of characters.

  {% latest_articles 5 %} – displays a list of the 5 most recent published articles (reusable partial).
