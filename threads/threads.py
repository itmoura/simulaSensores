import time
import random
from connectBd.mongo import connect, _insert, _update

bd = connect()

def threadSensor(user, nomeSensor, first, intervalo):
    while True:
        valorSensor = random.randint(30, 40)
        sensorAlarmado = False
        if valorSensor > 38:
            sensorAlarmado = True

        verUser = bd.find_one({"user": user})

        if first == True and verUser == None:
            _insert(user, nomeSensor, valorSensor, "ºC", sensorAlarmado)
        else:
            _update(user, nomeSensor, valorSensor, "ºC", sensorAlarmado)

        print(nomeSensor, valorSensor)
        if sensorAlarmado:
            print("Atenção! Temperatura Muito Alta, Verifique Sensor", nomeSensor, "!")
            return

        first = False
        time.sleep(intervalo)