from app import db

projeto_user = db.Table("projeto_user",
                        db.Column("projetos_id", db.Integer,
                                  db.ForeignKey("projetos.id")),
                        db.Column('cargo_id', db.Integer,
                                    db.ForeignKey('cargo.id'))
                        )
                        
class projetos(db.Model):
    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    texto = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)
    
class user(db.Model):
    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    
    projetos = db.Column(db.Integer, db.ForeignKey("projetos.id"))
    
class cargo(db.Model):
    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    
