from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datasource/catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
    def _fk_pragma(db_con, con_record):
        db_con.execute('pragma foreign_keys=ON')
    event.listen(db.engine, 'connect', _fk_pragma)
