# Little Lemon Restaurant

A full-stack web application for Little Lemon, a family-owned Mediterranean restaurant based in Westlands, Nairobi, Kenya. Built with Django.

## Live Demo

🌍 [littlelemon.pythonanywhere.com](https://littlelemon.pythonanywhere.com)

**Admin Dashboard:** [littlelemon.pythonanywhere.com/dashboard/login](https://littlelemon.pythonanywhere.com/dashboard/login)
- Username: `admin`
- Password: `12345`

## Features

- **Home** — Hero section, weekend special banner, feature cards, chef's special, customer reviews and photo gallery
- **Menu** — Filterable menu grid with food images, categories, prices and featured dish badges
- **About** — Restaurant story, mission statement and values
- **Book a Table** — Reservation form with date, time, guest number and special requests
- **Custom Admin Dashboard** — Protected staff panel to manage reservations and menu items

## Tech Stack

- **Backend** — Python 3.12, Django 6.0
- **Database** — SQLite
- **Frontend** — HTML, CSS (custom), vanilla JavaScript
- **Fonts** — Google Fonts (Markazi Text, Karla)
- **Hosting** — PythonAnywhere

## Setup & Installation

### Prerequisites
- Python 3.12+
- pip

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/charity254/Little-Lemon-Web-App.git
   cd Little-Lemon-Web-App
   ```

2. **Install dependencies**
   ```bash
   pip install django gunicorn --user
   ```

3. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
Little-Lemon-Web-App/
├── littlelemon/          # Project settings and URLs
├── restaurant/           # Main app
│   ├── migrations/       # Database migrations
│   ├── static/           # CSS, images
│   ├── templates/        # HTML templates
│   ├── models.py         # Menu and Booking models
│   ├── views.py          # View functions
│   ├── urls.py           # URL routing
│   ├── forms.py          # Django forms
│   └── admin.py          # Admin configuration
├── requirements.txt
├── Procfile
├── manage.py
└── db.sqlite3
```

## Models

### Menu
| Field | Type | Description |
|-------|------|-------------|
| name | CharField | Item name |
| category | CharField | Starters, Mains, Desserts, Drinks |
| price | DecimalField | Price in KSh |
| menu_item_description | TextField | Item description |
| featured | BooleanField | Featured dish flag |
| image | CharField | Image URL |

### Booking
| Field | Type | Description |
|-------|------|-------------|
| first_name | CharField | Guest first name |
| last_name | CharField | Guest last name |
| date | DateField | Reservation date |
| time | TimeField | Reservation time |
| guest_number | IntegerField | Number of guests |
| special_requests | TextField | Special requests |

## Admin Dashboard

The custom admin dashboard is accessible at `/dashboard/` and requires staff credentials.

Staff can:
- View, add and delete reservations
- View, add, edit and delete menu items

The default Django admin is also available at `/admin/`.

## Deployment on PythonAnywhere

1. Log in to [pythonanywhere.com](https://pythonanywhere.com)
2. Open a Bash console and clone the repo:
   ```bash
   git clone https://github.com/charity254/Little-Lemon-Web-App.git
   ```
3. Install dependencies:
   ```bash
   pip install django gunicorn --user
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Go to **Web** tab → **Add a new web app** → **Manual configuration** → **Python 3.12**
6. Set the source directory to `/home/<username>/Little-Lemon-Web-App`
7. Set the WSGI file to point to `littlelemon.wsgi`
8. Set static files URL to `/restaurant/static/` and directory to `/home/<username>/Little-Lemon-Web-App/restaurant/static`
9. Reload the web app

## License

MIT
