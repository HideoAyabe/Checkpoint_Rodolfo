c = float(input("Digite o capital inicial que voce deseja guardar na poupança: "))
pmt = float(input("Digite o valor dos aportes mensais que voce planeja fazer: "))
i = float(input("Digite o valor da taxa de juros: "))
n = int(input("Digite o perídodo (meses) que você pretende deixar o dinheiro investido: "))

m = c*(1 + i)**n + pmt * (((1 + i)**n - 1)/i)

print(f"O montante que você terá ao longo de {n} meses será R${m:.2f}.")
