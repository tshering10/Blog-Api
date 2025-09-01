# Django Blog API

A RESTful API built with Django and Django REST Framework for managing users, profiles, and blog posts.  
The project supports user authentication, nested profile updates, and secure CRUD operations for posts.

## Features

### User & Authentication

- User registration, login, logout
- JWT / token-based authentication
- Automatic profile creation on registration
- Users can update their own profile

### Profiles

- View all user profiles
- Retrieve, update, or delete own profile
- Update nested user info via profile endpoint
- Permissions: only owners can edit/delete their profiles

### Blog Posts

- Create, read, update, delete posts
- Posts auto-assigned to the logged-in user as author
- Only the author can edit/delete their own posts
- Others can view posts (read-only)

### Permissions

- **IsOwnerOrReadOnly** ensures only authors can modify posts or profiles  
- **IsAuthenticatedOrReadOnly** allows authenticated users to create posts, others can read

## Models Overview

- **User** (Django default)
- **Profile**
  - `user` (OneToOneField)
  - `bio`
- **Post**
  - `title`
  - `content`
  - `author` (ForeignKey to User)
  - `created_at`, `updated_at`


## API Endpoints

### Profiles

| Method | Endpoint                  | Description                           |
|--------|---------------------------|---------------------------------------|
| GET    | `/api/profile/`          | List all profiles                     |
| GET    | `/api/profile/<id>/`     | Retrieve a specific profile           |
| PATCH  | `/api/profile/<id>`        | Update logged-in user's profile       |
| DELETE | `/api/profile/<id>/` | Delete logged-in user's profile       |

### Setup Instructions
1. Clone the repo
git clone https://github.com/tshering10/Blog-Api.git
cd Blog-Api

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Apply Migrations:
python manage.py migrate

5. Create a superuser (optional):
py manage.py createsuperuser

6. Run development server
py manage.py runserver

