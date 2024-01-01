def cumprimentar():
    print("Olá! Eu sou um robô.")
    print("Qual é o seu nome?")
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}!")

def perguntar_idade():
    print("Posso perguntar sua idade?")
    resposta = input("Sim ou não: ")
    if resposta.lower() == "sim":
        idade = input("Quantos anos você tem? ")
        print(f"Legal! Você tem {idade} anos.")
    else:
        print("Tudo bem, sem problemas!")

def main():
    cumprimentar()
    perguntar_idade()

if __name__ == "__main__":
    main()


#estraído do chatgpt para estudo
    
