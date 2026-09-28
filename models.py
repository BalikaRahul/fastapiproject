from database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey

# create table tablename (col datatypes );
# to create a column in ORM we create a col object using Column
# default, notnull, unique, check, primaryKey, autoincrement
class Candidates_registation(Base):
    __tablename__="Candidates_registation"
    candidate_id = Column(Integer,primary_key=True,autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String(10),unique=True)
    email = Column(String,unique=True)
    city = Column(String)
    graduation_year = Column(Integer)
    skill = Column(String)
    password = Column(String)

class Job_applications(Base):
    __tablename__ = 'Job_applications'
    application_id = Column(Integer,primary_key=True,autoincrement=True)
    candidate_id = Column(Integer,ForeignKey("Candidates_registation.candidate_id"),nullable=False)
    job_id = Column(Integer,ForeignKey('job.job_id'))
    status = Column(Boolean,default='applied')

class Job(Base):
    __tablename__='Job'
    job_id = Column(Integer,primary_key=True,autoincrement=True)
    company_name = Column(String)
    role = Column(String)
    required_experience = Column(Integer)
    ctc = Column(Integer)
    skills = Column(String,nullable=False)
    bond = Column(Boolean,default=False)
    