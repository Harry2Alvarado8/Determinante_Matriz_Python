def Ingreso_de_Matriz():
    repet = 0
    c = 0
    ROW_first = []
    ROW_second = []
    ROW_third = []
    Matriz3x3 = []
    print "Ingrese Numeros:\n"
    while repet < 3:
        m = int(raw_input("Posicion row 1 column %d ::> \t" % (c + 1)))
        ROW_first.append(m)
        repet += 1
        c += 1

    repet = 0
    c = 0
    while repet < 3:
        m = int(raw_input("Posicion row 2 column %d ::> \t" % (c + 1)))
        ROW_second.append(m)
        repet += 1
        c += 1

    repet = 0
    c = 0
    while repet < 3:
        m = int(raw_input("Posicion row 3 column %d ::> \t" % (c + 1)))
        ROW_third.append(m)
        repet += 1
        c += 1

    Matriz3x3.append(ROW_first)
    Matriz3x3.append(ROW_second)
    Matriz3x3.append(ROW_third)

    return Matriz3x3




def Determinante_Matriz3x3(m):
    det_first = m[0][0] * ((m[1][1] * m[2][2]) - (m[1][2] * m[2][1]))
    det_second = m[0][1] * ((m[1][0] * m[2][2]) - (m[1][2] * m[2][0]))
    det_third = m[0][2] * ((m[1][0] * m[2][1]) - (m[1][1] * m[2][0]))

    Det_Matriz3x3 = det_first - det_second + det_third
    return Det_Matriz3x3



M = Ingreso_de_Matriz()
print "Tu matriz a sido: ",M
eureca = Determinante_Matriz3x3(M)
print "El resultado de la determinante de esta matriz es : ", eureca
if eureca == 0:
    print "Estas matriz no podria ser inversa debido a que \nla determinante de la matriz es cero."
