excelente = 0
ruim = 0

for n in range(1,11):
    print(f"\n--- Entrevistado n° {n} ---")

    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")

    print("Qual a sua opinião?")
    print("1: EXCELENTE | 2: BOM | 3: RUIM")
    opiniao =  input("Resposta: ")

    if opiniao == "1":
        excelente +=1
    elif opiniao == "3":
        ruim += 1

print("\n" + "="*20)
print("RESULTADO DA PESQUISA")
print(f"Total Excelente: {excelente}")
print(f"Total Ruim: {ruim}")
print("="*20)

input("\nProcesso finalizado. Aperte ENTER para sair.")
