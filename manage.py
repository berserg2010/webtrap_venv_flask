#!/usr/bin/env python3
from main import create_app


app = create_app("default")


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv(dotenv_path=".flaskenv")

    app.run(port=os.getenv("FLASK_RUN_PORT", 8888))
