import os

ROUTEROS_API_PORT = int(os.getenv("ROUTEROS_API_PORT", 8729))
DB_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/mikrosdn")