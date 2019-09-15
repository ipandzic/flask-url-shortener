from url_shortener import create_app
from url_shortener.extensions import db

print("Creating tables")

db.create_all(app=create_app())
