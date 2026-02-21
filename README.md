# Healthcare Backend API

A Django REST Framework backend for a healthcare application with patient and doctor management.

## Features

- User authentication with JWT tokens
- Patient management (CRUD)
- Doctor management (CRUD)
- Patient-Doctor mapping and assignment
- Validation and error handling
- Swagger API documentation

## Setup

### Prerequisites
- Python 3.9+
- PostgreSQL
- Virtual environment

### Installation

1. Clone the repository and navigate to the project:
```bash
cd health-be
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables in `.env`:
```
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Start the server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login and get JWT token

### Patients
- `GET /api/patients/` - List user's patients
- `POST /api/patients/` - Create new patient
- `GET /api/patients/{id}/` - Get patient details
- `PUT /api/patients/{id}/` - Update patient
- `DELETE /api/patients/{id}/` - Delete patient

### Doctors
- `GET /api/doctors/` - List all doctors
- `POST /api/doctors/` - Create new doctor
- `GET /api/doctors/{id}/` - Get doctor details
- `PUT /api/doctors/{id}/` - Update doctor
- `DELETE /api/doctors/{id}/` - Delete doctor

### Mappings
- `GET /api/mappings/` - List patient-doctor mappings
- `POST /api/mappings/` - Assign doctor to patient
- `GET /api/mappings/patient/{id}/` - Get doctors for patient
- `DELETE /api/mappings/{id}/` - Remove assignment

## Documentation

- Swagger: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`
