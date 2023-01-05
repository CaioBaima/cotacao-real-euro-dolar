import requests
import tkinter as tk

root = tk.Tk()
root.title('Cotações')
root.geometry('250x270')

def exibir():
    request = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL')
    cotacao = request.json()

    dolar = float(cotacao['USD']['bid'])
    euro = float(cotacao['EUR']['bid'])
    
    label_dolar['text'] = f'A cotação atual do dolar em real é R${dolar:.4f}'
    label_euro['text'] = f'A cotação atual do euro em real é R${euro:.4f}'

    label_dolar.pack()
    label_euro.pack()

def conversao():
    request = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL')
    cotacao = request.json()

    dolar = float(cotacao['USD']['bid'])
    euro = float(cotacao['EUR']['bid'])

    valor = (conversor.get())
    try:
        resultado1['text'] = f'Seu valor em dólar é R${float(valor)/dolar:.4f}'
        resultado2['text'] = f'Seu valor em dólar é R${float(valor)/euro:.4f}'
        erro['text'] = f''
    except:
        if len(valor) == 0:
            erro['text'] = f'Você precisa digitar um valor numérico acima.'


def espaco():
    espaço = tk.Label(text='')
    espaço.pack()

espaco()

label_dolar = tk.Label(text='')
label_euro = tk.Label(text='')
exibir()

label_dolar.pack()
label_euro.pack()

botao = tk.Button(root, text='Atualizar cotação', command=exibir)
botao.pack()

espaco()

label_converta = tk.Label(text='Digite o valor que deseja converter em real:')
label_converta.pack()

conversor = tk.Entry()
conversor.pack()

resultado1 = tk.Label(text='Seu valor em dólar é R$--.----')
resultado1.pack()
resultado2 = tk.Label(text='Seu valor em euro é R$--.----')
resultado2.pack()

botao_conversao = tk.Button(root, text='Converter.', command=conversao)
botao_conversao.pack()

erro = tk.Label(text='')
erro.pack()

fechar = tk.Button(root, text='Fechar', command=root.destroy)
fechar.pack()

root.mainloop()