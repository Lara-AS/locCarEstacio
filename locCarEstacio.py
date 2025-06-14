from tkinter import *
from tkinter import messagebox
import os

ARQ_VEICULOS = "veiculos.txt"
ARQ_MOTORISTAS = "motoristas.txt"
ARQ_MOVIMENTACOES = "movimentacoes.txt"

def salvar_linha(arq, dado):
    with open(arq, "a") as f:
        f.write(str(dado) + "\n")

def carregar_lista(arq):
    if not os.path.exists(arq):
        return []
    with open(arq, "r") as f:
        return [eval(l.strip()) for l in f.readlines()]

def janela_padrao(titulo, largura=610, altura=600):
    janela = Toplevel()
    janela.title(titulo)
    janela.geometry(f"{largura}x{altura}")
    janela.configure(bg="#e6f2ff")
    Label(janela, text="LocCarEstácio", font=("Arial", 14, "bold"), fg="#003366", bg="#e6f2ff").pack(pady=10)
    return janela

def listar_dados(arq, titulo, campos):
    janela = janela_padrao(titulo)
    txt = Text(janela, wrap=WORD, font=("Courier New", 10))
    txt.pack(expand=True, fill="both")

    dados = carregar_lista(arq)
    for d in dados:
        for c in campos:
            txt.insert(END, f"{c}: {d.get(c, '')}\n")
        txt.insert(END, "\n")

    return janela

def visualizar_motoristas():
    janela = listar_dados(ARQ_MOTORISTAS, "Motoristas Cadastrados", ["Nome", "CPF", "CNH", "Telefone"])
    Button(janela, text="Adicionar Motorista", width=25, command=cadastrar_motorista).pack(pady=10)

def visualizar_veiculos():
    janela = listar_dados(ARQ_VEICULOS, "Veículos Cadastrados", ["Placa", "Modelo", "Ano"])
    Button(janela, text="Adicionar Veículo", width=25, command=cadastrar_veiculo).pack(pady=10)

def visualizar_movimentacoes():
    janela = listar_dados(ARQ_MOVIMENTACOES, "Movimentações de Veículos", ["Motorista", "Veiculo"])
    Button(janela, text="Registrar Movimentação", width=25, command=movimentar_veiculo).pack(pady=10)

def visualizar_contas():
    janela = janela_padrao("Contas dos Veículos")
    txt = Text(janela, wrap=WORD, font=("Courier New", 10))
    txt.pack(expand=True, fill="both")

    veiculos = carregar_lista(ARQ_VEICULOS)
    for v in veiculos:
        txt.insert(END, f"Veículo: {v['Placa']}\n")
        txt.insert(END, "Contas:\n")
        contas = v.get("Contas", {})
        if contas:
            for k, val in contas.items():
                txt.insert(END, f"- {k}: {val}\n")
        else:
            txt.insert(END, "Sem contas registradas.\n")
        txt.insert(END, "\n")

    Button(janela, text="Adicionar Contas", width=25, command=controle_contas).pack(pady=10)

def cadastrar_motorista():
    janela = janela_padrao("Cadastro de Motorista")

    campos = ["Nome", "CPF", "CNH", "Telefone"]
    entradas = {}
    for campo in campos:
        Label(janela, text=f"{campo}:", bg="#e6f2ff").pack()
        entrada = Entry(janela, width=35)
        entrada.pack()
        entradas[campo] = entrada

    def salvar():
        if all(entradas[c].get() for c in campos):
            m = {c: entradas[c].get() for c in campos}
            salvar_linha(ARQ_MOTORISTAS, m)
            messagebox.showinfo("Sucesso", "Motorista cadastrado!")
            janela.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    Button(janela, text="Salvar", width=20, command=salvar).pack(pady=15)

def cadastrar_veiculo():
    janela = janela_padrao("Cadastro de Veículo")

    campos = ["Placa", "Modelo", "Ano"]
    entradas = {}
    for campo in campos:
        Label(janela, text=f"{campo}:", bg="#e6f2ff").pack()
        entrada = Entry(janela, width=35)
        entrada.pack()
        entradas[campo] = entrada

    def salvar():
        if all(entradas[c].get() for c in campos):
            v = {
                "Placa": entradas["Placa"].get().upper(),
                "Modelo": entradas["Modelo"].get(),
                "Ano": entradas["Ano"].get(),
                "Contas": {},
                "Multas": []
            }
            salvar_linha(ARQ_VEICULOS, v)
            messagebox.showinfo("Sucesso", "Veículo cadastrado!")
            janela.destroy()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    Button(janela, text="Salvar", width=20, command=salvar).pack(pady=15)

def movimentar_veiculo():
    motoristas = carregar_lista(ARQ_MOTORISTAS)
    veiculos = carregar_lista(ARQ_VEICULOS)
    if not motoristas or not veiculos:
        messagebox.showwarning("Aviso", "Cadastre motoristas e veículos antes.")
        return

    janela = janela_padrao("Registrar Movimentação")

    Label(janela, text="Selecionar Motorista:", bg="#e6f2ff").pack()
    motorista = StringVar()
    OptionMenu(janela, motorista, *[m["Nome"] for m in motoristas]).pack()

    Label(janela, text="Selecionar Veículo:", bg="#e6f2ff").pack()
    veiculo = StringVar()
    OptionMenu(janela, veiculo, *[v["Placa"] for v in veiculos]).pack()

    def salvar():
        if motorista.get() and veiculo.get():
            m = {"Motorista": motorista.get(), "Veiculo": veiculo.get()}
            salvar_linha(ARQ_MOVIMENTACOES, m)
            messagebox.showinfo("Sucesso", "Movimentação registrada!")
            janela.destroy()
        else:
            messagebox.showwarning("Erro", "Selecione motorista e veículo.")

    Button(janela, text="Registrar", width=20, command=salvar).pack(pady=15)

def controle_contas():
    veiculos = carregar_lista(ARQ_VEICULOS)
    if not veiculos:
        messagebox.showwarning("Aviso", "Nenhum veículo cadastrado.")
        return

    janela = janela_padrao("Adicionar Contas")

    Label(janela, text="Selecionar Veículo:", bg="#e6f2ff").pack()
    placa_var = StringVar()
    OptionMenu(janela, placa_var, *[v["Placa"] for v in veiculos]).pack()

    def campo_rotulo(label_text):
        Label(janela, text=label_text, bg="#e6f2ff").pack()
        campo = Entry(janela, width=30)
        campo.pack()
        return campo

    ipva = campo_rotulo("IPVA:")
    seguro = campo_rotulo("Seguro:")
    licenciamento = campo_rotulo("Licenciamento:")
    troca = campo_rotulo("Troca de óleo:")
    revisao = campo_rotulo("Revisão:")

    def salvar():
        atualizados = []
        achou = False
        for v in veiculos:
            if v["Placa"] == placa_var.get():
                v["Contas"] = {
                    "IPVA": ipva.get(),
                    "Seguro": seguro.get(),
                    "Licenciamento": licenciamento.get(),
                    "Troca_oleo": troca.get(),
                    "Revisao": revisao.get()
                }
                achou = True
            atualizados.append(v)

        if achou:
            with open(ARQ_VEICULOS, "w") as f:
                for v in atualizados:
                    f.write(str(v) + "\n")
            messagebox.showinfo("Salvo", "Contas atualizadas!")
            janela.destroy()
        else:
            messagebox.showwarning("Erro", "Veículo não encontrado.")

    Button(janela, text="Salvar Contas", width=20, command=salvar).pack(pady=10)

def visualizar_multas():
    janela = janela_padrao("Multas e Registro")
    txt = Text(janela, wrap=WORD, font=("Courier New", 10))
    txt.pack(expand=True, fill="both")

    veiculos = carregar_lista(ARQ_VEICULOS)
    for v in veiculos:
        txt.insert(END, f"Veículo: {v['Placa']}\n")
        txt.insert(END, "Multas:\n")
        if v["Multas"]:
            for m in v["Multas"]:
                txt.insert(END, f"- {m}\n")
        else:
            txt.insert(END, "Sem multas registradas.\n")
        txt.insert(END, "\n")

    Button(janela, text="Adicionar Multa", width=25, command=registrar_multa).pack(pady=10)

def registrar_multa():
    motoristas = carregar_lista(ARQ_MOTORISTAS)
    veiculos = carregar_lista(ARQ_VEICULOS)
    if not motoristas or not veiculos:
        messagebox.showwarning("Aviso", "Cadastre motoristas e veículos antes.")
        return

    janela = janela_padrao("Registrar Multa")

    placa = StringVar()
    Label(janela, text="Placa:", bg="#e6f2ff").pack()
    OptionMenu(janela, placa, *[v["Placa"] for v in veiculos]).pack()

    motorista = StringVar()
    Label(janela, text="Motorista:", bg="#e6f2ff").pack()
    OptionMenu(janela, motorista, *[m["Nome"] for m in motoristas]).pack()

    valor = Entry(janela, width=30)
    Label(janela, text="Valor:", bg="#e6f2ff").pack()
    valor.pack()

    local = Entry(janela, width=30)
    Label(janela, text="Local:", bg="#e6f2ff").pack()
    local.pack()

    data = Entry(janela, width=30)
    Label(janela, text="Data:", bg="#e6f2ff").pack()
    data.pack()

    def salvar():
        atualizados = []
        achou = False
        for v in veiculos:
            if v["Placa"] == placa.get():
                m = f"R${valor.get()} - {local.get()} - {data.get()} - Motorista: {motorista.get()}"
                v["Multas"].append(m)
                achou = True
            atualizados.append(v)

        if achou:
            with open(ARQ_VEICULOS, "w") as f:
                for v in atualizados:
                    f.write(str(v) + "\n")
            messagebox.showinfo("Salvo", "Multa registrada!")
            janela.destroy()
        else:
            messagebox.showwarning("Erro", "Veículo não encontrado.")

    Button(janela, text="Registrar Multa", width=20, command=salvar).pack(pady=10)

root = Tk()
root.title("Sistema LocCarEstácio")
root.geometry("300x550")
root.configure(bg="#e6f2ff")

Label(root, text="LocCarEstácio", font=("Arial", 14, "bold"), fg="#003366", bg="#e6f2ff").pack(pady=10)
Label(root, text="Menu do Sistema", font=("Arial", 11), bg="#e6f2ff").pack(pady=5)

Button(root, text="Motoristas (Ver e Adicionar)", width=25, command=visualizar_motoristas).pack(pady=5)
Button(root, text="Veículos (Ver e Adicionar)", width=25, command=visualizar_veiculos).pack(pady=5)
Button(root, text="Movimentações (Ver e Adicionar)", width=25, command=visualizar_movimentacoes).pack(pady=5)
Button(root, text="Contas (Ver e Adicionar)", width=25, command=visualizar_contas).pack(pady=5)
Button(root, text="Multas (Ver e Adicionar)", width=25, command=visualizar_multas).pack(pady=5)

root.mainloop()
