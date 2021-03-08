# Tugas Montercarlo M.Razhaldy Ihza.D 152018086 C    #

import random

def predict(banyak, down, up, hrg):
    ttl1 = 0
    ttl2 = 0
    data = []
    out = []
    for i in range(banyak):
        data.append(random.random())
    for i in range(banyak):
        if (data[i] >= down[0]) and (data[i] <= up[0]):
            n=0
        elif (data[i] >= down[1]) and (data[i] <= up[1]):
            n=1
        elif (data[i] >= down[2]) and (data[i] <= up[2]):
            n=2
        elif (data[i] >= down[3]) and (data[i] <= up[3]):
            n=3
        elif (data[i] >= down[4]) and (data[i] <= up[4]):
            n=4
        elif (data[i] >= down[5]) and (data[i] <= up[5]):
            n=5
        elif (data[i] >= down[6]) and (data[i] <= up[6]):
            n=6
            
        out.append(n)
    data = []
    for i in  range(len(out)):
        ttl1 += out[i]
        n = out[i] * hrg
        ttl2 += n
    print('Jumlah Permintaan Berdasarkan Predict = ', ttl1, 'pcs')
    print('Pengeluaran Modal Berdasarkan Predict = Rp.',ttl2)

def inputdata():
    while True:
        masuk1 = input('Permintaan = ')
        masuk2 = input('Minggu : ')
        if (masuk1 == '') and (masuk1 == ''):
                break
        try:
            datain.append((int(masuk1),int(masuk2)))
        except:
            print("Input Yang Benar")

def interval(kumulatif):
    up = []
    down = []
    down.append(0)
    for i in range((len(kumulatif))-1):
        n = kumulatif[i] + 0.001
        down.append(n)
    for i in range((len(kumulatif))):
        n = kumulatif[i]
        up.append(n)
    return down, up
    
def prob():
    ftot = 0
    out = []
    for i in range(len(datain)):
        ftot += datain[i][1]
    for i in range(len(datain)):
        n = datain[i][1] / ftot
        out.append(n)
    return out

def probkum(inprobabilitas):
    out = []
    out.append(inprobabilitas[0])
    pjng = len(inprobabilitas) - 1
    for i in range(pjng):
        n = out[i] + inprobabilitas[i+1]
        out.append(round(n,1))
    return out





datain = []
inputdata()
alpha = prob()
beta = probkum(alpha)
bo, ab = interval(beta)[:2]
npredict = int(input('Masukkan banyak prediksi: '))
price = int(input('Tentukan modal barang: '))
print('== Prediksi Dengan MonteCarlo ==')
predict(npredict, bo, ab, price)
