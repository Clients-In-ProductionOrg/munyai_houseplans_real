#!/usr/bin/env python
"""
Setup script for Cedric Django Admin Panel
This script helps set up the Django environment and create the initial superuser
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, description=""):
    """Execute a shell command and return its status"""
    if description:
        print(f"\n{'='*60}")
        print(f"  {description}")
        print('='*60)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=False)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running command: {e}")
        return False

def check_env_file():
    """Check if .env file exists"""
    env_file = Path('.env')
    if not env_file.exists():
        print("\n⚠️  WARNING: .env file not found!")
        print("Please copy .env.example to .env and configure your database:")
        print("  cp .env.example .env")
        print("\nThen update with your Supabase credentials:")
        print("  - DB_HOST: Your Supabase host")
        print("  - DB_USER: Your database user")
        print("  - DB_PASSWORD: Your database password")
        print("  - DB_NAME: Your database name")
        return False
    return True

def setup_django():
    """Run Django setup commands"""
    print("\n" + "="*60)
    print("  DJANGO ADMIN PANEL SETUP")
    print("="*60)
    
    # Check .env file
    if not check_env_file():
        sys.exit(1)
    
    # Install dependencies
    if not run_command(
        'pip install -r requirements.txt',
        "Step 1: Installing Python dependencies"
    ):
        print("Failed to install requirements!")
        sys.exit(1)
    
    # Run migrations
    if not run_command(
        'python manage.py migrate',
        "Step 2: Running database migrations"
    ):
        print("Failed to run migrations!")
        print("Make sure your database credentials in .env are correct.")
        sys.exit(1)
    
    # Create superuser
    print("\n" + "="*60)
    print("  Step 3: Create Superuser Account")
    print("="*60)
    print("You will be prompted to create an admin account.")
    print("This account will have full access to the admin panel.")
    
    run_command(
        'python manage.py createsuperuser',
        "Creating superuser account"
    )
    
    # Collect static files
    if not run_command(
        'python manage.py collectstatic --noinput',
        "Step 4: Collecting static files"
    ):
        print("Warning: Failed to collect static files (this is OK for development)")
    
    # Print completion message
    from decouple import config
    backend_url = config('BACKEND_URL')
    print("\n" + "="*60)
    print("  SETUP COMPLETE ✓")
    print("="*60)
    print("\nTo start the development server, run:")
    print("  python manage.py runserver")
    print("\nThen access the admin panel at:")
    print(f"  {backend_url}/admin")
    print("\nLog in with the superuser credentials you just created.")
    print("="*60)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    setup_django()
