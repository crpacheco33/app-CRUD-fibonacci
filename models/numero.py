from utils.db import db

class Numero(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer)
    
    
    

    def __init__(self, numero):
        self.numero = numero
        
        
        
