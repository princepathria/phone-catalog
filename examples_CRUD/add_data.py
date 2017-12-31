import os
pwd = os.getcwd()
os.chdir("..")
from database_setup import db, Company, Phone
os.chdir(pwd)

Apple = Company(id='1', name='Apple', desc='''Apple Inc. is an American
 multinational technology company headquartered in Cupertino, California that
 designs, develops, and sells consumer electronics, computer software, and
 online services.''')

db.session.add(Apple)
db.session.commit()
