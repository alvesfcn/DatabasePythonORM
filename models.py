from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base

class Email(Base):
 
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer,ForeignKey ("usuarios.id"))
    email = Column(String)

class Senha(Base):  
  
    __tablename__ = "senhas"
    
    id = Column(Integer, primary_key=Tru)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    senha = Column(Integer) 

class Usuario(Base):
 
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = relationship("Mail", uselist=False, backref="usuarios")
    senha = relationship("Senha", uselist=False, backref="usuarios")



