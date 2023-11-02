def mapa(n):
    matriz = []

    for i in range(n):      
        fila = []
   
        for j in range(n):
            fila.append(0)

        matriz.append(fila)
    return jugar(matriz)

def mostrar(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            print(mapa[i][j], end="")
        print("")

def poner(mapa, pj):
    
    while True:

        fila = int(input("Ingrese la fila en la que quiere ingresar su ficha, desde 0 - " + str(len(mapa)-1) + " : ")) 
        columna = int(input("Ingrese la columna en la que quiere ingresar su ficha, desde 0 - " + str(len(mapa)-1) + " : "))
            
        if  0 <= fila < len(mapa):
            if  0 <= columna < len(mapa):

                if mapa[fila][columna] == 0:
                    mapa[fila][columna] = pj
                    return mapa
                else:
                    print("La casilla esta ocupada. Intente Nuevamente")
                
            else:
                print("La columna es invalida. Intente nuevamente")
        else:
            print("La fila es invalida. Intente nuevamente")

def salir():
    pass

def jugar(mapa):
    p1 = 1
    p2 = 6
    turno = 0

    while True:
            
        if turno % 2 == 0:
            txt = "1"
            pj = p1
        else:
            txt = "2"
            pj = p2
        
        mostrar(mapa)
        mapa = poner(mapa, pj)
        if verificar(mapa, p1, p2, turno):
            print("Felicidades jugador " + txt + ", has ganado.")
            return 
        

        turno += 1

def verificar(mapa, p1, p2, turno):
    if turno % 2 == 0:
        x = p1 * len(mapa)
    else:
        x = p2 * len(mapa)
    
    vertical = 0
    horizontal = 0
    diagonal = 0
    diagonalInv = 0

    for i in range(len(mapa)):

        inv = len(mapa) - i - 1  
        if 0 <= inv < len(mapa):
            diagonalInv += mapa[i][inv]

        for j in range(len(mapa)):
            horizontal += mapa[i][j]
            vertical += mapa[j][i]
            if i == j:
                diagonal += mapa[i][j]
    
    if vertical == x or horizontal == x or diagonal == x or diagonalInv == x:
        return True
    else:
        return False

def eleccion():
    while True:
        n = input("Ingrese la cantidad de largo y ancho que quiere que tenga el tablero: ")
        
        try:
            n = int(n)

            if n > 20:
                print("No puede ser mayor a 20. Intente nuevamente.")
            elif n < 3:
                print("No puede ser menor a 3. Intente nuevamente.")
            else:
                return mapa(n)
        
        except ValueError:
            if n == '':
                print("Tiene que ingresar un valor. Intente nuevamente.")
            else:
                print("No puede ingresar letras. Intente nuevamente.")
    
    

def start():
    return eleccion()

if __name__ == "__main__":
    start()
