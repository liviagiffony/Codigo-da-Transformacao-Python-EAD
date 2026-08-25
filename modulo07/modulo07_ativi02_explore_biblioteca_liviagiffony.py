print("===== PROVA DE CONHECIMENTOS GERAIS =====")
print("Responda às 3 questões!\n")

pontos = 0

# Questão 1
print("1) Qual é o maior planeta do Sistema Solar?")
print("a) Terra")
print("b) Marte")
print("c) Júpiter")
print("d) Vênus")

resposta = input("Resposta: ")

if resposta.lower() == "c":
    print("Correto!\n")
    pontos += 1
else:
    print("Errado! A resposta correta é Júpiter.\n")


# Questão 2
print("2) Quanto é 8 x 7?")
print("a) 54")
print("b) 56")
print("c) 64")
print("d) 48")

resposta = input("Resposta: ")

if resposta.lower() == "b":
    print("Correto!\n")
    pontos += 1
else:
    print("Errado! A resposta correta é 56.\n")


# Questão 3
print("3) Qual animal é conhecido como o 'rei da selva'?")
print("a) Tigre")
print("b) Elefante")
print("c) Leão")
print("d) Girafa")

resposta = input("Resposta: ")

if resposta.lower() == "c":
    print("Correto!\n")
    pontos += 1
else:
    print("Errado! A resposta correta é Leão.\n")


print("===== RESULTADO =====")
print("Você acertou", pontos, "de 3 questões!")

if pontos == 3:
    print("Parabéns! Você acertou tudo!")
elif pontos >= 1:
    print("Você foi bem!")
else:
    print("Estude um pouco mais!")