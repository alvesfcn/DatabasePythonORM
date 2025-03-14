from database import SessionLocal
from models import Usuario, Email, Senha
import os
print(os.path.abspath("meubanco.db"))


def atualizar_usuario(usuario_id, novo_nome, email_id=None, novo_email=None, senha_id=None, nova_senha=None):
    db = SessionLocal()  # Criar uma única sessão para todas as operações

    try:
        # Buscar o usuário pelo ID
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

        if usuario:
            usuario.nome = novo_nome  # Atualizar o nome
            print(f"Nome do usuário atualizado para: {usuario.nome}")
        else:
            print(f"Usuário com ID {usuario_id} não encontrado.")

        # Atualizar o email se ambos os parâmetros forem fornecidos
        email = db.query(Email).filter(Email.id == email_id).first()
        if email_id:
            email.endereco = novo_email
            print(f"E-mail atualizado para: {email.endereco}")

        # Atualizar a senha se ambos os parâmetros forem fornecidos
        if senha_id:
            senha = db.query(Senha).filter(Senha.id == senha_id).first()
           # if senha:
            senha.valor = nova_senha  # Supondo que 'valor' seja a coluna da senha
            print(f"Senha atualizada.")

        # 🔥 IMPORTANTE: Confirmar as mudanças no banco de dados
        db.commit()
    
    except Exception as e:
        db.rollback()  # Se der erro, desfaz as mudanças
        print(f"Erro ao atualizar: {e}")

    finally:
        db.close()  # Fechar a conexão

# Atualizar o nome do usuário com ID 1
atualizar_usuario(usuario_id=1, novo_nome="mestre chico",email_id=1, novo_email="amantedelinux@gmail.com", nova_senha="54321")
# Atualizar o nome do usuário com ID 2
atualizar_usuario(usuario_id=2, novo_nome="Maria Atualizada", novo_email="aaaaa@gmail ", nova_senha="novaSenha456")
