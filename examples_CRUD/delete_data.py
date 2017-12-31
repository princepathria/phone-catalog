import os
pwd = os.getcwd()
os.chdir("..")
from database_setup import db, Company, Phone
os.chdir(pwd)


p = Company.query.filter_by(name='apple').one()

db.session.delete(p)
db.session.commit()
