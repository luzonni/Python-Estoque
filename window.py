import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


# Função para adicionar um valor à tabela
def adicionar_valor():
    valor1 = valor1_entry.get()
    valor2 = valor2_entry.get()
    valor3 = valor3_entry.get()
    valor4 = valor4_entry.get()

    if valor1 and valor2 and valor3 and valor4:
        tree.insert('', 'end', values=(valor1, valor2, valor3, valor4))
        valor1_entry.delete(0, 'end')
        valor2_entry.delete(0, 'end')
        valor3_entry.delete(0, 'end')
        valor4_entry.delete(0, 'end')


# Função para remover um valor selecionado da tabela
def remover_valor():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
        
def recuperar_valores():
    for item in tree.get_children():
        valores = tree.item(item)['values']
        print(valores)

# Crie uma instância da janela principal
janela = tk.Tk()
janela.title("Tabela de Valores")

janela.configure(bg='#363e50')
font = tkFont.Font(family='Arial',size=14,weight='bold')


# Crie um widget Treeview para a tabela
tree = ttk.Treeview(janela, columns=('ID', 'Nome', 'Quantidade', 'TAG'), show='headings')
tree.heading('#1', text='ID')
tree.heading('#2', text='Nome')
tree.heading('#3', text='Quantidade')
tree.heading('#4', text='TAG')

tree.column('#0', width=0, stretch=tk.NO)

tree.pack()

# Crie entradas para adicionar valores
valor1_label = tk.Label(janela, text='ID:',font=font)
valor1_label.pack()
valor1_entry = tk.Entry(janela)
valor1_entry.pack()

valor2_label = tk.Label(janela, text='Nome:',font=font)
valor2_label.pack()
valor2_entry = tk.Entry(janela)
valor2_entry.pack()

valor3_label = tk.Label(janela, text='Quantidade:',font=font)
valor3_label.pack()
valor3_entry = tk.Entry(janela)
valor3_entry.pack()

valor4_label = tk.Label(janela, text='TAG:',font=font)
valor4_label.pack()
valor4_entry = tk.Entry(janela)
valor4_entry.pack()

# Crie botões para adicionar e remover valores
tk.Button(janela, text="Adicionar Valor", command=adicionar_valor).pack()
tk.Button(janela, text="Remover Valor Selecionado", command=remover_valor).pack()
tk.Button(janela, text="Print Valores", command=recuperar_valores).pack()

# Inicie o loop principal da interface gráfica
janela.mainloop()

