from datetime import date
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Tutor
    admin = User(
        email="pal.tutor@ncl.ac.uk",
        password="password123",
        name="Eliana Lara",
        role="Admin"
    )
    db.session.add(admin)
    db.session.commit()