import threading

from threads.threads import threadSensor

# Para rodar projeto, executar -> python -m pip install 'pymongo[srv]'
# Configurar -- Como coloquei banco online, resolvi que cada usuário poderá ter a sua medida,
#               assim não fazendo o sensor do outro parar de ler
user = input("Entre com seu nome para configurar seu banco: ")

# Chamando as threads
sensor1 = threading.Thread(target=threadSensor, args=(user, "Temperatura_1", True, 2))
sensor2 = threading.Thread(target=threadSensor, args=(user, "Temperatura_2", True, 2))
sensor3 = threading.Thread(target=threadSensor, args=(user, "Temperatura_3", True, 2))

sensor1.start()
sensor2.start()
sensor3.start()