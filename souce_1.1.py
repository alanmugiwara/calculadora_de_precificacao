import tkinter as tk
from tkinter import Entry, Label, Button, Text
from PIL import Image, ImageTk

# Função para calcular o CPA e o lucro e exibir o resultado
def calcular_cpa():
    custo_produto_brl = float(custo_produto_entry.get().replace(",", "."))
    custo_marketing_brl = float(custo_marketing_entry.get().replace(",", "."))
    porcentagem_gateway = float(porcentagem_gateway_entry.get().replace(",", ".")) / 100
    porcentagem_loja_virtual = float(porcentagem_loja_virtual_entry.get().replace(",", ".")) / 100
    porcentagem_checkout = float(porcentagem_checkout_entry.get().replace(",", ".")) / 100

    # Obtenha o valor da entrada de venda como uma string
    valor_venda_str = valor_venda_entry.get()

    # Substitua vírgulas por pontos na string e converta para float
    valor_venda_brl = float(valor_venda_str.replace(",", "."))

    cpa = custo_produto_brl + custo_marketing_brl
    cpa += (porcentagem_gateway * cpa)
    cpa += (porcentagem_loja_virtual * cpa)
    cpa += (porcentagem_checkout * cpa)

    lucro = valor_venda_brl - cpa
    lucro_porcentagem = (lucro / cpa) * 100

    resultado_cpa.delete(1.0, tk.END)
    resultado_cpa.insert(tk.END, f"CPA: R${cpa:.2f}")

    resultado_lucro.delete(1.0, tk.END)
    resultado_lucro.insert(tk.END, f"Lucro: R${lucro:.2f} ({lucro_porcentagem:.2f}%)")

# Função para abrir URLs em um navegador
import webbrowser

def open_url(url):
    webbrowser.open(url)

# Configuração da janela
window = tk.Tk()
window.title("Calculadora de Precificação | By @alanmugiwaras")
window.geometry("430x570")

# Criação de rótulos e campos de entrada usando o gerenciador grid
Label(window, text="Custo do Produto no Fornecedor (BRL)").grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
custo_produto_entry = Entry(window)
custo_produto_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='w')

Label(window, text="Custo de Marketing (BRL)").grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')
custo_marketing_entry = Entry(window)
custo_marketing_entry.grid(row=3, column=0, padx=10, pady=(0, 10), sticky='w')

Label(window, text="Porcentagem do Gateway de Pagamento (%)").grid(row=4, column=0, padx=10, pady=(10, 0), sticky='w')
porcentagem_gateway_entry = Entry(window)
porcentagem_gateway_entry.grid(row=5, column=0, padx=10, pady=(0, 10), sticky='w')

Label(window, text="Porcentagem de Taxa da Loja Virtual (%)").grid(row=6, column=0, padx=10, pady=(10, 0), sticky='w')
porcentagem_loja_virtual_entry = Entry(window)
porcentagem_loja_virtual_entry.grid(row=7, column=0, padx=10, pady=(0, 10), sticky='w')

Label(window, text="Porcentagem Checkout Transparente (%)").grid(row=8, column=0, padx=10, pady=(10, 0), sticky='w')
porcentagem_checkout_entry = Entry(window)
porcentagem_checkout_entry.grid(row=9, column=0, padx=10, pady=(0, 10), sticky='w')

Label(window, text="Valor de Venda (BRL)").grid(row=10, column=0, padx=10, pady=(10, 0), sticky='w')
valor_venda_entry = Entry(window)
valor_venda_entry.grid(row=11, column=0, padx=10, pady=(0, 10), sticky='w')

calcular_button = Button(window, text="Calcular CPA e Lucro", command=calcular_cpa)
calcular_button.grid(row=12, column=0, padx=10, pady=(10, 10), sticky='w')

resultado_cpa = Text(window, height=1, width=40)
resultado_cpa.grid(row=13, column=0, padx=10, pady=(0, 10), columnspan=2, sticky='w')

resultado_lucro = Text(window, height=1, width=40)
resultado_lucro.grid(row=14, column=0, padx=10, pady=(0, 10), columnspan=2, sticky='w')

# Observação para o usuário
observacao_label = Label(window, text="Digite '0' para ignorar os campos que não deseja calcular", anchor='w')
observacao_label.grid(row=15, column=0, columnspan=2, padx=10, pady=10, sticky='w')

# Inicia o loop da aplicação
window.mainloop()
