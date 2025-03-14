from database import SessionLocal
from models import Usuario

def excluir_usuario(usuario_id):
    db = SessionLocal()

    usuario =  db.query(Usuario).filter(Usuario.id == usuario_id ).first()
    db.delete(usuario)
    db.commit()
    if usuario:
        print(f"Usuário com id {usuario_id} foi excluido,")
    else:
        print(f"Usuário com id {usuario_id} não encontrado.")

    db.close()
    
excluir_usuario(3)