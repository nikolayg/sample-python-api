import os

env = os.environ.get("PYTHON_ENV", "dev")
port = os.environ.get("PORT", 8080)

all_environments = {
    "dev": { "port": 5000, "debug": True, "swagger-url": "/api/swagger" },
    "production": { "port": port, "debug": False, "swagger-url": None  }
}

environment_config = all_environments[env]
