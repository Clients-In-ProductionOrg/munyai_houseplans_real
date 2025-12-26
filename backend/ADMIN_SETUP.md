# Django Admin Panel Setup Guide

## ✅ Completed Setup Steps

### 1. Virtual Environment
- Created Python virtual environment at `backend/venv`
- Activated and installed all dependencies

### 2. Django Installation & Configuration
- Django 6.0 installed
- Default authentication system enabled
- Admin panel configured at `/admin` URL
- Database migrations applied successfully

### 3. Database Setup
- Using SQLite for development (`db.sqlite3`)
- All authentication, user, and permission tables created:
  - `auth_user` - User accounts
  - `auth_permission` - Permissions
  - `auth_group` - User groups
  - `admin_logentry` - Admin activity logs
  - `django_session` - Session management

### 4. Superuser Account Created
**Admin Credentials:**
- **Username:** `admin`
- **Password:** `admin123`
- **Email:** `admin@cedric.com`

### 5. Server Running
- Development server: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

---

## 🔐 Security Features Implemented

✅ **Authentication Enabled**
- Built-in Django authentication system active
- Password hashing using PBKDF2
- Session-based authentication

✅ **Admin Restriction**
- Only staff/superuser accounts can access admin panel
- Normal users blocked from admin area
- Authentication required for all admin operations

✅ **Security Settings**
- `CSRF_COOKIE_HTTPONLY = True` - Protect CSRF tokens
- `SESSION_COOKIE_HTTPONLY = True` - Prevent JavaScript access to session cookies
- `SESSION_COOKIE_SECURE = False` (development) - Change to `True` for HTTPS in production

---

## 📊 Registered Models in Admin

The following models are registered and manageable through the admin panel:

### Core App Models
- **HousePlan** - House plan templates with pricing and details
- **BuiltHome** - Completed home projects
- **Contact** - Customer contact information
- **Quote** - Customer quotes/inquiries

### Auth Models (Built-in)
- **Users** - User accounts with staff/superuser status
- **Groups** - User group permissions
- **Permissions** - System permissions

---

## 🚀 How to Use Admin Panel

### Access the Admin
1. Open browser: `http://127.0.0.1:8000/admin/`
2. Login with:
   - Username: `admin`
   - Password: `admin123`

### Manage Records
From the admin dashboard, you can:
- **Create** new records for all registered models
- **Update** existing records
- **Delete** records
- **Bulk actions** on multiple records
- **Search & Filter** records by various fields

### Create Additional Admin Accounts
```python
from django.contrib.auth.models import User
User.objects.create_superuser('newadmin', 'email@example.com', 'password')
```

---

## 🗄️ Database Connection

### Development (Current)
- **Engine:** SQLite
- **File:** `backend/db.sqlite3`
- **No configuration needed** - works out of the box

### Production with Supabase
To switch to PostgreSQL (Supabase), update `.env`:

```env
USE_SQLITE=False
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your-project.supabase.co
DB_PORT=5432
```

Then run migrations:
```bash
python manage.py migrate
```

---

## 📝 Installed Packages

```
Django==6.0
djangorestframework==3.16.1
django-cors-headers==4.9.0
psycopg2-binary==2.9.11 (PostgreSQL driver)
python-decouple==3.8 (Environment variables)
Pillow==12.0.0 (Image handling)
```

---

## 🔍 Verification Checklist

- ✅ Virtual environment created and activated
- ✅ Django configured with admin panel
- ✅ Database migrations applied
- ✅ Superuser account created (admin/admin123)
- ✅ Admin access restricted to staff/superuser
- ✅ Models registered in admin
- ✅ Development server running on port 8000
- ✅ Admin login page accessible

---

## ⚙️ Common Commands

```bash
# Activate virtual environment
cd backend
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # Linux/Mac

# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create new superuser
python manage.py createsuperuser

# Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

---

## 🔗 Configuration Files

- **Settings:** `cedric_admin/settings.py`
- **URLs:** `cedric_admin/urls.py`
- **Admin Config:** `core/admin.py`
- **Models:** `core/models.py`
- **Environment:** `.env`

---

## 📞 Support

For issues or configuration changes, refer to:
- Django Admin Documentation: https://docs.djangoproject.com/en/6.0/ref/contrib/admin/
- Django Authentication: https://docs.djangoproject.com/en/6.0/topics/auth/
