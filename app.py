from forex_python.converter import CurrencyRates


def boas_vindas():
    mensagem = 'Bem-vindo ao sistema de Conversão monetária!'
    print('*' * len(mensagem))
    print(mensagem)
    print('*' * len(mensagem))


def opcoes_moedas():
    moedas = {
        '1': 'USD',
        '2': 'EUR',
        '3': 'Outra'
    }
    for key, value in moedas.items():
        print(f'{key} - {value}')


def aplicacao():
    moeda_incial = input('Escolha uma moeda inicial: ')
    if moeda_incial == '1':
        moeda_incial = 'USD'
    elif moeda_incial == '2':
        moeda_incial = 'EUR'
    elif moeda_incial == '3':
        moeda_incial = input('Digite a moeda inicial: ')
    moeda_cambio = input('Escolha a moeda de cambio: ')
    if moeda_cambio == '1':
        moeda_cambio = 'USD'
    elif moeda_cambio == '2':
        moeda_cambio = 'EUR'
    elif moeda_cambio == '3':
        moeda_cambio = input('Digite a moeda de cambio: ')

    valor_converter = float(input('Digite o valor que pretende converter: '))
    c = CurrencyRates()
    conversao = c.convert(moeda_incial.upper(), moeda_cambio.upper(), valor_converter)
    print(f'{valor_converter}({moeda_incial}) equivale a {conversao:.2f}({moeda_cambio.upper()})')


boas_vindas()
opcoes_moedas()
aplicacao()
