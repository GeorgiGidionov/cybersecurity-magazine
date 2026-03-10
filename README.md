Cybersecurity Magazine is a full-featured Django web application built 
as an educational project. It simulates an online magazine focused on 
cybersecurity, offering articles, a product store, and subscription plans – 
all without user authentication (as per project requirements).

Three Django apps with clear responsibilities:

        articles – manage magazine articles, authors, categories and tags.

        store – handle cybersecurity products and customer orders.

        subscriptions – manage subscription plans and signups.

    Database models with relationships:

        Article → Category (many‑to‑one)

        Article → Author (many‑to‑one)

        Article ↔ Tag (many‑to‑many)

        Order → Product (many‑to‑one)

    Full CRUD for Article and Product models.

    10+ dynamic templates built with Django Template Language and Bootstrap 5:

        Home page with featured articles and latest products.

        Article list (filterable by search, sortable by date), detail, create, edit, delete.

        Product list (sortable by price/newest), detail, create, edit, delete, order form.

        Subscription plans list and signup form.

        About, Contact, and custom 404 error page.

    Forms with validations:

        Article, Product, Order, Subscription forms.

        Read‑only/disabled fields (e.g., published article status).

        User‑friendly error messages, help texts, placeholders.

        Confirmation step before deletion (Django’s DeleteView).

    Custom template tags/filters:

        markdown_to_html – render Markdown content.

        truncate_chars – truncate text by character count.

        latest_articles – inclusion tag to display recent articles.

    PostgreSQL database backend.

    Fully responsive design using Bootstrap 5.

    No authentication – all features are publicly accessible, meeting the assignment criteria.

Technologies Used

    Backend: Django 6.0.2, Python 3.13

    Database: PostgreSQL 16

    Frontend: HTML5, CSS3, Bootstrap 5, JavaScript (minimal)

    Version Control: Git, GitHub

    Additional Libraries:

        markdown – for Markdown rendering in articles

        psycopg2-binary – PostgreSQL adapter

        python-dotenv – environment variables management (optional)
Project Structure
text

cybersecurity-magazine/
├── cybersecurity_magazine/       
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py                  
│   └── wsgi.py
├── articles/                     
│   ├── migrations/
│   ├── templatetags/              
│   │   ├── __init__.py
│   │   └── magazine_extras.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── store/                          
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── subscriptions/                  
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/                      
│   ├── base.html
│   ├── 404.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── articles/
│   │   ├── article_list.html
│   │   ├── article_detail.html
│   │   ├── article_form.html
│   │   └── article_confirm_delete.html
│   ├── store/
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   ├── product_form.html
│   │   ├── product_confirm_delete.html
│   │   ├── order_form.html
│   │   └── order_success.html
│   └── subscriptions/
│       ├── plan_list.html
│       ├── subscription_form.html
│       └── subscription_success.html
├── static/
│   └── images/                      
│       └── 3043140.jpg
├── media/                            
├── requirements.txt
├── manage.py
├── .venv                     
└── README.md                        

Installation & Setup

Follow these steps to run the project locally.
1. Prerequisites

    Python 3.13 or higher

    PostgreSQL 16

    pip (Python package manager)

    Git

2. Clone the repository
bash

git clone https://github.com/GeorgiGidionov/cybersecurity-magazine.git
cd cybersecurity-magazine

1. Create and activate a virtual environment
bash

python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

1. Install dependencies
bash

pip install -r requirements.txt

1. Configure PostgreSQL

Create a database and user:
SQL

CREATE DATABASE cybersecurity_magazine;
CREATE USER postgres WITH PASSWORD 123456;
GRANT ALL PRIVILEGES ON DATABASE cybersecurity_magazine TO postgres;

1. Set environment variables

Create a .env file in the project root (use .env.example as a template) with the following content:
env

SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=cybersecurity_magazine
DB_USER=postgres
DB_PASSWORD=123456
DB_HOST=127.0.0.1
DB_PORT=5432

Alternatively, you can hardcode the database credentials in settings.py for local testing, but using a .env file is recommended for security.
1. Apply migrations
bash

python manage.py makemigrations
python manage.py migrate

1. Create a superuser (optional – for admin access)
bash

python manage.py createsuperuser

1. Run the development server
bash

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.
Usage Guide
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

    Subscribe – /subscriptions/subscribe/?plan=<id> (form with date validation; plan is pre‑selected).

    Success page – /subscriptions/success/.

Other pages

    About – /about/

    Contact – /contact/

    Custom 404 – triggers automatically for non‑existent pages (visible when DEBUG=False).

🔧 Custom Template Tags & Filters

The project includes several custom template tags/filters located in articles/templatetags/magazine_extras.py:

    {{ text|markdown_to_html }} – converts Markdown to safe HTML.

    {{ text|truncate_chars:100 }} – truncates text to a given number of characters.

    {% latest_articles 5 %} – displays a list of the 5 most recent published articles (reusable partial).

Usage in templates:
django

{% load magazine_extras %}

<div class="article-content">
    {{ article.content|markdown_to_html }}
</div>

<p>{{ long_text|truncate_chars:150 }}</p>

<div class="sidebar">
    <h3>Последни статии</h3>
    {% latest_articles 5 %}
</div>

Testing (optional)

You can run Django’s built‑in test suite (if any tests are written):
bash

python manage.py test

Deployment Notes

For production deployment, you must:

    Set DEBUG = False in settings.py (or via environment variable).

    Configure ALLOWED_HOSTS with your domain.

    Use a production‑grade web server (Gunicorn, uWSGI) and reverse proxy (Nginx).

    Serve static files with collectstatic:
    bash


Important Notes

    No user authentication is implemented, as required by the original assignment.

    All forms are publicly accessible.

    The database is pre‑configured for PostgreSQL; adjust credentials in .env accordingly.

    The project meets all specified requirements:

         3 Django apps

         3+ database models with many-to-one and many-to-many relationships

         3+ forms with validations, read-only fields, and confirmation on delete

         10+ templates (7+ dynamic)

         Full CRUD for at least 2 models

         Custom template tags/filters

         Custom 404 page

         Bootstrap 5 design

         PostgreSQL database

         GitHub repository with 3+ commits on separate days


