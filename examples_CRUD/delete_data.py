import os
pwd = os.getcwd()
os.chdir("..")
from database_setup import db, Company, Phone
os.chdir(pwd)


p = Company.query.filter_by(name='Apple').one()
# q = Phone.query.filter_by(company_id=p.id).all()
# db.session.delete(q)
db.session.delete(p)
db.session.commit()
