from simple_term_menu import TerminalMenu

options = [
    "Convertir Estado de Cuenta PDF a Excel",
    "Buscar Movimientos Faltantes",
    "Exportar Templates Excel",
    "Salir"
    ]

quitting = False

mainMenu = TerminalMenu(
    options, 
    title = "~ Seleccione que quiere hacer ~"
    )

subMenuBank = TerminalMenu(
    [
        "BBVA",
        "Banamex",
        "Banregio",
        "Banorte"
    ],
    title = "Escoge el Banco del Estado de Cuenta"
    )

while quitting == False:
    optionsIndex = mainMenu.show()
    optionsChoice = options[optionsIndex]

    if optionsChoice == "Salir":
        quitting = True
    if optionsChoice == "Convertir Estado de Cuenta PDF a Excel":
        subMenuBank.show()
    else:
        print(optionsChoice)