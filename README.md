#  WatchRoulette — Django Web App

WatchRoulette is a fun, functional Django web application that helps users
manage a watchlist (movies/anime/series) and randomly pick what to watch next
using a roulette-style selector.

This project was built to practice **real-world Django concepts**:
authentication, models, forms, permissions, and clean UX flows.

---

##  Features

- User authentication (login/logout)
- Personal watchlist (Movie / Anime / Series)
- Random “Spin Roulette” picker
- Mark items as watched
- Rate watched items (1–10)
- Secure actions using POST + CSRF
- Clean redirect flow after login

---

##  Tech Stack

- Python
- Django
- SQLite (development)
- HTML (Django templates)

---

##  Project Structure

```text
secure_site/
├── watch/          #  MAIN PROJECT: WatchRoulette
├── accounts/       # Supporting app (auth practice)
├── secure_site/    # Project settings
├── manage.py
├── requirements.txt

Primary focus of this repository is the watch/ app.

```

🚀 Setup & Run Locally
git clone https://github.com/Muhammed-Azif-A-006/django-watchroulette.git
cd django-watchroulette

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Open:

Home → http://127.0.0.1:8000/

WatchRoulette → http://127.0.0.1:8000/watch/

## Login Flow

Visiting / redirects to WatchRoulette

Unauthenticated users are redirected to login

After login, users land directly on WatchRoulette

## Notes

This repository contains additional Django apps created during learning.
They are not the primary focus of this project.

