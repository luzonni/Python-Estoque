import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
from Produto import Produto
from Estoque import Estoque
from Tagger import Tagger

PATH:str = "Banco.db"
Tagger:Tagger = Tagger("Tags.db")
TAGS:list = Tagger.getTags()

class Engine:
    
    def __init__(self, name:str):
        self.__estoque = Estoque(PATH)
        self.__window = tk.Tk()
        self.__window.title(name)
        self.__window.configure(bg='lightblue')
        self.__window.minsize(1000, 300)
        self.configWindow(self.__window)
        
    @property
    def estoque(self):
        return self.__estoque
    
    @estoque.setter
    def estoque(self, newEstoque):
        self.__estoque = newEstoque
    
    def configWindow(self, janela:Tk):
        janela.resizable(width=False, height=False)
        janela.columnconfigure(0, weight=1)
        janela.columnconfigure(1, weight=1)
        janela.rowconfigure(0, weight=1)
        janela.protocol("WM_DELETE_WINDOW", self.close)
        framedireitafont = tkFont.Font(family='Arial', size=10, weight='bold')
        
        # Frame da tabela
        frame_esquerda = tk.Frame(janela)
        frame_esquerda.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.tree = ttk.Treeview(frame_esquerda, columns=('ID', 'NOME', 'QUANTIDADE', 'TAG'), show='headings')
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='NOME')
        self.tree.heading('#3', text='QUANTIDADE')
        self.tree.heading('#4', text='TAG')
        self.tree.column('#1', width=25)
        self.tree.column('#2', width=100)
        self.tree.column('#3', width=100)
        self.tree.column('#4', width=100)
        row_style = ttk.Style()
        row_style.configure("Treeview", rowheight=25, background="#bbd5de", font=('Arial', 8))
        column_style = ttk.Style()
        column_style.configure("Treeview.Heading", font=('Arial', 8), background="#121718")
        self.tree.pack(fill=tk.BOTH, expand=True)
         
        # Frame de manipulação
        frame_meio = tk.Frame(janela)
        frame_meio.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        frame_meio = tk.Frame(janela)
        frame_meio.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        if not self.__estoque.isEmpty():
            produtos = self.__estoque.getList()
            for produto in produtos:
                self.tree.insert('', 'end', values=(produto.id, produto.nome, produto.quantidade, TAGS[produto.tagId]))
        label_nome = tk.Label(frame_meio, text='NOME:', font=framedireitafont)
        label_nome.pack()
        self.entry_nome = tk.Entry(frame_meio)
        self.entry_nome.pack(fill=tk.X)
        label_quantidade = tk.Label(frame_meio, text='QUANTIDADE:', font=framedireitafont)
        label_quantidade.pack()
        self.entry_quantidade = tk.Entry(frame_meio)
        self.entry_quantidade.pack(fill=tk.X)
        label_tag = tk.Label(frame_meio, text='TAG:', font=framedireitafont)
        label_tag.pack()
        self.entry_tag = tk.Listbox(frame_meio)
        my_list = TAGS
        for item in my_list:
            self.entry_tag.insert(END, item)
        self.entry_tag.pack(fill=tk.X)
        botao_adicionar = tk.Button(frame_meio, text="Adicionar Valor", command=self.adicionar_valor)
        botao_adicionar.config(bg="#8ab0bd", fg="black", width=15)
        botao_adicionar.pack(pady=5)
        botao_remover = tk.Button(frame_meio, text="Remover Valor", command=self.remover_valor)
        botao_remover.config(bg="#8ab0bd", fg="black", width=15)
        botao_remover.pack(pady=5)
        botao_mostrar = tk.Button(frame_meio, text="Editar Valores", command=self.recuperar_valores)
        botao_mostrar.config(bg="#8ab0bd", fg="black", width=15)
        botao_mostrar.pack(pady=5)
        
        # Frame de Configuração
        frame_direita = tk.Frame(janela)
        frame_direita.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
        tk.Label(frame_direita, text='___ Configurações ___', font=framedireitafont, bg="#7d7c7c", ).pack()
        tk.Label(frame_direita, text='Limpar lista de Tags:', font=framedireitafont, bg="#7d7c7c").pack()
        botao_remover_tags = tk.Button(frame_direita, text="Limpar", command=self.dellTagFile)
        botao_remover_tags.config(bg="#8a070d")
        botao_remover_tags.pack(fill=tk.X)
        tk.Label(frame_direita, text='Reiniciar tabela:', font=framedireitafont, bg="#7d7c7c").pack()
        botao_remover_items = tk.Button(frame_direita, text="Limpar", command=self.dellallItemsFile)
        botao_remover_items.config(bg="#8a070d")
        botao_remover_items.pack(fill=tk.X)
        frame_direita.config(bg="#7d7c7c")
        
        
        janela.mainloop()
    
    def dellTagFile(self):
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente apagar todas as Tags? Isso fará TODOS os itens da lista serem removidos")
        if resposta:
            print("Deletar Tags!")
        else: 
            print("Ação cancelada!")
            
    def dellallItemsFile(self):
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente apagar todas as Tags? Isso fará TODOS os itens da lista serem removidos")
        if resposta:
            print("Deletar Items!")
        else: 
            print("Ação cancelada!")
    
    def adicionar_valor(self):
        id:int = len(self.__estoque.getList())
        nome:str = self.entry_nome.get()
        quantidade:int = self.entry_quantidade.get()
        tag_id:int = int(self.entry_tag.curselection()[0])
        
        if nome and quantidade:
            self.tree.insert('', 'end', values=(id, nome, quantidade, TAGS[tag_id]))
            self.entry_nome.delete(0, 'end')
            self.entry_quantidade.delete(0, 'end')
            self.__estoque.add(Produto(id, nome, quantidade, tag_id))
        else:
            print("Valores não preenchidos")
            
    def remover_valor(self):
        selected_item = self.tree.selection()
        if selected_item:
            id_selected = self.tree.item(selected_item)["values"][0]
            self.tree.delete(selected_item)
            self.__estoque.remove(id_selected)
            

    def recuperar_valores(self):
        for item in self.tree.get_children():
            valores = self.tree.item(item)['values']
            print(valores)
    
    def close(self):
        self.__estoque.closeList()
        self.__window.destroy()
            
            
Engine("Supermercado Ótimo!Preço")