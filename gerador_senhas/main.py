import tkinter as tk
import random
import string

def gerar():
    try:
        tamanho = int(entry.get())
        if tamanho < 4:
            resultado.config(text="Use no mínimo 4 caracteres")
            return

        chars = string.ascii_letters + string.digits + "!@#$%"
        senha = "".join(random.choice(chars) for _ in range(tamanho))
        resultado.config(text=f"Sua senha: {senha}")
    except:
        resultado.config(text="Digite um número válido")

janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("380x280")
janela.configure(bg="#f4f4f4")

tk.Label(
    janela,
    text="Gerador de Senhas",
    font=("Arial", 18, "bold"),
    bg="#f4f4f4"
).pack(pady=10)

tk.Label(
    janela,
    text="Quantos caracteres sua senha deve ter?",
    bg="#f4f4f4"
).pack()

entry = tk.Entry(janela, font=("Arial", 12), justify="center")
entry.pack(pady=5)

tk.Button(
    janela,
    text="Gerar senha segura",
    bg="#4f4bc4",
    fg="white",
    font=("Arial", 11, "bold"),
    width=22,
    command=gerar
).pack(pady=15)

resultado = tk.Label(
    janela,
    text="A senha aparecerá aqui",
    font=("Arial", 11),
    wraplength=320,
    bg="#f4f4f4"
)
resultado.pack()

janela.mainloop()
