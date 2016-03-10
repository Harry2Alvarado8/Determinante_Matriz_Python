# [[00,01,02]
# ,[10,11,12],
#  [20,21,22]]


def adjunta(m):
    # lista = []
    adj_1 = ((m[1][1] * m[2][2]) - (m[1][2] * m[2][1]))
    adj_2 = ((m[1][0] * m[2][2]) - (m[1][2] * m[2][0]))
    adj_3 = ((m[1][0] * m[2][1]) - (m[1][1] * m[2][0]))
    adj_4 = ((m[0][1] * m[2][2]) - (m[0][2] * m[2][1]))
    adj_5 = ((m[0][0] * m[2][2]) - (m[0][2] * m[2][0]))
    adj_6 = ((m[0][0] * m[2][1]) - (m[0][1] * m[2][0]))
    adj_7 = ((m[0][1] * m[1][2]) - (m[1][1] * m[0][2]))
    adj_8 = ((m[0][0] * m[1][2]) - (m[1][0] * m[0][2]))
    adj_9 = ((m[0][0] * m[1][1]) - (m[0][1] * m[1][0]))
    adjunta = [[adj_1,adj_2,adj_3],[adj_4,adj_5,adj_6],[adj_7,adj_8,adj_9]]
    return adjunta

# [[00,01,02]
# ,[10,11,12],
#  [20,21,22]]
def traspuesta(m):
    one = m[0][0]
    dos = m[0][1]
    tres = m[0][2]
    cuatro = m[1][0]
    cinco = m[1][1]
    seis = m[1][2]
    siete = m[2][0]
    ocho = m[2][1]
    nueve = m[2][2]
    traspuesta  = [[one,cuatro,siete],[dos,cinco,ocho],[tres,seis,nueve]]
    return traspuesta

def inversa(d,m):
    var1 = m[0][0] / d
    var2 = m[0][1] / d
    var3 = m[0][2] / d
    var4 = m[1][0] / d
    var5 = m[1][1] / d
    var6 = m[1][2] / d
    var7 = m[2][0] / d
    var8 = m[2][1] / d
    var9 = m[2][2] / d
    inver = [[var1,var4,var7],[var2,var5,var8],[var3,var6,var9]]
    return inver
