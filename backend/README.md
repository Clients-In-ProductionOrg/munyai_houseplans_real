# Django Backend - Cedric Admin Project

This is a Django backend for the Cedric website with a fully functional admin panel.

## Project Structure

```
backend/
├── cedric_admin/          # Main project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py          # URL routing
│   ├── wsgi.py          # WSGI application
│   ├── asgi.py          # ASGI application
│   └── __init__.py
├── core/                 # Core application
│   ├── models.py        # Data models (HousePlan, BuiltHome, Contact, Quote)
│   ├── admin.py         # Admin configuration
│   ├── views.py         # API views
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # App URLs
│   └── migrations/      # Database migrations
├── templates/           # Django templates
├── static/             # Static files (CSS, JS)
├── media/              # User-uploaded media
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and fill in your Supabase credentials:

```bash
cp .env.example .env
```

Edit `.env` with your Supabase PostgreSQL connection details:
```
DB_HOST=your-project.supabase.co
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=postgres
SECRET_KEY=your-secret-key
```

### 3. Run Database Migrations

```bash
python manage.py migrate
```

This creates all necessary tables including:
- Django authentication tables (User, Group, Permission)
- Django session tables
- Core app models (HousePlan, BuiltHome, Contact, Quote)

### 4. Create Superuser Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account:
- Username: (your username)
- Email: admin@example.com
- Password: (strong password)

### 5. Start Development Server

```bash
python manage.py runserver
```

The Django server will start at `http://localhost:8000`

### 6. Access Admin Panel

Navigate to: `http://localhost:8000/admin`

Log in with your superuser credentials.

## Admin Panel Features

### Models Available in Admin:
- **House Plans** - Manage house plan listings with prices, bedrooms, bathrooms, and images
- **Built Homes** - Showcase completed projects
- **Contact Messages** - View and manage customer inquiries
- **Quote Requests** - Manage customer quote requests
- **Users** - Manage admin users and permissions

### Security Features

1. **Staff-Only Access**: Only staff and superuser accounts can access the admin panel
2. **Session Management**: Secure session cookies with HTTPONLY flag
3. **CSRF Protection**: CSRF token validation on all forms
4. **PostgreSQL on Supabase**: Secure database hosting with credentials from environment variables

## Admin Actions

Once logged in, admins can:
- Create, read, update, and delete (CRUD) house plans
- Manage built home portfolios
- View and respond to contact inquiries
- Track and process quote requests
- Manage user accounts and permissions
- Customize permissions for staff users

## API Endpoints

- `GET /api/core/plans/` - View all house plans
- `POST /api/core/contacts/` - Submit contact form
- `POST /api/core/quotes/` - Submit quote request
- More endpoints available via Django REST Framework

## Database Migration Notes

Django automatically handles:
- `auth_user` table for authentication
- `auth_permission` table for permissions
- `auth_group` table for user groups
- `django_session` table for session management
- Core app tables for business models

All migrations are tracked and versioned in `core/migrations/`.

## Development Notes

- Debug mode is enabled by default in `.env` (set to False for production)
- CORS is configured to allow requests from frontend on localhost:5173
- Static files are served from `static/` directory
- Media uploads go to `media/` directory

## Security Checklist for Production

- [ ] Set DEBUG=False in .env
- [ ] Change SECRET_KEY to a strong random value
- [ ] Set appropriate ALLOWED_HOSTS
- [ ] Set SESSION_COOKIE_SECURE=True
- [ ] Set CSRF_COOKIE_SECURE=True
- [ ] Configure HTTPS
- [ ] Use strong superuser password
- [ ] Set up proper logging and monitoring
- [ ] Configure database backups
- [ ] Use environment-specific settings

## Troubleshooting

### Migration Issues
```bash
# Create migrations for core app
python manage.py makemigrations core

# Apply migrations
python manage.py migrate
```

### Reset Database (Development Only)
```bash
# Delete all migrations except __init__.py
# Then:
python manage.py migrate --run-syncdb
```

### Admin Access Issues
- Ensure user has `is_staff = True` and `is_superuser = True`
- Check that the user is marked as active
- Clear browser cache and cookies
