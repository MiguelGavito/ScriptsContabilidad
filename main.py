from simple_term_menu import TerminalMenu

# lista de opciones 
options = [
    "Convertir Estado de Cuenta PDF a Excel",
    "Buscar Movimientos Faltantes",
    "Exportar Templates Excel",
    "Salir"
    ]

# banderas
quitting = False
convert = False

# Las opciones del menu y el titulo del menu
mainMenu = TerminalMenu(
    options, 
    title = "~ Seleccione que quiere hacer ~"
    )

# Submenu de los bancos
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

    # opciones en el Menu Principal
    if optionsChoice == "Salir":
        quitting = True
    if optionsChoice == "Convertir Estado de Cuenta PDF a Excel":
        subMenuBank.show()


    # opciones en el Submenu Convert
    if optionsChoice == "BBVA":
        #ejecutar funcion para template BBVA
        print(optionsChoice)

    # opciones en el Submenu Comparar Excels

    # opciones en el Submenu Export Excel
    else:
        print(optionsChoice)