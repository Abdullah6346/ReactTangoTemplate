# Full Stack Framework: TanStack Router + Django

This project is a modern full stack framework combining a powerful React frontend (using TanStack Router) with a robust Django backend. It is designed for rapid development, scalability, and maintainability.

## Features

- **Frontend:** React with TanStack Router for advanced routing and modern UI development
- **Backend:** Django for RESTful APIs, authentication, and business logic
- **TypeScript:** Type safety for frontend code
- **Vite:** Fast frontend build tool
- **Docker:** Containerized development and deployment

## Project Structure

```
/ (root)
├── api/                  # Django api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── welcome/
│   │   ├── __init__.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── __pycache__/
│   │   └── models/
│   │       ├── __init__.py
│   │       └── welcome.py
│   └── __pycache__/
├── app/                  # React app (TanStack Router)
│   ├── app.css
│   ├── root.tsx
│   ├── routes.ts
│   ├── routes/
│   │   └── home.tsx
│   └── welcome/
│       ├── logo-dark.svg
│       ├── logo-light.svg
│       └── welcome.tsx
├── config/               # Django config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── public/               # Static assets
│   └── favicon.ico
├── db.sqlite3
├── Dockerfile
├── install.js
├── manage.py
├── package.json
├── pnpm-lock.yaml
├── react-router.config.ts
├── requirements.txt
├── tsconfig.json
├── vite.config.ts
└── README.md
```

## Getting Started

### Backend (Django)

1. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Frontend (React + TanStack Router)

1. Install Node dependencies:
   ```sh
   pnpm install
   ```

### Simple RUN

1. Run this:
   ```sh
   pnpm run dev
   ```

### Docker (optional)

Build and run the full stack app in containers:

```sh
docker build -t my-framework .
docker run -p 8000:8000 my-framework
```

## License

MIT
