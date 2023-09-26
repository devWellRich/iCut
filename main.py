import datetime

class Usuario:
    def __init__(self, nome, email, telefone, senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha

class Servico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Agendamento:
    def __init__(self, usuario, servico, barbeiro, data, horario, pago=False):
        self.usuario = usuario
        self.servico = servico
        self.barbeiro = barbeiro
        self.data = data
        self.horario = horario
        self.pago = pago

    def realizar_pagamento(self, metodo_pagamento, dados_pagamento):
        if metodo_pagamento == "cartao_credito":
            numero_cartao = dados_pagamento.get("numero_cartao")
            validade_cartao = dados_pagamento.get("validade_cartao")
            cvv_cartao = dados_pagamento.get("cvv_cartao")

            # Verificar e simular o processamento do pagamento com cartão de crédito
            # Simular que o pagamento foi bem-sucedido
            self.pago = True
        elif metodo_pagamento == "pix":
            # Simular a geração de um QR Code para o PIX
            qr_code = "PIX-QR-CODE-12345"

            # Enviar o QR Code para o email do usuário
            print(f"QR Code gerado com sucesso. Verifique o seu email para o pagamento: {self.usuario.email}")

            # Simular que o pagamento foi bem-sucedido após o usuário realizar o PIX
            self.pago = True

class BancoDados:
    def __init__(self):
        self.usuarios = []
        self.servicos = []
        self.agendamentos = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario_por_email(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

    def adicionar_servico(self, servico):
        self.servicos.append(servico)

    def listar_servicos(self):
        return self.servicos

    def agendar_servico(self, agendamento):
        self.agendamentos.append(agendamento)

def menu_principal(banco_dados):
    while True:
        print("\n** Menu Principal **")
        print("1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Listar Serviços")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario(banco_dados)
        elif escolha == "2":
            fazer_login(banco_dados)
        elif escolha == "3":
            listar_servicos(banco_dados)
        elif escolha == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_usuario(banco_dados):
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    senha = input("Senha: ")

    usuario_existente = banco_dados.buscar_usuario_por_email(email)
    if usuario_existente:
        print("Erro: Este e-mail já está cadastrado.")
    else:
        novo_usuario = Usuario(nome, email, telefone, senha)
        banco_dados.adicionar_usuario(novo_usuario)
        print("Usuário cadastrado com sucesso!")

def fazer_login(banco_dados):
    while True:
        email = input("E-mail: ")
        senha = input("Senha: ")

        if email == "0" or senha == "0":
            break  # Voltar ao menu principal

        usuario = banco_dados.buscar_usuario_por_email(email)
        if usuario and usuario.senha == senha:
            print(f"Bem-vindo, {usuario.nome}!")
            agendar_servico(banco_dados, usuario)
            break  # Sai do loop se o login for bem-sucedido
        else:
            print("Erro: E-mail ou senha incorretos. Digite '0' para voltar ao menu principal ou tente novamente.")

def listar_servicos(banco_dados):
    servicos = banco_dados.listar_servicos()
    print("\n** Serviços Disponíveis **")
    for i, servico in enumerate(servicos, start=1):
        print(f"{i}. {servico.nome} - R$ {servico.preco:.2f}")

def listar_barbeiros():
    barbeiros = ["Wellington Richard", "Daniel Camilo", "Tulio Inacio", "Matheus Nogueira", "Leander Tampieri", "Lucas Coimbra", "Victor Santos"]
    print("\n** Barbeiros Disponíveis **")
    for i, barbeiro in enumerate(barbeiros, start=1):
        print(f"{i}. {barbeiro}")

def agendar_servico(banco_dados, usuario):
    servicos_listados = banco_dados.listar_servicos()

    print("\n** Serviços Disponíveis **")
    for i, servico in enumerate(servicos_listados, start=1):
        print(f"{i}. {servico.nome} - R$ {servico.preco:.2f}")

    print("Escolha um serviço pelo número ou digite '0' para voltar ao menu principal.")
    escolha_servico = input("Escolha o serviço pelo número: ")

    if escolha_servico == "0":
        return  # Voltar ao menu principal

    try:
        escolha_servico = int(escolha_servico) - 1
        if escolha_servico < 0 or escolha_servico >= len(servicos_listados):
            print("Opção inválida.")
            return

        listar_barbeiros()

        print("Escolha um barbeiro pelo número.")
        escolha_barbeiro = input("Escolha o barbeiro pelo número: ")

        try:
            escolha_barbeiro = int(escolha_barbeiro) - 1
            barbeiros = ["Wellington Richard", "Daniel Camilo", "Tulio Inacio", "Matheus Nogueira", "Leander Tampieri", "Lucas Coimbra", "Victor Santos"]
            if escolha_barbeiro < 0 or escolha_barbeiro >= len(barbeiros):
                print("Opção inválida.")
                return

            data = input("Data (DD/MM/AAAA): ")
            try:
                data = datetime.datetime.strptime(data, "%d/%m/%Y").date()
            except ValueError:
                print("Erro: Formato de data inválido. Use DD/MM/AAAA.")
                return

            horario = input("Horário: ")
            print(f"Agendando o serviço '{servicos_listados[escolha_servico].nome}' com o barbeiro '{barbeiros[escolha_barbeiro]}'")

            novo_agendamento = Agendamento(usuario, servicos_listados[escolha_servico], barbeiros[escolha_barbeiro], data, horario)
            banco_dados.agendar_servico(novo_agendamento)

            # Opções de pagamento
            print("\n** Opções de Pagamento **")
            print("1. Pagar com Cartão de Crédito")
            print("2. Pagar com PIX")
            print("3. Pagar Presencialmente")
            escolha_pagamento = input("Escolha uma opção de pagamento: ")

            if escolha_pagamento == "1":
                # Pagamento com cartão de crédito
                numero_cartao = input("Número do Cartão de Crédito: ")
                validade_cartao = input("Validade do Cartão de Crédito (MM/AA): ")
                cvv_cartao = input("CVV do Cartão de Crédito: ")

                dados_pagamento = {
                    "numero_cartao": numero_cartao,
                    "validade_cartao": validade_cartao,
                    "cvv_cartao": cvv_cartao
                }

                novo_agendamento.realizar_pagamento("cartao_credito", dados_pagamento)
                print("Pagamento com cartão de crédito realizado com sucesso.")
                print("Comprovante de pagamento enviado para o e-mail cadastrado.")
            elif escolha_pagamento == "2":
                # Pagamento com PIX
                print("Gerando QR Code para pagamento PIX...")
                novo_agendamento.realizar_pagamento("pix", {})
            elif escolha_pagamento == "3":
                # Pagamento presencial
                print("Pagamento presencial selecionado. Você pode pagar diretamente na barbearia no horário agendado.")
            else:
                print("Opção de pagamento inválida.")
                return

            print("Agendamento realizado com sucesso!")

        except ValueError:
            print("Opção inválida. Digite um número válido.")

    except ValueError:
        print("Opção inválida. Digite um número válido.")

if __name__ == "__main__":
    banco_dados = BancoDados()

    # Exemplo: Adicionar serviços
    banco_dados.adicionar_servico(Servico("Corte de Cabelo", 30.0))
    banco_dados.adicionar_servico(Servico("Barba", 15.0))
    banco_dados.adicionar_servico(Servico("Pacote Completo", 40.0))

    menu_principal(banco_dados)
