# Restaurant Kitchen Service

A Django-based web application for managing dishes, ingredients, dish types, and cooks in a restaurant kitchen.

## Database Structure

The database includes four main entities:

- **DishType** — category of a dish.
- **Dish** — main model describing dishes with name, description, price, type, ingredients, and assigned cooks.
- **Cook** — custom user model based on `AbstractUser`, extended with `years_of_experience`.
- **Ingredient** — ingredient used in dishes.

## DB Schema

![Database Schema](static/images/kitchen_service_db.jpg)

## Demo

![Main Page](static/images/kitchen_service_main_page.jpg)

## Features

- Authentication system based on Django auth
- Custom user model: `Cook`
- Create, read, update, and delete functionality for:
  - cooks
  - dishes
  - dish types
  - ingredients
- Assign cooks to dishes
- Add ingredients to dishes
- Search functionality on list pages
- Pagination for convenient browsing through large amounts of data
- Admin panel for database management
- Fixture support with demo data via `kitchen_data.json`
- Styled homepage dashboard with project statistics

## Technologies Used

- **Backend:** Python, Django, Django ORM
- **Frontend:** HTML5, CSS3, Django Templates, Bootstrap 5
- **Database:** SQLite3

## Getting Started

These instructions will help you set up the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/Livan94/-restaurant-kitchen-service.git
cd -restaurant-kitchen-service
```

### 2. Create and activate virtual environment

#### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

### 3. Create `.env` file

Create your local `.env` file based on `.env.example`.

#### Linux / macOS

```bash
cp .env.example .env
```

#### Windows

```bash
copy .env.example .env
```

The `.env.example` file contains:

```env
# True for local development, False for production-like local check
DEBUG=True

# Django secret key for local development
SECRET_KEY=your-secret-key-here

# Comma-separated hosts
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

This project expects each user to create a local superuser manually before loading fixture data.

```bash
python manage.py createsuperuser
```

### 7. Load demo data

After creating the superuser, load the prepared fixture:

```bash
python manage.py loaddata kitchen_data.json
```

> **Important:**  
> The fixture file does not provide a ready-to-use admin password.  
> The admin account should be created locally with `createsuperuser`.

### 8. Run the development server

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

## Local setup with `DEBUG=False` (optional)

By default, the project is intended to run locally with:

```env
DEBUG=True
```

If you want to fully disable debug mode, open your `.env` file and change:

```env
DEBUG=False
```

You should also make sure that `ALLOWED_HOSTS` contains the local addresses you use:

```env
ALLOWED_HOSTS=127.0.0.1,localhost
```

Then run the project with the usual commands:

```bash
python manage.py migrate
python manage.py runserver
```

> **Note:**  
> Running the project with `DEBUG=False` is optional and intended as a production-like local check.  
> In this mode, additional configuration may be required for static files and deployment-related settings.  
> For standard local development, it is recommended to keep `DEBUG=True`.  

## Demo Data

The project includes a `kitchen_data.json` fixture file with enough sample records to demonstrate:

- pagination
- search
- list views
- many-to-many relationships
- dashboard statistics

The fixture contains sample:
- dish types
- ingredients
- cooks
- dishes

## Usage

After launching the project, you can:

- log in with your superuser account
- browse dishes, cooks, ingredients, and dish types
- search records on list pages
- view paginated results
- manage records through the web interface
- use the Django admin panel for advanced data management

## Author

Developed as a study project for practicing Django, database modeling, authentication, class-based views, and frontend integration.