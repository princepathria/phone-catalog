from settings import db

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    discp = db.Column(db.String(500))
    phones = db.relationship('Phone', backref='Phone', lazy=True)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.discp,
        }


class Phone(db.Model):
    __tablename__ = 'phone'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    specs = db.Column(db.String(500))
    price = db.Column(db.Integer)
    rating = db.Column(db.Integer, db.CheckConstraint('rating<=100'))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    company = db.relationship('Company')

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'name': self.name,
            'specification': self.specs,
            'id': self.id,
            'price': self.price,
            'rating': self.rating,
        }


if __name__ == '__main__':
    db.create_all()
