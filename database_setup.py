from project import db


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(500))


class Phone(db.Model):
    __tablename__ = 'phone'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    specs = db.Column(db.String(500))
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer, db.CheckConstraint('rating<=100'))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship(Company)


if __name__ == '__main__':
    db.create_all()
