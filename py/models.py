from datetime import datetime
from app import db 
class Contato(db.Model):
    __tablename__ = 'contato'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    estado = db.Column(db.String(2), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    comentarios = db.Column(db.String(400))

    def __str__(self):
        return f'{self.id} - {self.nome} - {self.estado} - {self.email} - {self.cidade}- {self.comentarios}'