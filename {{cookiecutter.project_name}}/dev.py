"""
Runs the application for local development. This file should not be used to start the
application for production.

Refer to https://www.uvicorn.org/deployment/ for production deployments.
"""
import os

import uvicorn
from rich.console import Console

try:
    import uvloop
except ModuleNotFoundError:
    pass
else:
    uvloop.install()

if __name__ == "__main__":
    os.environ["APP_ENV"] = "dev"

    console = Console()
    console.rule("[bold yellow]Running for local development", align="left")
{%- if cookiecutter.use_openapi == "True" %}
    console.print("[bold yellow]Visit http://localhost:8000/docs")
{%- endif %}

    uvicorn.run("app.main:app", host="localhost", lifespan="on", log_level="info", reload=True)
