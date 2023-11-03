import tkinter as tk
from tkinter import * 
from tkinter import ttk
import tkinter.font as tkFont

def adicionar_tag():
    valor1 = entry_nome_tag.get()
    if valor1:
        tree.insert('', 'end', values=(valor1))
        entry_nome_tag.delete(0, 'end')

def remover_tag():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)


# Instância da janela principal
janela = tk.Tk()
janela.title("Adicionar/Remover Tags")
janela.configure(bg='#363f4e')
janela.minsize(500, 200)

# Isso aqui é pra manter fixo 
janela.resizable(width=False, height=False)

# Configurar a fonte
font = tkFont.Font(family='Arial', size=14, weight='bold')
framedireitafont = tkFont.Font(family='Arial', size=10)

# Frame para a tabela
frame_esquerda = tk.Frame(janela)
frame_esquerda.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Frame para as entradas e botões
frame_direita = tk.Frame(janela)
frame_direita.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# Crie um widget Treeview para a tabela
tree = ttk.Treeview(frame_esquerda, columns=('TAG'), show='headings')
tree.heading('#1', text='Tags')

tree.column('#1', width=100)

# Scroll
scroll = ttk.Scrollbar(frame_esquerda, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)

tree.pack(fill=tk.BOTH)
scroll.pack(side="right", fill="y")

# Configurar o peso das colunas e linhas
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.rowconfigure(0, weight=1)

# Entrada das tags
label_nome_tag = tk.Label(frame_direita, text='Nome:', font=framedireitafont)
label_nome_tag.pack()
entry_nome_tag = tk.Entry(frame_direita)
entry_nome_tag.pack(fill=tk.X)

# Botão Adicionar tag
botao_adicionar_tag = tk.Button(frame_direita, text="Adicionar", command=adicionar_tag)
botao_adicionar_tag.config(bg="#2b323e", fg="white", width=15)
botao_adicionar_tag.pack(side="top", padx=10, pady=5)


# Botão Remover tag
botao_remover_tag = tk.Button(frame_direita, text="Remover", command=remover_tag)
botao_remover_tag.config(bg="#2b323e", fg="white", width=15)
botao_remover_tag.pack(side="top", padx=10, pady=5)


# Estilo da coluna
coluna_style = ttk.Style()
coluna_style.configure("Treeview", rowheight=25, background="#5e6571", font=('Arial', 8))

# Inicie o loop principal da interface gráfica
janela.mainloop()
