# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
s = 0 

while True:
    n = float(input("Digite quantos números quiser para soma-los, digite 0 para parar: "))
    if n == 0:
        break

    s += n


print (f"A soma dos números é {s}")
