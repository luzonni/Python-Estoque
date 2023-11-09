import os
import tkinter as tk
from tkinter import * 
from tkinter import ttk
import tkinter.font as tkFont

class Tagger:
    
    def __init__(self, path:str):
        self.__path = path
    
    def getTags(self):
        self.__listTags = []
        if os.path.exists(self.__path):
            with open(self.__path, 'r') as arquivo:
                text = arquivo.read().split("/")
                for item in text:
                    self.__listTags.append(item)
            return self.__listTags[0: len(self.__listTags)-1]
        else:
            self.start()
            return self.__listTags

    def closeList(self):
        with open(self.__path, 'w') as arquivo:
            arquivo.write(self.changeToFile(self.__listTags))
        self.__window.destroy()
    
    def changeToFile(self, tagsArray):
        line = ""
        for tag in tagsArray:
            line += tag + "/"
        return line
    
    def start(self):
        self.__window = tk.Tk()
        self.__window.title("Adicionar/Remover Tags")
        self.__window.configure(bg='#363f4e')
        self.__window.minsize(500, 100)
        self.__window.resizable(width=False, height=False)
        font = tkFont.Font(family='Arial', size=14, weight='bold')
        framedireitafont = tkFont.Font(family='Arial', size=10)
        frame_esquerda = tk.Frame(self.__window)
        frame_esquerda.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        frame_direita = tk.Frame(self.__window)
        frame_direita.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.__tree = ttk.Treeview(frame_esquerda, columns=('TAG'), show='headings')
        self.__tree.heading('#1', text='Tags')
        self.__tree.column('#1', width=100)
        self.__tree.pack(fill=tk.BOTH)
        self.__window.columnconfigure(0, weight=1)
        self.__window.columnconfigure(1, weight=1)
        self.__window.rowconfigure(0, weight=1)
        label_nome_tag = tk.Label(frame_direita, text='Tag:', font=framedireitafont)
        label_nome_tag.pack()
        self.__entry_nome_tag = tk.Entry(frame_direita)
        self.__entry_nome_tag.pack(fill=tk.X)
        botao_adicionar_tag = tk.Button(frame_direita, text="Adicionar", command=self.adicionar_tag)
        botao_adicionar_tag.config(bg="#2b323e", fg="white", width=15)
        botao_adicionar_tag.pack(side="top", padx=10, pady=5)
        botao_remover_tag = tk.Button(frame_direita, text="Remover", command=self.remover_tag)
        botao_remover_tag.config(bg="#2b323e", fg="white", width=15)
        botao_remover_tag.pack(side="top", padx=10, pady=5)
        botao_finish = tk.Button(frame_direita, text="Salvar", command=self.closeList)
        botao_finish.config(bg="#2b323e", fg="white", width=15)
        botao_finish.pack(side="top", padx=10, pady=5)
        coluna_style = ttk.Style()
        coluna_style.configure("Treeview", rowheight=25, background="#cad5e8", font=('Arial', 10))
        # self.__window.protocol("WM_DELETE_WINDOW", self.closeList)
        self.__window.mainloop()

    def adicionar_tag(self):
        valor = self.__entry_nome_tag.get()
        print(valor)
        if valor:
            self.__tree.insert('', tk.END, values=(valor,))
            self.__entry_nome_tag.delete(0, 'end')
            self.__listTags.append(valor)

    def remover_tag(self):
        selected_item = self.__tree.selection()
        index_selected = self.__tree.index(selected_item[0])
        if selected_item:
            self.__listTags.remove(self.__listTags[index_selected])
            self.__tree.delete(selected_item)
            
    

