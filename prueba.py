from ventana import App

def main():
    app = App("Cualquier nombre")

    app.mainloop()

    print(app.nombre.get())
    print(app.mes.get())
    print(app.anio.get())
    print(app.tipo.get())
    print(app.impuesto.get())

if __name__ == "__main__":
    main()