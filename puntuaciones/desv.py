import statistics

serie = []  # aquí debes reemplazar los puntos suspensivos con los 50 números aleatorios

desviaciones = []

for i in range(8, len(serie)):
    subserie = serie[i-8:i+1]
    desviacion = statistics.stdev(subserie)
    desviaciones.append(str(serie[i]) + " / " + str(desviacion))

print(desviaciones)