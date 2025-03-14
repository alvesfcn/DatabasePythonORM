from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base
class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    usuario_id = Column(Integer,ForeignKey ("usuarios.id"), index=True)
    email = Column(String)

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha = Column(String)

class Senha(Base):  
    __tablename__ = "senhas"

    id = Column(Integer, primary_key=True, index=True)
    senha = Column(Integer) 


