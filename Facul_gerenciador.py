import os
from colorama import Fore, init

init(autoreset=True)


eventos = [{
    "nome": "code & future",
    "data": "15/08/2026",
    "descricao": "Um mega evento de todas as areas da tecnologia",
    "vagas": 3000
}]


inscricoes = {}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input(f"{Fore.YELLOW}\nPressione ENTER para voltar...")


def cadastrar_evento():
    limpar_tela()
    print(f"{Fore.MAGENTA}=== CADASTRO DE EVENTOS ===")
    listar_eventos(simples=True)

    nome = input("Nome do Evento: ")
    data = input("Data do Evento: ")
    descricao = input("Descrição: ")
    try:
        vagas = int(input("Número máximo de participantes: "))
    except ValueError:
        print(f"{Fore.RED}Digite apenas números para vagas!")
        pausar()
        return

    evento = {"nome": nome, "data": data, "descricao": descricao, "vagas": vagas}
    eventos.append(evento)
    inscricoes[nome] = []
    print(f"{Fore.GREEN}Evento '{nome}' cadastrado com sucesso!")
    pausar()

def atualizar_evento():
    limpar_tela()
    print(f"{Fore.MAGENTA}=== ATUALIZAR EVENTO ===")
    listar_eventos(simples=True)
    nome = input("Digite o nome do evento para atualizar: ")

    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            data = input("Nova Data: ")
            vagas = input("Novo nº de vagas: ")

            if data:
                evento["data"] = data
            if vagas:
                try:
                    evento["vagas"] = int(vagas)
                except ValueError:
                    print(f"{Fore.RED}Número inválido!")
                    pausar()
                    return

            print(f"{Fore.GREEN}Evento '{evento['nome']}' Atualizado com Sucesso!")
            pausar()
            return
    print(f"{Fore.RED}Evento não encontrado!")
    pausar()

def ver_inscritos():
    limpar_tela()
    print(f"{Fore.MAGENTA}=== LISTA DE INSCRITOS ===")
    listar_eventos(simples=True)
    nome = input("Digite o nome do evento: ")

    evento = next((e for e in eventos if e["nome"].lower() == nome.lower()), None)
    if not evento:
        print(f"{Fore.RED}Evento não encontrado!")
        pausar()
        return

    participantes = inscricoes.get(evento["nome"], [])
    if participantes:
        print(f"{Fore.GREEN}Participantes no evento '{evento['nome']}':")
        for aluno in participantes:
            print(f"- {aluno}")
    else:
        print(f"{Fore.YELLOW}Nenhum participante inscrito.")
    pausar()

def excluir_evento():
    limpar_tela()
    print(f"{Fore.MAGENTA}=== EXCLUIR EVENTO ===")
    listar_eventos(simples=True)
    nome = input("\nDigite o nome do evento para excluir: ")

    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            eventos.remove(evento)
            inscricoes.pop(evento["nome"], None)
            print(f"{Fore.GREEN}Evento '{nome}' excluído com sucesso!")
            pausar()
            return
    print(f"{Fore.RED}Evento não encontrado!")
    pausar()


def listar_eventos(simples=False):
    if not eventos:
        print(f"{Fore.RED}Nenhum evento cadastrado.")
    else:
        print(f"{Fore.CYAN}\nEventos disponíveis:")
        for evento in eventos:
            vagas_restantes = evento["vagas"] - len(inscricoes.get(evento["nome"], []))
            linha = f"- {evento['nome']} | Data: {evento['data']} | Vagas: {vagas_restantes}"
            if not simples:
                linha += f" | Descrição: {evento['descricao']}"
            print(Fore.WHITE + linha)



def inscrever_aluno():
    limpar_tela()
    print(f"{Fore.MAGENTA}=== INSCRIÇÃO EM EVENTOS ===")
    listar_eventos()
    nome_evento = input("\nDigite o nome do evento para se inscrever: ")

    
    evento = next((e for e in eventos if e["nome"].lower() == nome_evento.lower()), None)
    if not evento:
        print(f"{Fore.RED}Evento não encontrado!")
        pausar()
        return

    
    lista = inscricoes.setdefault(evento["nome"], [])

    vagas_restantes = evento["vagas"] - len(lista)
    if vagas_restantes <= 0:
        print(f"{Fore.RED}Não há mais vagas disponíveis!")
        pausar()
        return

    participante = input("Digite seu nome: ")
    if participante in lista:
        print(f"{Fore.YELLOW}Você já está inscrito nesse evento!")
    else:
        lista.append(participante)
        print(f"{Fore.GREEN}{participante} inscrito com sucesso no evento '{evento['nome']}'!")
    pausar()


def menu_aluno():
    while True:
        limpar_tela()
        print(f"{Fore.BLUE}====== MENU DO ALUNO ======")
        print("1 - Lista eventos")
        print("2 - Inscrever-se em evento")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            limpar_tela()
            listar_eventos()
            pausar()
        elif opcao == "2":
            inscrever_aluno()
        elif opcao == "0":
            break
        else:
            print(f"{Fore.RED}Opção inválida!")
            pausar()

def menu_coordenador():
    while True:
        limpar_tela()
        print(f"{Fore.BLUE}====== MENU DO COORDENADOR ======")
        print("1 - Cadastrar evento")
        print("2 - Atualizar evento")
        print("3 - Listar eventos")
        print("4 - Ver inscritos")
        print("5 - Excluir evento")
        print("0 - Voltar")
        opcao = input("\nEscolha: ")

        if opcao == "1":
            cadastrar_evento()
        elif opcao == "2":
            atualizar_evento()
        elif opcao == "3":
            limpar_tela()
            listar_eventos()
            pausar()
        elif opcao == "4":
            ver_inscritos()
        elif opcao == "5":
            excluir_evento()
        elif opcao == "0":
            break
        else:
            print(f"{Fore.RED}Opção inválida!")
            pausar()

def menu_principal():
    while True:
        limpar_tela()
        print(f"{Fore.MAGENTA}====== SISTEMA DE EVENTOS UNIFECAF ======")
        print("1 - Aluno")
        print("2 - Coordenador")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            menu_aluno()
        elif opcao == "2":
            menu_coordenador()
        elif opcao == "0":
            print(f"{Fore.GREEN}Saindo do sistema...")
            break
        else:
            print(f"{Fore.RED}Opção inválida!")
            pausar()


menu_principal()
