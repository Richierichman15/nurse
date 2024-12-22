from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URL = "postgresql://gitonga-nyaga:Mailman03!@localhost:5432/nurse_db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Request(Base):
    __tablename__ = 'requests'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False) 
    description = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
