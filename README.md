# Basketball Management System

Welcome to Hoop Proton, a Basketball Management System!

## Features

- Manage multiple teams with individual rosters and schedules.
- Create and edit player profiles and personal information.
- Schedule and manage announcements.
- Interactive whiteboard using Fabric.js for coaches to strategize and plan plays.
- Payment management system for handling player fees.
- Comprehensive CRUD operations for all basketball management tasks.
- Integrated Google Calendar API for managing and sharing game schedules.
- Intuitive user interface based on a responsive Colorlib template.
- Supports user authentication and role-based access control.

## Requirements

- Python 3.8+
- Django 4.0+
- Node.js 14.0+ (for Fabric.js)

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/basketball-management-system.git
```
```
cd basketball-management-system
```



2. Create a virtual environment and activate it:
```
python -m venv venv
```
```
source venv/bin/activate # For Linux/Mac
```
```
venv\Scripts\activate # For Windows
```

3. Install the required packages:
```
pip install django
```
```
pip install -r requirements.txt
```

4. Run migrations:
```
python manage.py migrate
```

5. Collect static files:
```
python manage.py collectstatic
```

6. Install Fabric.js:
```
npm install fabric
```
## Usage

Start the development server:
```
python manage.py runserver
```
Access the application:
Open a web browser and navigate to
```
http://127.0.0.1:8000
```
