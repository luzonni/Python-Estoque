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
tree = ttk.Treeview(frame_esquerda, columns=('CATEGORIA', 'NOME', 'QUANTIDADE', 'TAG'), show='headings')
tree.heading('#1', text='CATEGORIA')
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
valor1_label = tk.Label(frame_direita, text='CATEGORIA:', font=framedireitafont)
valor1_label.pack()
valor1_entry = tk.Entry(frame_direita)
valor1_entry.pack(fill=tk.X)

valor2_label = tk.Label(frame_direita, text='NOME:', font=framedireitafont)
valor2_label.pack()
valor2_entry = tk.Entry(frame_direita)
valor2_entry.pack(fill=tk.X)

valor3_label = tk.Label(frame_direita, text='QUANTIDADE:', font=framedireitafont)
valor3_label.pack()
valor3_entry = tk.Entry(frame_direita)
valor3_entry.pack(fill=tk.X)

valor4_label = tk.Label(frame_direita, text='TAG:', font=framedireitafont)
valor4_label.pack()
valor4_entry = tk.Entry(frame_direita)
valor4_entry.pack(fill=tk.X)

#Criação e personalização dos botões

# Botão Adicionar
botao_adicionar = tk.Button(frame_direita, text="Adicionar Valor", command=adicionar_valor)
botao_adicionar.config(bg="green", fg="White", width=15)
botao_adicionar.pack(pady=5)

# Botão Remover
botao_remover = tk.Button(frame_direita, text="Remover Valor", command=remover_valor)
botao_remover.config(bg="red", fg="White", width=15)
botao_remover.pack(pady=5)

# Botão Editar
# botao_editar = tk.Button(frame_direita, text="Editar Valor", command=editar_valor)
# botao_editar.config(bg="blue", fg="white", width=15)
# botao_editar.pack(pady=5)


# Botão Mostrar Valores
botao_mostrar = tk.Button(frame_direita, text="Mostrar Valores", command=recuperar_valores)
botao_mostrar.config(bg="yellow", width=15)
botao_mostrar.pack(pady=5)

# estilo da Treeview para as colunas
column_style = ttk.Style()
column_style.configure("Treeview.Heading", font=('Arial', 8), background="#121718")

# estilo da Treeview para as linhas
row_style = ttk.Style()
row_style.configure("Treeview", rowheight=25, background="#bbd5de", font=('Arial', 8))

# Obs: Tentei fazer com que as linhas e colunas ficassem com espaçamento, cor e qualquer coisa do tipo diferente, mas
# aparentemente não deu certo. Se souber a resposta, seria interessante alterar isso. Vou deixar ambos no código, pois
# não faz diferença. O Único que funciona é o row_style

# Inicie o loop principal da interface gráfica
janela.mainloop()
