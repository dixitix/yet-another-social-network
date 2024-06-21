from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import bcrypt
import os

Base = declarative_base()

DATABASE_URI = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def create_db():
    Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    email = Column(String)
    phone_number = Column(String)

def add_user(username, password, **kwargs):
    session = Session()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=username, password_hash=hashed_password.decode('utf-8'), **kwargs)
    try:
        session.add(new_user)
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False
    finally:
        session.close()

def update_user(username, **kwargs):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        session.commit()
        session.close()
        return True
    else:
        session.close()
        return False

def authenticate_user(username, password):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        session.close()
        return user
    else:
        session.close()
        return None

def get_id(username):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    session.close()
    return user.id

if __name__ == '__main__':
    create_db()
