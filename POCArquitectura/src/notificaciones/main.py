from pulsar import Client, AuthenticationToken
from avro.schema import Parse
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
import io
# Parse the Avro schema for the command
comando_schema = Parse(open("src/notificaciones/schema/v1/propiedad.avsc").read())

def consumir_comandos():
    client = Client('pulsar://127.0.0.1:6650')
    consumer = client.subscribe('persistent://public/default/comandos-propiedades', 'subscripcion-1')
    while True:
        msg = consumer.receive()
        try:
            bytes_io = io.BytesIO(msg.data())
            decoder = BinaryDecoder(bytes_io)
            reader = DatumReader(comando_schema)
            comando_data = reader.read(decoder)
            print("Comando recibido:", comando_data)
            consumer.acknowledge(msg)
        except Exception as e:
            print("Error al procesar el comando:", e)
            consumer.negative_acknowledge(msg)

if __name__ == "__main__":
    consumir_comandos()
