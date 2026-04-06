Cybersecurity Magazine is a full‑featured Django web application built as 
part of a Django Advanced exam project. It simulates an online magazine focused on 
cybersecurity, offering articles, a product store, subscription plans, 
user authentication, RESTful API, asynchronous tasks (Celery), and full 
test coverage.

FEATURES:
User system – registration, login, logout, profile editing (extended User model via Profile).
Two user groups – Editors (full CRUD rights) and Customers (view‑only) – defined in the admin site.
Three main apps – articles, store, subscriptions + accounts + api.
CRUD for multiple models – Articles, Products, Categories, Authors, ProductCategories, Comments. 
Advanced database relationships – many‑to‑one and many‑to‑many (Article ↔ Tag, Product ↔ Tag).
RESTful API – endpoints for articles, products, comments using DRF with token authentication.
Asynchronous tasks – email notifications for new comments via Celery + Redis.
Responsive frontend – Bootstrap 5 with custom CSS, fallback images, and dynamic navigation.
Comprehensive tests – 28+ tests covering models, forms, views, and API.
Custom error pages – 404 and 500 (optional).
Production ready – environment variables, WhiteNoise for static files, deployment on Azure.

TECHNOLOGIES
Backend: Django 6.0.2, Django REST Framework, Celery, Redis
Database: PostgreSQL 16
Frontend: HTML5, CSS3, Bootstrap 5, JavaScript
Deployment: Azure App Service (Linux) + Azure Database for PostgreSQL
Version Control: Git, GitHub
Testing: Django test framework (28+ tests)

PREREQUISITES
Python 3.13+
PostgreSQL 16+
Redis (for Celery, optional – can use CELERY_TASK_ALWAYS_EAGER=True)
Git
Microsoft Azure

1.Clone the repository
git clone https://github.com/GeorgiGidionov/cybersecurity-magazine.git
cd cybersecurity-magazine

2.Create and activate virtual environment
python -m venv venv
source venv/bin/activate   -linux/Mac
.\venv\Scripts\activate    - windows

3.Install dependencies
pip install -r requirements.txt

4.Set up environment variables
Create a .env file in the project root

SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=cybersecurity_magazine
DB_USER=postgres
DB_PASSWORD=123456
DB_HOST=localhost
DB_PORT=5432
CELERY_BROKER_URL=redis://localhost:6379/0

5.Configure PostgreSQL
SQL
CREATE DATABASE cybersecurity_magazine;
CREATE USER postgres WITH PASSWORD 123456;
GRANT ALL PRIVILEGES ON DATABASE cybersecurity_magazine TO postgres;

6.Apply migrations
python manage.py migrate

7.Create a superuser (admin)
python manage.py createsuperuser

8.Collect static files (for production)
python manage.py collect static --noinput

9.Run the development server
python manage.py runserver
now visit http://127.0.0.1:8000/.

Tests
python manage.py test --noinput

 API 
 GET	/api/articles/	List all published articles
POST	/api/articles/	Create a new article (authenticated)
GET	/api/articles/{slug}/	Retrieve a single article
PUT	/api/articles/{slug}/	Update an article
DELETE	/api/articles/{slug}/	Delete an article
GET	/api/products/	List all available products
POST	/api/products/	Create a product (authenticated)
GET	/api/comments/	List approved comments
POST	/api/comments/	Add a comment (authenticated)
POST	/api-token-auth/	Obtain authentication token (username+password)

Deployment on Azure

The project is deployed on Azure. You can access it at:  
http://cyberssecuritymagazine-gug6g4djbcfce5fh.switzerlandnorth-01.azurewebsites.net/
