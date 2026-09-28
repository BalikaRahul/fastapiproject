from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# declarative_base - This is used to create the Base class for models
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./tasks.db",connect_args={"check_same_thread":False})
# Database_url - 
# connection arguments - A dictionary of arguments
LocalSession = sessionmaker(bind=engine,autoflush=True) # returns a class

Base = declarative_base()