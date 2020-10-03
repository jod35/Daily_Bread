from daily_bread import create_app
from daily_bread.config import DevConfig
import os

config=os.getenv('FLASK_ENV') or DevConfig

app=create_app(config)

if __name__ == "__main__":
    app.run()