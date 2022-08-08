user = input("user:")
senha = input("senha:")

while user == senha:
    print("Erro: A senha precisa ser outra. ")
    senha = input("Digite sua senha")
print("Login aceito!!")
