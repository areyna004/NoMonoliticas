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
    consumer_consultas_propiedades = client.subscribe('persistent://public/default/eventos-propiedades', 'subscripcion-3')
    
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
            consumer_comandos_propiedades.acknowledge(msg1)
        except Exception as e:
            print("Error al procesar el comando:", e)
            consumer_comandos_propiedades.negative_acknowledge(msg1)
        
        msg2 = consumer_eventos_propiedades.receive()
        try: 
            data = json.loads(msg2.data().decode('utf-8'))
            print("Evento recibido:", data)
            changelog("Evento recibido:" + str(data))
            consumer_eventos_propiedades.acknowledge(msg2)
            client = Client('pulsar://10.182.0.2:6650')
            producer_comandos_propiedad = client.create_producer('persistent://public/default/eventos-notificaciones', chunking_enabled=True) 
            producer_comandos_propiedad.send(msg2.data())
            client.close()
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
