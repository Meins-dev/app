from .usuarios import Usuario, ErroAutenticacao

class AuthService:
    def autenticar(self, login: str, senha: str) -> Usuario:
        # In a real application, this would query a database or external service.
        # For demonstration, we use a hardcoded dictionary.
        tabela_usuarios = {
            "meins": {
                "senha": "123456",
                "nome_exibicao": "Paulo Meins",
                "idade": 18,
                "telefone": "67 99268-7233",
                "foto": "imagens/usuarios/paulo_meins.jpg",  # relative to imagens/usuarios
            },
            "usuario2": {
                "senha": "senha2",
                "nome_exibicao": "Usuário 2",
                "idade": 25,
                "telefone": "11 98765-4321",
                "foto": "/imagens/usuarios/usuario2.jpg",
            },
            "usuario3": {
                "senha": "senha3",
                "nome_exibicao": "Usuário 3",
                "idade": 30,
                "telefone": "21 99999-0000",
                "foto": "/imagens/usuarios/usuario3.jpg",
            },
        }

        usuario_data = tabela_usuarios.get(login)

        if not usuario_data:
            raise ErroAutenticacao("Login ou senha inválidos.")

        if usuario_data["senha"] != senha:
            raise ErroAutenticacao("Login ou senha inválidos.")

        return Usuario(
            nome_exibicao=usuario_data["nome_exibicao"],
            idade=usuario_data["idade"],
            telefone=usuario_data["telefone"],
            foto=usuario_data["foto"],
        )