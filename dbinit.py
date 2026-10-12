#!/usr/bin/env python3

# typically done in interactive shell at project root
# executing this script in root directory also have same effect
from app import app, db
with app.app_context():
  db.create_all()
