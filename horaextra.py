base = float(input('Qual o seu salario: '))

saldo = (base / 220) + (base / 220 / 2)

print('O valor da sua hora extra é {:.2f}'  
.format(saldo))

extra = float(input('Digite a quantidade de horas extras trabalhadas:'))

total = saldo * extra

print('O valor das horas extras somado é {:.2f}'.format(total))