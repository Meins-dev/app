import sys
import dataclasses

class Usuario:
    def __init__(self, nome_exibicao):
        self.nome_exibicao = nome_exibicao


class ErroAutenticacao(Exception):
    pass


class AuthService:

    def autenticar(self, login: str, senha: str) -> Usuario:

        tabela_usuarios = {
            "meins": {
                "senha": "123456",
                "nome_exibicao": "Meins"
            },
            "usuario2": {
                "senha": "senha2",
                "nome_exibicao": "Usuário 2"
            },
            "usuario3": {
                "senha": "senha3",
                "nome_exibicao": "Usuário 3"
            }

        }

        usuario = tabela_usuarios.get(login)

        if not usuario:
            raise ErroAutenticacao("Login ou senha inválidos.")

        if usuario["senha"] != senha:
            raise ErroAutenticacao("Login ou senha inválidos.")

        return Usuario(
            nome_exibicao=usuario["nome_exibicao"]
        )