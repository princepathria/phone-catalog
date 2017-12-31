import os
pwd = os.getcwd()
os.chdir("..")
from database_setup import db, Company, Phone
os.chdir(pwd)


p = Company.query.filter_by(name='Apple').one()
p.name = 'apple'
db.session.add(p)
db.session.commit()
