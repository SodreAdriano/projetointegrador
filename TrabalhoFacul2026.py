class CadastroVeiculo:

    def __init__(self, nome_motorista, modelo, placa, ano, cor):
        self.nome_motorista = nome_motorista
        self.modelo = modelo
        self.placa = placa
        self.ano = int(ano)
        self.cor = cor

    def verificar_vencimento(self, ano_atual=2026):
        """Verifica se o veículo tem mais de 4 anos de uso e gera um alerta."""
        idade_carro = ano_atual - self.ano

        print(f"\nMotorista: {self.nome_motorista}")
        print(f"Veículo: {self.modelo} | Placa: {self.placa} | Ano: {self.ano}")

        if idade_carro > 4:
            print(
                f"⚠️  ALERTA: Este veículo tem {idade_carro} anos de uso e VENCEU o limite estipulado!"
            )
        else:
            print(
                f"✅ Status: Veículo regularizado ({idade_carro} anos de uso)."
            )
        print("-" * 50)


# Banco de dados temporário (Lista)
banco_de_dados = []

# Alguns dados iniciais para o sistema não começar vazio
banco_de_dados.append(
    CadastroVeiculo("Carlos Silva", "Yamaha Neo 125", "ABC-1234", 2021, "Preto")
)
banco_de_dados.append(
    CadastroVeiculo("Ana Souza", "Chevrolet Onix", "XYZ-5678", 2023, "Prata")
)

# Loop principal do sistema
while True:
    print("\n==================================================")
    print("      SISTEMA DE GESTÃO DE FROTA (2026)           ")
    print("==================================================")
    print("[1] Cadastrar Veículo Novo")
    print("[2] Listar Veículos e Verificar Alertas")
    print("[3] Sair do Sistema")
    print("==================================================")

    opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()

    if opcao == "1":
        print("\n--- TELA DE CADASTRO ---")
        nome = input("Nome completo do motorista: ")
        modelo = input("Modelo do carro/moto: ")
        placa = input("Placa do veículo: ")
        ano = input("Ano do veículo (ex: 2022): ")
        cor = input("Cor do veículo: ")

        # Validação simples para garantir que o ano seja um número
        try:
            # Cria o novo objeto com os dados digitados e adiciona na lista
            novo_veiculo = CadastroVeiculo(nome, modelo, placa, ano, cor)
            banco_de_dados.append(novo_veiculo)
            print("\n✅ Veículo cadastrado com sucesso!")
        except ValueError:
            print("\n❌ Erro: O ano do veículo precisa ser um número válido.")

    elif opcao == "2":
        print("\n==================================================")
        print("          RELATÓRIO DE MONITORAMENTO              ")
        print("==================================================")

        if not banco_de_dados:
            print("Nenhum veículo cadastrado no sistema.")
        else:
            for veiculo in banco_de_dados:
                veiculo.verificar_vencimento()

        input("\nPressione ENTER para voltar ao menu principal...")

    elif opcao == "3":
        print("\nSaindo do sistema... Até logo!")
        break

    else:
        print("\n❌ Opção inválida! Por favor, escolha 1, 2 ou 3.")


# ---------------------------------------------------------
# Simulando o Armazenamento e Testes (Banco de Dados Local)
# ---------------------------------------------------------

# Lista que vai funcionar como o nosso banco de dados
banco_de_dados = []

# 1. Cadastrando um veículo que vai gerar ALERTA (Ano 2021 -> 5 anos de uso em 2026)
carro_antigo = CadastroVeiculo(
    nome_motorista="Carlos Silva",
    modelo="Yamaha Neo 125",
    placa="ABC-1234",
    ano=2021,
    cor=f"Preto",
)
banco_de_dados.append(carro_antigo)

# 2. Cadastrando um veículo REGULAR (Ano 2023 -> 3 anos de uso em 2026)
carro_novo = CadastroVeiculo(
    nome_motorista="Ana Souza",
    modelo="Chevrolet Onix",
    placa="XYZ-5678",
    ano=2023,
    cor="Prata",
)
banco_de_dados.append(carro_novo)

# 3. Executando a varredura no sistema para checar as condições
print("=== INICIANDO SISTEMA DE MONITORAMENTO DE FROTA (2026) ===")

for veiculo in banco_de_dados:
    veiculo.verificar_vencimento()