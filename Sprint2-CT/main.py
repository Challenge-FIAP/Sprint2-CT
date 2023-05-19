from cliente import Cliente
from veiculo import Veiculo
from atendente import atendente

#Com o projeto temos o intuito de usar uma interface semelhante a da Uber para dar aos segurados da Porto, celeridade e otimização no processo de solicitar um Guincho. Com esse sistema poderemos atender não somente aos veículo pesados, mas também a todos os tipos de emergências.
#O solicitante terá a oportunidade de checar pela plataforma, qual veículo está indo ao seu encontro para solucionar o problema em questão. O acompanhamento em tempo real, vai permitir ao segurado saber se o veículo atende as suas necessidades, caso contrário, o mesmo poderá cancelar e realizar um novo chamado com o auxílio de um Chat Bot.
#Na outra ponta, teremos o segurador que em tempo real saberá pelas informações levantes através da solicitação, se é capaz de resolver o problema que está sendo solicitado.
veiculos = []

print("PORTO SEGURO")
print("-----------------------------------------------------------------")
print("Seja bem-vindo!")
cliente1 = Cliente("", "", "")
cliente1.cadastrar_cliente()
resposta = input("Deseja continuar com a solicitação? (sim/não)")


while resposta == "sim":
    print("------------------------------------------------------------------")
    print("1- Solicitar guincho: ")
    print("2- Adionar novo veiculo: ")
    print("3- Consultar veiculos cadastrados: ")
    print("4- Consultar meu cadastro: ")
    print("5- outros:")
    escolha = input("Selecione uma opção: ")
    if escolha == "1":
        if len(veiculos) == 0:
            print(f"{cliente1.nome}Você não possui veiculos cadastrados.")
            escolha2 = (input("Deseja cadastrar? (sim/não)"))
            if escolha2 == "sim":
                veiculo = Veiculo("", "", "", "")
                veiculo.cadastrar_veiculo()
                veiculos.append(veiculo)
            else:
                print("------------------------------------------------------------------")
                print("A Porto Seguro agradece o seu contato.")
                print("------------------------------------------------------------------")
                print("PROGAMA FINALIZADO.") 
                break    
        if veiculo.tipo == "Moto":
            print(f"{cliente1.nome}, um veiculo de reboque está a caminho de você")
            print(f"Nosso especialista {atendente.nome} deverá chegar dentro de 15 minutos.")
        elif veiculo.tipo == "Veículo de passeio":
            print(f"{cliente1.nome}, um guincho pequeno está a caminho de você")
            print(f"Nosso especialista {atendente.nome} deverá chegar dentro de 15 minutos.")
        elif veiculo.tipo == "Veículo de carga leve":
            print(f"{cliente1.nome},um guincho médio está a caminho de você")
            print(f"Nosso especialista {atendente.nome} deverá chegar dentro de 15 minutos.")
        elif veiculo.tipo == "Veículo de carga pesado":
                print(f"{cliente1.nome},um guincho grande está a caminho de você")
                print(f"Nosso especialista {atendente.nome} deverá chegar dentro de 15 minutos.")
        else:
                print("Opção invalida, entre em contato com a central de atendimento.")
    elif escolha == "2":
        veiculo = Veiculo("", "", "", "")
        veiculo.cadastrar_veiculo()
        veiculos.append(veiculo)
    elif escolha == "3":
        for veiculo in veiculos:
            print(f"Modelo: {veiculo.modelo}, Marca: {veiculo.marca}, Placa: {veiculo.placa} Tipo: {veiculo.tipo}")
    elif escolha == "4":
            print(f"Nome completo: {cliente1.nome}")            
            print(f"Login completo: {cliente1.login}")
            print(f"Quantidade de veiculos segurados: {len(veiculos)}")         
    else:
        print("Favor entrar em contato com a central de atendimento.")
        break
    
    print("------------------------------------------------------------------")
    resposta = (input("Gostaria de fazer outra solicitação? (sim/não)"))
    
if resposta != "sim":    
    print("")
    print("A Porto Seguro agradece o seu contato.")
    print("------------------------------------------------------------------")
    print("PROGAMA FINALIZADO.")