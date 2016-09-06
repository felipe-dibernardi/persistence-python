# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "felipe"
__date__ = "$Sep 6, 2016 11:14:04 AM$"

import database
import datetime
from database import User
from database import Company
from database import Project

if __name__ == "__main__":
    
    database.Base.metadata.create_all(database.engine)
    
    date_converter = '%Y-%m-%d %H:%M:%S'
    
    now = datetime.datetime.now()
    
    empresa = Company(fantasy_name="Empresa", document="0123456789")
    
    database.insert(empresa)
    
    empresa.users = [
    User(name="Felipe Di Bernardi S Thiago", username="felipe", password="#felipe#", age=28),
    User(name="Chayanne Antunes Felix", username="chay", password="#chay#", age=26),
    User(name="Daniela Di Bernardi", username="dani", password="#dani#", age=48),
    User(name="Eduardo Di Bernardi S Thiago", username="dudu", password="#dudu#", age=14),
    User(name="Luiza Di Bernardi S Thiago", username="luiza", password="#luiza#", age=19)]
    
    empresa.projects = [
    Project(name="ProjetoUm", start_date=now.strftime(date_converter)), 
    Project(name="ProjetoDois", start_date=now.strftime(date_converter))
    ]

    database.update(empresa)
    
    empresa.projects[0].team = [database.find(User, 1), database.find(User, 2)]
    empresa.projects[1].team = [database.find(User, 3), database.find(User, 4), database.find(User, 5)]
    
    database.update(empresa.projects[0])
    database.update(empresa.projects[1])
    
    database.list_all(Company)
    
    database.list_all(User)
    
    database.list_all(Projects)
