import tkinter as tk

ALTURA_COMPACTA = 300
ALTURA_EXPLICACAO = 580

def converter():
    try:
        c = float(entry.get())
        tipo = escolha.get()

        # ===== FAHRENHEIT =====
        if tipo == "F":
            resultado_valor = (c * 9/5) + 32
            unidade = "°F"

            explicacao_texto = (
                "Como funciona a conversão para Fahrenheit:\n"
                f"\nPasso 1: começamos com {c} °C"
                f"\n\nPasso 2: multiplicamos por 9 ÷ 5"
                f"\n       {c} × 9 ÷ 5 = {(c * 9/5):.2f}"
                f"\n\nPasso 3: somamos 32"
                f"\n       {(c * 9/5):.2f} + 32 = {resultado_valor:.2f}"
                f"\n\nResultado final: {resultado_valor:.2f} °F"
            )

            contexto_texto = (
                "Onde essa unidade é usada?\n"
                "O Fahrenheit (°F) é usado principalmente nos "
                "Estados Unidos e no Canadá para informar a "
                "temperatura do clima.\n\n"

            )

        # ===== KELVIN =====
        else:
            if c < -273.15:
                resultado.config(text="Valor inválido")

                explicacao.config(
                    text=(
                        "Conversão para Kelvin não é possível.\n\n"
                        "O Kelvin começa no zero absoluto (0 K).\n"
                        "Isso equivale a -273,15 °C.\n\n"
                        "Não existem temperaturas menores que isso."
                    )
                )

                contexto.config(
                    text=(
                        "Curiosidade:\n"
                        "O zero absoluto é a menor temperatura possível "
                        "na física. Nesse ponto, as partículas quase "
                        "não se movem."
                    )
                )

                janela.geometry(f"400x{ALTURA_EXPLICACAO}")
                btn_limpar.pack(pady=5)
                return

            resultado_valor = c + 273.15
            unidade = "K"

            explicacao_texto = (
                "Como funciona a conversão para Kelvin:\n"
                f"\nPasso 1: começamos com {c} °C"
                f"\n\nPasso 2: somamos 273.15"
                f"\n       {c} + 273.15 = {resultado_valor:.2f}"
                f"\n\nResultado final: {resultado_valor:.2f} K"
            )

            contexto_texto = (
                "Onde essa unidade é usada?\n"
                "O Kelvin (K) é usado principalmente em ciência, "
                "como na física e na química.\n\n"
                "Curiosidade:\n"
                "No Kelvin, não existem temperaturas negativas."
            )

        # ===== EXIBIÇÃO FINAL =====
        resultado.config(text=f"{resultado_valor:.2f} {unidade}")
        explicacao.config(text=explicacao_texto)
        contexto.config(text=contexto_texto)

        janela.geometry(f"400x{ALTURA_EXPLICACAO}")
        btn_limpar.pack(pady=5)

    except:
        resultado.config(text="Digite um valor válido")
        explicacao.config(text="")
        contexto.config(text="")
        janela.geometry(f"400x{ALTURA_COMPACTA}")

def limpar():
    entry.delete(0, tk.END)
    resultado.config(text="Resultado")
    explicacao.config(text="")
    contexto.config(text="")
    janela.geometry(f"400x{ALTURA_COMPACTA}")
    btn_limpar.pack_forget()

# ===== JANELA =====
janela = tk.Tk()
janela.title("Conversor de Temperatura")
janela.geometry(f"400x{ALTURA_COMPACTA}")
janela.configure(bg="#f4f4f4")
janela.resizable(False, False)

# ===== TÍTULO =====
tk.Label(
    janela,
    text="Conversor de Temperatura",
    font=("Arial", 18, "bold"),
    bg="#f4f4f4"
).pack(pady=10)

# ===== ENTRADA =====
tk.Label(
    janela,
    text="Temperatura em Celsius",
    bg="#f4f4f4"
).pack()

entry = tk.Entry(janela, font=("Arial", 12), justify="center")
entry.pack(pady=5)

# ===== OPÇÕES =====
escolha = tk.StringVar(value="F")

frame_opcoes = tk.Frame(janela, bg="#f4f4f4")
frame_opcoes.pack(pady=5)

tk.Radiobutton(
    frame_opcoes,
    text="Fahrenheit (°F)",
    variable=escolha,
    value="F",
    bg="#f4f4f4"
).pack(side="left", padx=10)

tk.Radiobutton(
    frame_opcoes,
    text="Kelvin (K)",
    variable=escolha,
    value="K",
    bg="#f4f4f4"
).pack(side="left", padx=10)

# ===== BOTÃO CONVERTER =====
tk.Button(
    janela,
    text="Converter",
    bg="#4f4bc4",
    fg="white",
    font=("Arial", 11, "bold"),
    width=22,
    command=converter
).pack(pady=10)

# ===== RESULTADO =====
resultado = tk.Label(
    janela,
    text="Resultado",
    font=("Arial", 14, "bold"),
    bg="#f4f4f4"
)
resultado.pack(pady=5)

# ===== EXPLICAÇÃO =====
explicacao = tk.Label(
    janela,
    text="",
    font=("Arial", 11),
    bg="#ffffff",
    justify="left",
    wraplength=360
)
explicacao.pack(padx=15, pady=10, fill="both")

# ===== CONTEXTO =====
contexto = tk.Label(
    janela,
    text="",
    font=("Arial", 10),
    bg="#eef1f7",
    fg="#333333",
    justify="left",
    wraplength=360
)
contexto.pack(padx=15, pady=(0, 10), fill="both")

# ===== BOTÃO LIMPAR =====
btn_limpar = tk.Button(
    janela,
    text="Limpar",
    bg="#cccccc",
    width=12,
    command=limpar
)

janela.mainloop()
