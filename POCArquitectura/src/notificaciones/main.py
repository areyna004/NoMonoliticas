from pulsar import Client, AuthenticationToken
from avro.schema import Parse
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
import io, sys, json
import mysql.connector
from datetime import datetime

comando_schema = Parse(open("src/notificaciones/schema/v1/propiedad.avsc").read())

def consumir_comandos():
    client = Client('pulsar://10.182.0.2:6650')
    consumer_comandos_propiedades = client.subscribe('persistent://public/default/comandos-propiedades', 'subscripcion-1')
    consumer_eventos_propiedades = client.subscribe('persistent://public/default/eventos-propiedades', 'subscripcion-2')
    consumer_compensacion_propiedades = client.subscribe('persistent://public/default/compensacion-propiedades', 'subscripcion-3')
    producer_notif_propiedad = client.create_producer('persistent://public/default/eventos-notificaciones') 
    producer_notif_propiedad = client.create_producer('persistent://public/default/eventos-notificaciones') 

    while True:
        msg1 = consumer_comandos_propiedades.receive()
        
        try:
            consumer_comandos_propiedades.acknowledge(msg1)
            bytes_io = io.BytesIO(msg1.data())
            decoder = BinaryDecoder(bytes_io)
            reader = DatumReader(comando_schema)
            comando_data = reader.read(decoder)
            print("Comando recibido:", comando_data)
            changelog("Comando recibido:"+ str(comando_data))
        except Exception as e:
            print("Error al procesar el comando:", e)
            consumer_comandos_propiedades.negative_acknowledge(msg1)
        
        msg2 = consumer_eventos_propiedades.receive()

        try: 
            consumer_eventos_propiedades.acknowledge(msg2)
            data = json.loads(msg2.data().decode('utf-8'))
            print("Evento recibido:", data)
            changelog("Evento recibido:" + str(data))
            
            if data['nombre'] != 'Casa Repetida':
                
                producer_notif_propiedad.send(msg2.data())
        
        except Exception as e:
            print("Error al procesar el evento:", e)
            consumer_comandos_propiedades.negative_acknowledge(msg2)

        msg3 = consumer_compensacion_propiedades.receive()
        
        try: 
            consumer_compensacion_propiedades.acknowledge(msg3)
            data = json.loads(msg3.data().decode('utf-8'))
            print("Evento de Compensacion recibido:", data)
            changelog("Compensacion recibida:" + str(data))
            producer_notif_propiedad.send(msg3.data())
        
        except Exception as e:
            print("Error al procesar el evento:", e)
            consumer_comandos_propiedades.negative_acknowledge(msg2)

def changelog(evento):
    conn = mysql.connector.connect(
        host='34.66.105.29',
        user='root',
        password='U6yEZgrAjc6c1olP',
        database='deb-eventos'
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS eventos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            evento TEXT,
            hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()

    cursor.execute('INSERT INTO eventos (evento) VALUES (%s)', (evento,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    consumir_comandos()
