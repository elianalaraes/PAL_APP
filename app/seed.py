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
        role="Admin",
        id_number = 230740851
    )
    db.session.add(admin)
    db.session.commit()

    # Tutor
    student = User(
        email="pal.student@ncl.ac.uk",
        password="password123",
        name="Anna Li",
        role="Student",
        id_number=230740855
    )
    db.session.add(student)
    db.session.commit()
