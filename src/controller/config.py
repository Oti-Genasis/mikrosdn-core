import os

ROUTEROS_DEFAULT_API_PORT = int(os.getenv("ROUTEROS_API_PORT", 8729)) # default API port for RouterOS
DB_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/mikrosdn") # default database URL
ROUTEROS_API_TIMEOUT = int(os.getenv("ROUTEROS_API_TIMEOUT", 10))  # in seconds
ROUTEROS_API_RETRIES = int(os.getenv("ROUTEROS_API_RETRIES", 3))  # number of retries for API calls
ROUTEROS_API_RETRY_DELAY = int(os.getenv("ROUTEROS_API_RETRY_DELAY", 2))  # delay between retries in seconds
ROUTEROS_API_DEFAULT_USERNAME = os.getenv("ROUTEROS_API_USERNAME", "admin") # default username for RouterOS API
ROUTEROS_API_DEFAULT_PASSWORD = os.getenv("ROUTEROS_API_PASSWORD", "pass") # default password for RouterOS API
ROUTEROS_API_SSL = os.getenv("ROUTEROS_API_SSL", "false").lower() # use SSL for RouterOS API
