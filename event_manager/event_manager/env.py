"""
env.py
https://django-environ.readthedocs.io/en/latest/quickstart.html
"""
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()