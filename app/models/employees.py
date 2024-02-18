from app.utils.database import db

class Employees(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  gender = db.Column(db.String(100), nullable=True)
  phone = db.Column(db.Integer, nullable=True)
  address = db.Column(db.String(100), nullable=True)

  def as_dict(self):
    return {
          "id": self.id,
          "name": self.name,
          "gender": self.gender,
          "phone": self.phone,
          "address": self.address
          }  