import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
from tools.Produto import Produto
from tools.Estoque import Estoque
from tools.Tagger import Tagger

PATH:str = "res/Banco.db"
Tagger:Tagger = Tagger("res/Tags.db")
TAGS:list = Tagger.getTags()

class Engine:
    
    def __init__(self, name:str):
        self.__estoque = Estoque(PATH)
        self.__window = tk.Tk()
        self.__window.title(name)
        self.__window.configure(bg='lightblue')
        self.__window.minsize(600, 300)
        self.__auxWindow:Tk = tk.Frame(self.__window)
        self.configWindow(self.__window)
        
    @property
    def estoque(self):
        return self.__estoque
    
    @estoque.setter
    def estoque(self, newEstoque):
        self.__estoque = newEstoque
    
    def configWindow(self, janela:Tk):
        janela.resizable(width=True, height=False)
        janela.columnconfigure(0, weight=2)
        janela.rowconfigure(0, weight=2)
        janela.protocol("WM_DELETE_WINDOW", self.close)
        # Frame Main
        frame_esquerda = tk.Frame(janela)
        frame_esquerda.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.tree = ttk.Treeview(frame_esquerda, columns=('ID', 'NOME', 'QUANTIDADE', 'TAG'), show='headings')
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='NOME')
        self.tree.heading('#3', text='QUANTIDADE')
        self.tree.heading('#4', text='TAG')
        self.tree.column('#1', width=50)
        self.tree.column('#2', width=200)
        self.tree.column('#3', width=200)
        self.tree.column('#4', width=200)
        if not self.__estoque.isEmpty():
            produtos = self.__estoque.getList()
            for produto in produtos:
                self.tree.insert('', 'end', values=(produto.id, produto.nome, produto.quantidade, TAGS[produto.tagId]))
        row_style = ttk.Style()
        row_style.configure("Treeview", rowheight=25, background="#bbd5de", font=('Arial', 8))
        column_style = ttk.Style()
        column_style.configure("Treeview.Heading", font=('Arial', 8), background="#121718")
        self.entry_filter = ttk.Combobox(frame_esquerda, values=(["Todos"] + TAGS), state="readonly")
        self.entry_filter.set("Filtro")
        self.entry_filter.bind("<<ComboboxSelected>>", self.filtrarTable)
        self.entry_filter.pack(side=tk.TOP, anchor=tk.E, padx=10, pady=10)
        self.tree.pack(fill=tk.BOTH, expand=True)
        botao_adicionar = tk.Button(frame_esquerda, text="Adicionar Item", command=lambda : self.addFrame_Inserir(janela))
        botao_adicionar.config(bg="#8ab0bd", fg="black", width=15)
        botao_adicionar.pack(side=RIGHT, anchor=tk.E, padx=5)
        botao_remover = tk.Button(frame_esquerda, text="Remover Item", command=self.remover_valor)
        botao_remover.config(bg="#8ab0bd", fg="black", width=15)
        botao_remover.pack(side=RIGHT, anchor=tk.E, padx=5, pady=5)
        botao_editar = tk.Button(frame_esquerda, text="Editar Item", command=lambda : self.addFrame_Edit(janela))
        botao_editar.config(bg="#8ab0bd", fg="black", width=15)
        botao_editar.pack(side=RIGHT, anchor=tk.E, padx=5)
        func_config = lambda : self.addFrame_Config(janela)
        botao_config = tk.Button(frame_esquerda, text="Config", command=func_config)
        botao_config.config(bg="#8ab0bd", fg="black", width=10)
        botao_config.pack(side=LEFT, anchor=tk.W, padx=10)
        janela.mainloop()
        
    def addFrame_Inserir(self, janela:Tk):
        self.__auxWindow.destroy()
        self.__auxWindow = tk.Frame(janela)
        janela.columnconfigure(1, weight=1)
        janela.rowconfigure(1, weight=1)
        font = tkFont.Font(family='Arial', size=10, weight='bold')
        self.__auxWindow.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        tk.Button(self.__auxWindow, text="Fechar", command=lambda : self.closeAuxWindow(janela)).pack(anchor="ne", padx=10, pady=10)
        label_nome = tk.Label(self.__auxWindow, text='NOME:', font=font)
        label_nome.pack()
        self.entry_nome = tk.Entry(self.__auxWindow)
        self.entry_nome.pack(fill=tk.X, padx=15)
        label_quantidade = tk.Label(self.__auxWindow, text='QUANTIDADE:', font=font)
        label_quantidade.pack()
        self.entry_quantidade = tk.Entry(self.__auxWindow, validate='key', validatecommand=(janela.register(lambda novo_valor: novo_valor.isdigit() or novo_valor == ''), '%P'))
        self.entry_quantidade.pack()
        label_tag = tk.Label(self.__auxWindow, text='TAG:', font=font)
        label_tag.pack()
        self.entry_tag = ttk.Combobox(self.__auxWindow, values=TAGS, state="readonly")
        self.entry_tag.set("Selecione uma Tag")
        self.entry_tag.pack(fill=tk.X, padx=10)
        botao_adicionar = tk.Button(self.__auxWindow, text="Adicionar Valor", command=lambda : self.adicionar_valor(janela))
        botao_adicionar.config(bg="#8ab0bd", fg="black", width=15)
        botao_adicionar.pack(side=tk.BOTTOM, pady=25)
    
    def addFrame_Edit(self, janela:Tk):
        index = self.tree.index(self.tree.focus())
        produto = self.__estoque.get(index)
        
        id:int = produto.id
        nome:str = produto.nome
        quantidade:int = produto.quantidade
        tag_id:int = produto.tagId
        self.__auxWindow.destroy()
        self.__auxWindow = tk.Frame(janela)
        janela.columnconfigure(1, weight=1)
        janela.rowconfigure(1, weight=1)
        font = tkFont.Font(family='Arial', size=10, weight='bold')
        self.__auxWindow.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        tk.Button(self.__auxWindow, text="Fechar", command=lambda : self.closeAuxWindow(janela)).pack(anchor="ne", padx=10, pady=10)
        
        tk.Label(self.__auxWindow, text=f'Editando produto: {nome}').pack()
        tk.Label(self.__auxWindow, text='NOME:', font=font).pack()
        texto_variavel_quantidade = tk.StringVar()
        texto_variavel_quantidade.set(nome)
        entry_nome = tk.Entry(self.__auxWindow, textvariable=texto_variavel_quantidade)
        entry_nome.pack(fill=tk.X, padx=15)
        tk.Label(self.__auxWindow, text='QUANTIDADE:', font=font).pack()
        texto_variavel_quantidade = tk.StringVar()
        texto_variavel_quantidade.set(quantidade)
        entry_quantidade = tk.Entry(self.__auxWindow, validate='key', validatecommand=(janela.register(lambda novo_valor: novo_valor.isdigit() or novo_valor == ''), '%P'), textvariable=texto_variavel_quantidade)
        
        entry_quantidade.pack()
        label_tag = tk.Label(self.__auxWindow, text='TAG:', font=font)
        label_tag.pack()
        entry_tag = ttk.Combobox(self.__auxWindow, values=TAGS, state="readonly")
        entry_tag.set(TAGS[tag_id])
        entry_tag.pack(fill=tk.X, padx=10)
        botao_adicionar = tk.Button(self.__auxWindow, text="Alterar", command=lambda : self.alterar_item(janela, id, entry_nome, entry_quantidade, entry_tag))
        botao_adicionar.config(bg="#8ab0bd", fg="black", width=15)
        botao_adicionar.pack(side=tk.BOTTOM, pady=25)
    
    def addFrame_Config(self, janela:Tk):
        self.__auxWindow.destroy()
        self.__auxWindow = tk.Frame(janela)
        font = tkFont.Font(family='Arial', size=10, weight='bold')
        self.__auxWindow.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
        tk.Button(self.__auxWindow, text="Fechar", command=lambda : self.closeAuxWindow(janela)).pack(anchor="ne", padx=10, pady=10)
        tk.Label(self.__auxWindow, text='___ Configurações ___', font=font).pack()
        tk.Label(self.__auxWindow, text='Limpar lista de Tags:', font=font).pack()
        botao_remover_tags = tk.Button(self.__auxWindow, text="Limpar", command=self.dellTagFile)
        botao_remover_tags.config(bg="#faa0a1")
        botao_remover_tags.pack(fill=tk.X, padx=15)
        tk.Label(self.__auxWindow, text='Reiniciar tabela:', font=font).pack()
        botao_remover_items = tk.Button(self.__auxWindow, text="Limpar", command=self.dellallItemsFile)
        botao_remover_items.config(bg="#faa0a1")
        botao_remover_items.pack(fill=tk.X, padx=15)
        tk.Label(self.__auxWindow, text='Editar lista de tags:', font=font).pack()
        botao_editar_tags = tk.Button(self.__auxWindow, text="Editar", command =lambda : Tagger.edit())
        botao_editar_tags.config(bg="#8ab0bd")
        botao_editar_tags.pack(fill=tk.X, padx=15)
        
    def closeAuxWindow(self, janela:Tk):
        self.__auxWindow.destroy()
        janela.columnconfigure(0, weight=1)
        janela.rowconfigure(0, weight=1)
        janela.columnconfigure(1, weight=0)
        janela.rowconfigure(1, weight=0)
    
    def adicionar_valor(self, frame:Tk):
        id:int = len(self.__estoque.getList())
        nome:str = self.entry_nome.get()
        quantidade:int = self.entry_quantidade.get()
        tag_id:int = int(self.entry_tag.current())
        
        if nome and quantidade:
            self.tree.insert('', 'end', values=(id, nome, quantidade, TAGS[tag_id]))
            self.entry_nome.delete(0, 'end')
            self.entry_quantidade.delete(0, 'end')
            self.__estoque.add(Produto(id, nome, quantidade, tag_id))
            self.closeAuxWindow(frame)
        else:
            print("Valores não preenchidos")
            
    def alterar_item(self, frame:Tk, id:int, entry_nome:Entry ,entry_quantidade:Entry, entry_tag:ttk.Combobox):
        produto_editado = Produto(id, entry_nome.get(), entry_quantidade.get(), entry_tag.current())
        self.__estoque.getList()[id] = produto_editado
        self.tree.delete(*self.tree.get_children())
        produtos = self.__estoque.getList()
        for produto in produtos:
            self.tree.insert('', 'end', values=(produto.id, produto.nome, produto.quantidade, TAGS[produto.tagId]))
        self.closeAuxWindow(frame)
    
    def filtrarTable(self, event):
        index = self.entry_filter.current()
        self.tree.delete(*self.tree.get_children())
        filterList = ["Todos"] + TAGS
        produtos = self.__estoque.getList()
        for produto in produtos:
            if index == 0 or index == produto.tagId + 1:
                self.tree.insert('', 'end', values=(produto.id, produto.nome, produto.quantidade, TAGS[produto.tagId]))
    
    def dellTagFile(self):
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente apagar todas as Tags? Isso fará TODOS os itens da lista serem removidos")
        if resposta:
            Tagger.clearDB()
            self.__estoque.clearDB()
            self.__window.destroy()
        else: 
            print("Ação cancelada!")
            
    def dellallItemsFile(self):
        resposta = messagebox.askyesno("Confirmação", "Deseja realmente apagar todas as Tags? Isso fará TODOS os itens da lista serem removidos")
        if resposta:
            self.__estoque.clearDB()
            self.tree.delete(*self.tree.get_children())
        else: 
            print("Ação cancelada!")
            
            
    def remover_valor(self):
        selected_item = self.tree.selection()
        if selected_item:
            id_selected = self.tree.item(selected_item)["values"][0]
            resposta = messagebox.askyesno("Confirmação", f'Desesa apagar "{self.__estoque.get(id_selected).nome}" da tabela?')
            if resposta:
                    self.tree.delete(selected_item)
                    self.__estoque.remove(id_selected)
            else: 
                print("Ação cancelada!")
       
            

    def recuperar_valores(self):
        for item in self.tree.get_children():
            valores = self.tree.item(item)['values']
            print(valores)
    
    def close(self):
        self.__estoque.closeList()
        self.__window.destroy()
            
            
Engine("Supermercado Ótimo!Preço")