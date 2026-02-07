import tkinter as tk

ALTURA_COMPACTA = 360
ALTURA_EXPLICACAO = 520

def calcular(op):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())

        if op == "+":
            r = n1 + n2
            sinal = "+"
        elif op == "-":
            r = n1 - n2
            sinal = "-"
        elif op == "*":
            r = n1 * n2
            sinal = "×"
        elif op == "/":
            r = n1 / n2
            sinal = "÷"

        resultado.config(text=f"Resultado: {r}")

        explicacao.config(
            text=(
                "Como o cálculo funciona:\n"
                f"\nPasso 1: usamos os números {n1} e {n2}\n"
                f"\nPasso 2: aplicamos a operação {sinal}\n"
                f"\nConta: {n1} {sinal} {n2}\n"
                f"\nResultado final: {r}"
            )
        )

        janela.geometry(f"380x{ALTURA_EXPLICACAO}")

    except:
        resultado.config(text="Erro")
        explicacao.config(text="Digite dois números válidos")
        janela.geometry(f"380x{ALTURA_COMPACTA}")

def limpar():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    resultado.config(text="Resultado aparecerá aqui")
    explicacao.config(text="")
    janela.geometry(f"380x{ALTURA_COMPACTA}")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry(f"380x{ALTURA_COMPACTA}")
janela.configure(bg="#f4f4f4")
janela.resizable(False, False)

tk.Label(janela, text="Calculadora",
         font=("Arial", 18, "bold"),
         bg="#f4f4f4").pack(pady=10)

tk.Label(janela, text="Primeiro número", bg="#f4f4f4").pack()
entry1 = tk.Entry(janela, font=("Arial", 12), justify="center")
entry1.pack(pady=5)

tk.Label(janela, text="Segundo número", bg="#f4f4f4").pack()
entry2 = tk.Entry(janela, font=("Arial", 12), justify="center")
entry2.pack(pady=5)

frame = tk.Frame(janela, bg="#f4f4f4")
frame.pack(pady=10)

btn = {
    "font": ("Arial", 12, "bold"),
    "width": 6,
    "bg": "#4f4bc4",
    "fg": "white"
}

tk.Button(frame, text="+", command=lambda: calcular("+"), **btn).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="-", command=lambda: calcular("-"), **btn).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="×", command=lambda: calcular("*"), **btn).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="÷", command=lambda: calcular("/"), **btn).grid(row=1, column=1, padx=5, pady=5)

resultado = tk.Label(janela, text="Resultado aparecerá aqui",
                     font=("Arial", 13, "bold"),
                     bg="#f4f4f4")
resultado.pack(pady=10)

explicacao = tk.Label(janela, text="",
                      font=("Arial", 11),
                      bg="#ffffff",
                      justify="left",
                      wraplength=340)
explicacao.pack(padx=15, pady=10, fill="both")

tk.Button(janela, text="Limpar",
          bg="#cccccc",
          width=12,
          command=limpar).pack(pady=5)

janela.mainloop()
