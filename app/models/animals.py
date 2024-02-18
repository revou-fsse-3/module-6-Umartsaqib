from app.utils.database import db

class Animals(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  age = db.Column(db.Integer, nullable=True)
  type = db.Column(db.String(100), nullable=True)
  gender = db.Column(db.String(100), nullable=True)

  def as_dict(self):
    return {
          "id": self.id,
          "name": self.name,
          "age": self.age,
          "type": self.type,
          "gender": self.gender
          }