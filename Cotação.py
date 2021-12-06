from time import sleep

nome = str(input('Informe o seu nome: '))
valor = float(input('Informe o valor que obtem em Real R$ '))
moeda_conv = int(input('Informe para qual moeda que converter:\n[1]USD\n[2]EURO\n[3]PESO ARGENTINO\n[4]LIBRA\n[5]CAD '
                         '\nQual Moeda escolhida: '))

sleep(2)
if moeda_conv == 1:
    print('Sr {} com R$ {:.2f} o senhor terá $ {:.2F} Dolares Americano  !'.format(nome, valor, valor/5.69))
elif moeda_conv == 2:
    print('Sr {} com R$ {:.2f} o senhor terá £ {:.2F} Euros !'.format(nome, valor, valor/6.42))
elif moeda_conv == 3:
    print('Sr {} com R$ {:.2f} o senhor terá $ {:.2F} Peso argentino !'.format(nome, valor, valor/0.056))
elif moeda_conv == 4:
    print('Sr {} com R$ {:.2f} o senhor terá £ {:.2F} Libras esterlinas !'.format(nome, valor, valor/7.55))
elif moeda_conv == 5:
    print('Sr {} com R$ {:.2f} o senhor terá C$ {:.2F} Dolares Canadenses !'.format(nome, valor, valor/4.46))

elif moeda_conv != 1 or 2 or 3 or 4 or 5:
    print('Opção invalida')

print('Cotação do dia 06/12/2021')
print('Obrigado sr {} volte sempre !!'.format(nome))
