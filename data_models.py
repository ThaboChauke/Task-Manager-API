from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Create a base class for the models
Base = declarative_base()


# Define the User model for registration
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)  # Store hashed passwords
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"


# Database setup (adjust the connection URL as needed)
DATABASE_URL = "sqlite:///register.db"  # Use SQLite for simplicity; replace with your DB URL

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Create tables

# Session setup
Session = sessionmaker(bind=engine)
session = Session()


# Example: Adding a new user
def register_user(username, email, password_hash):
    new_user = User(username=username, email=email, password_hash=password_hash)
    session.add(new_user)
    session.commit()
    return new_user


# Usage
if __name__ == "__main__":
    user = register_user("testuser", "testuser@example.com", "hashedpassword123")
    print(user)
