from pulsar import Client, AuthenticationToken
from avro.schema import Parse
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
import io, sys, json

comando_schema = Parse(open("src/notificaciones/schema/v1/propiedad-comando.avsc").read())
evento_schema = Parse(open("src/notificaciones/schema/v1/propiedad-evento.avsc").read())

def consumir_comandos():
    client = Client('pulsar://127.0.0.1:6650')
    consumer_comandos_propiedades = client.subscribe('persistent://public/default/comandos-propiedades', 'subscripcion-1')
    consumer_eventos_propiedades = client.subscribe('persistent://public/default/eventos-propiedades', 'subscripcion-2')
    while True:
        msg1 = consumer_comandos_propiedades.receive()
        try:
            consumer_comandos_propiedades.acknowledge(msg1)
            bytes_io = io.BytesIO(msg1.data())
            decoder = BinaryDecoder(bytes_io)
            reader = DatumReader(comando_schema)
            comando_data = reader.read(decoder)
            print("Comando recibido:", comando_data)
            consumer_comandos_propiedades.acknowledge(msg1)
        except Exception as e:
            print("Error al procesar el comando:", e)
            consumer_comandos_propiedades.negative_acknowledge(msg1)
        
        msg2 = consumer_eventos_propiedades.receive()
        data = json.loads(msg2.data().decode('utf-8'))
        print("Evento recibido:", data)
        consumer_eventos_propiedades.acknowledge(msg2)



if __name__ == "__main__":
    consumir_comandos()
