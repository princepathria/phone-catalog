import os
pwd = os.getcwd()
os.chdir("..")
from database_setup import db, Company, Phone
os.chdir(pwd)

x = Company.query.all()
y = db.session.query(db.func.count(db.func.distinct(Company.name)))
z = Company.query.first()
p = Company.query.filter_by(name='Apple').first()

print(x[0].name)
print(y)
print(p.desc)
