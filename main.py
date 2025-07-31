from simple_term_menu import TerminalMenu

options = [
    "Convertir Estado de Cuenta PDF a Excel",
    "Buscar Movimientos Faltantes",
    "Exportar Templates Excel",
    "Salir"
    ]

quitting = False

mainMenu = TerminalMenu(options)

while quitting == False:
    optionsIndex = mainMenu.show()
    optionsChoice = options[optionsIndex]

    if optionsChoice == "Salir":
        quitting = True
    else:
        print(optionsChoice)