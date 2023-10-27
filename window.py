import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

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

def remover_valor():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)

def recuperar_valores():
    for item in tree.get_children():
        valores = tree.item(item)['values']
        print(valores)

# Instância da janela principal
janela = tk.Tk()
janela.title("Tabela de Valores")

# Cor da Janela
janela.configure(bg='#363e50')

# Configurar o tamanho mínimo da janela
janela.minsize(400, 300)

# Configurar a fonte
font = tkFont.Font(family='Arial', size=14, weight='bold')

# Feito para colocar a tabela na esquerda
frame_esquerda = tk.Frame(janela)
frame_esquerda.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Feito para colocar as entradas e os botões na direita
frame_direita = tk.Frame(janela)
frame_direita.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# Crie um widget Treeview para a tabela
tree = ttk.Treeview(frame_esquerda, columns=('ID', 'Nome', 'Quantidade', 'TAG'), show='headings')
tree.heading('#1', text='ID')
tree.heading('#2', text='Nome')
tree.heading('#3', text='Quantidade')
tree.heading('#4', text='TAG')

tree.column('#0', width=0, stretch=tk.NO)


tree.pack(fill=tk.BOTH, expand=True) #o fill=tk.BOTH, expand=true serve para preencher e expandir para ajustar ao tamanho


# Isso aqui serve para configurar  o peso das colunas e linhas para que elas se ajustem à janela
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.rowconfigure(0, weight=1)

# Crie entradas para adicionar valores
valor1_label = tk.Label(frame_direita, text='ID:')
valor1_label.pack()
valor1_entry = tk.Entry(frame_direita)
valor1_entry.pack(fill=tk.X)

valor2_label = tk.Label(frame_direita, text='Nome:')
valor2_label.pack()
valor2_entry = tk.Entry(frame_direita)
valor2_entry.pack(fill=tk.X)

valor3_label = tk.Label(frame_direita, text='Quantidade:')
valor3_label.pack()
valor3_entry = tk.Entry(frame_direita)
valor3_entry.pack(fill=tk.X)

valor4_label = tk.Label(frame_direita, text='TAG:')
valor4_label.pack()
valor4_entry = tk.Entry(frame_direita)
valor4_entry.pack(fill=tk.X)

# O fill=tk.x serve para peencher horizontalmente

# Crie botões para adicionar e remover valores
tk.Button(frame_direita, text="Adicionar Valor", command=adicionar_valor).pack()
tk.Button(frame_direita, text="Remover Valor Selecionado", command=remover_valor).pack()
tk.Button(frame_direita, text="Print Valores", command=recuperar_valores).pack()

# Inicie o loop principal da interface gráfica
janela.mainloop()
