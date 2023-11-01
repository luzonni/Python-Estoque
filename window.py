import tkinter as tk
from tkinter import * 
from tkinter import ttk
import tkinter.font as tkFont
from Tagger import getTags

TAGS:list = getTags("Tags.db")


def adicionar_valor():
    valor1 = entry_nome.get()
    valor2 = entry_quantidade.get()
    valor3 = TAGS[int(entry_tag.curselection()[0])]
    if valor1 and valor2 and valor3:
        tree.insert('', 'end', values=(0, valor1, valor2, valor3))
        entry_nome.delete(0, 'end')
        entry_quantidade.delete(0, 'end')

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
janela.configure(bg='lightblue')
janela.minsize(1000, 300)

# Configurar a fonte
font = tkFont.Font(family='Arial', size=14, weight='bold')
framedireitafont = tkFont.Font(family='Arial', size=10, weight='bold')

# Frame para a tabela
frame_esquerda = tk.Frame(janela)
frame_esquerda.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Frame para as entradas e botões
frame_direita = tk.Frame(janela)
frame_direita.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')


# Crie um widget Treeview para a tabela
tree = ttk.Treeview(frame_esquerda, columns=('ID', 'NOME', 'QUANTIDADE', 'TAG'), show='headings')
tree.heading('#1', text='ID')
tree.heading('#2', text='NOME')
tree.heading('#3', text='QUANTIDADE')
tree.heading('#4', text='TAG')

tree.column('#1', width=100)
tree.column('#2', width=100)
tree.column('#3', width=100)
tree.column('#4', width=100)


tree.pack(fill=tk.BOTH, expand=True)


# Configurar o peso das colunas e linhas
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.rowconfigure(0, weight=1)

# Crie entradas para adicionar valores

label_nome = tk.Label(frame_direita, text='NOME:', font=framedireitafont)
label_nome.pack()
entry_nome = tk.Entry(frame_direita)
entry_nome.pack(fill=tk.X)

label_quantidade = tk.Label(frame_direita, text='QUANTIDADE:', font=framedireitafont)
label_quantidade.pack()
entry_quantidade = tk.Entry(frame_direita)
entry_quantidade.pack(fill=tk.X)

label_tag = tk.Label(frame_direita, text='TAG:', font=framedireitafont)
label_tag.pack()
entry_tag = tk.Listbox(frame_direita)
my_list = TAGS
for item in my_list:
    entry_tag.insert(END, item)
entry_tag.pack(fill=tk.X)

#Criação e personalização dos botões

# Botão Adicionar
botao_adicionar = tk.Button(frame_direita, text="Adicionar Valor", command=adicionar_valor)
botao_adicionar.config(bg="#8ab0bd", fg="black", width=15)
botao_adicionar.pack(pady=5)

# Botão Remover
botao_remover = tk.Button(frame_direita, text="Remover Valor", command=remover_valor)
botao_remover.config(bg="#8ab0bd", fg="black", width=15)
botao_remover.pack(pady=5)

# Botão Editar
# botao_editar = tk.Button(frame_direita, text="Editar Valor", command=editar_valor)
# botao_editar.config(bg="blue", fg="white", width=15)
# botao_editar.pack(pady=5)


# Botão Mostrar Valores
botao_mostrar = tk.Button(frame_direita, text="Editar Valores", command=recuperar_valores)
botao_mostrar.config(bg="#8ab0bd", fg="black", width=15)
botao_mostrar.pack(pady=5)

# estilo da Treeview para as colunas
column_style = ttk.Style()
column_style.configure("Treeview.Heading", font=('Arial', 8), background="#121718")

# estilo da Treeview para as linhas
row_style = ttk.Style()
row_style.configure("Treeview", rowheight=25, background="#bbd5de", font=('Arial', 8))

# Inicie o loop principal da interface gráfica
janela.mainloop()
