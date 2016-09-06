# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "felipe"
__date__ = "$Sep 6, 2016 11:20:53 AM$"

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = sqlalchemy.create_engine('mysql+pymysql://python:python@localhost:3306/python_test')
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class Database:
    
    user = ""
    password = ""
    host = ""
    port = ""
    schema = ""
    
    def __init__(self, user, password, host, port, schema):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.schema = schema

project_user_table = Table('project_user', Base.metadata,
                        Column(('projects_id'), Integer, ForeignKey('projects.id')),
                        Column(('users_id'), Integer, ForeignKey('users.id'))
                        )

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    username = Column(String(32), nullable=False)
    password = Column(String(64), nullable=False)
    age = Column(Integer, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    
    company = relationship("Company", back_populates = "users")
    
    def __repr__(self):
        return "Id: {4}, Name: {0}, Age: {1}, Username: {2}, Password: {3}".format(self.name, self.age, self.username, 
    self.password, self.id)

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    
    company = relationship("Company", back_populates = "projects")
    
    team = relationship("User", secondary=project_user_table)
    
    def __repr__(self):
        return "Id: {0}, Name: {1}, Start date: {2}".format(self.id ,self.name, self.start_date)

class Company(Base):
    __tablename__ = 'companies'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fantasy_name = Column(String(64), nullable=False)
    document = Column(String(32), nullable=False)
    users = relationship("User", order_by=User.id, back_populates="company")
    projects = relationship("Project", order_by=Project.id, back_populates="company")
    
    def __repr__(self):
        return "Id: {2}, Name: {0}, Document: {1}".format(self.fantasy_name ,self.document, self.id)

def insert(object):
    try:
        session.add(object)
        session.commit()
    except:
        print "Error while adding " + str(type(object)) + "."
        
def update(object):
    try:
        session.add(object)
        session.commit()
    except:
        print "Error while updating " + str(type(object)) + "."
        

def find(object, id):
    try:
        return session.query(object).filter_by(id=id).one()
    except:
        print "Error while retrieving " + str(type(object)) + "."

def delete(object, id):
    try:
        obj = session.query(object).filter_by(id=id).one()
        session.delete(obj)
        session.commit()
    except:
        print "Error while deleting " + str(type(object)) + "."
    
    
def list_all(object):
    try:
        objects = session.query(object).all()
        for obj in objects:
            print obj
    except:
        print "Error while listing " + str(type(object)) + "."
        

        
