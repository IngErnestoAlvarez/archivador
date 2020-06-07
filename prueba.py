from ventana import App

def main():
    app = App("Cualquier nombre")

    app.mainloop()

    print(app.nombre)
    print(app.mes)
    print(app.anio)
    print(app.tipo)

if __name__ == "__main__":
    main()