# Little Lemon Restaurant

A full-stack web application for Little Lemon, a family-owned Mediterranean restaurant based in Westlands, Nairobi, Kenya. Built with Django.

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

## Setup & Installation

### Prerequisites
- Python 3.12+
- pip

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Little-Lemon-Web-App
   ```

2. **Install dependencies**
   ```bash
   pip3 install django --user --break-system-packages
   ```

3. **Apply migrations**
   ```bash
   python3 manage.py migrate
   ```

4. **Create a superuser** (for admin access)
   ```bash
   python3 manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python3 manage.py runserver
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

## Environment Notes

- `DEBUG = True` — set to `False` in production
- `SECRET_KEY` — replace with a secure key in production
- Database — migrate to PostgreSQL for production use

## License

MIT
