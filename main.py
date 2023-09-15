# Criando uma calculadora com tkinter
from tkinter import *

# Funções
def limpar() -> None:
    # Deletando tudo que tiver no display
    display.delete(0, END)

def inserir(valor: str) -> None:
    display.insert(END, valor)

def calcular() -> None:
    # Pegando o valor do display
    valor_display = display.get()
    # Calculando o resultado coma a função eval
    # passando o valor do display
    resultado = eval(valor_display)
    limpar()
    # Inserindo o resultado no display
    display.insert(END, str(resultado))



janela = Tk()
janela.title("Calculadora")

# Criando o display/Entry
display = Entry(janela, font="Arial 20 bold",
                fg="white", bg="navy", width=19)
display.pack()

# Criando o frame
frame = Frame(janela)

# Botões
btn_0 = Button(frame, text="0", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("0"))
btn_1 = Button(frame, text="1", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("1"))
btn_2 = Button(frame, text="2", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("2"))
btn_3 = Button(frame, text="3", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("3"))
btn_4 = Button(frame, text="4", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("4"))
btn_5 = Button(frame, text="5", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("5"))
btn_6 = Button(frame, text="6", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("6"))
btn_7 = Button(frame, text="7", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("7"))
btn_8 = Button(frame, text="8", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("8"))
btn_9= Button(frame, text="9", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("9"))
btn_limpar = Button(frame, text="C", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=limpar)
btn_igual = Button(frame, text="=", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=calcular)
btn_somar = Button(frame, text="+", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("+"))
btn_sub = Button(frame, text="-", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("-"))
btn_mult = Button(frame, text="*", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("*"))
btn_div = Button(frame, text="/", bg="orange",
              font="Arial 16 bold", fg="white",
              height=3, width=5, command=lambda: inserir("/"))

frame.pack()

# Primeira Linha
btn_7.grid(row=0, column=0)
btn_8.grid(row=0, column=1)
btn_9.grid(row=0, column=2)
btn_mult.grid(row=0, column=3)

# Segunda linha
btn_4.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)
btn_sub.grid(row=1, column=3)

# Terceira linha
btn_1.grid(row=2, column=0)
btn_2.grid(row=2, column=1)
btn_3.grid(row=2, column=2)
btn_somar.grid(row=2, column=3)

# Quarta linha
btn_limpar.grid(row=3, column=0)
btn_0.grid(row=3, column=1)
btn_igual.grid(row=3, column=2)
btn_div.grid(row=3, column=3)

janela.mainloop()