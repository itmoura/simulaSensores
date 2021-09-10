from pymongo import MongoClient

def connect():
    client = MongoClient('mongodb+srv://itmoura:hBz6wleAuUgJj195@cluster0.grf7r.mongodb.net/test?authSource=admin&replicaSet=atlas-4pytg9-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')

    db = client['bancoiot']

    return db.sensores

def _insert(user, nomeSensor, valorSensor, unidadeMedida, sensorAlarmado):
    connect().insert(
        {
            "user": user,
            "nomeSensor": nomeSensor,
            "valorSensor": valorSensor,
            "unidadeMedida": unidadeMedida,
            "sensorAlarmado": sensorAlarmado
        }
    )

def _update(user, nomeSensor, valorSensor, unidadeMedida, sensorAlarmado):
    connect().update(
            {"user": user, "nomeSensor": nomeSensor},
            {
                "user": user,
                "nomeSensor": nomeSensor,
                "valorSensor": valorSensor,
                "unidadeMedida": unidadeMedida,
                "sensorAlarmado": sensorAlarmado
            }
    )