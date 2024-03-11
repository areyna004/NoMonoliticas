from sagas import Saga

class OrderSaga(Saga):
    def __init__(self, order_id):
        self.order_id = order_id

    def autenticar_usuario(self):
        # Implement logic to authenticate the user
        print("Authenticating user...")

    def procesar_cambio(self):
        # Implement logic to process changes for the order
        print("Processing changes...")

    def mandar_notificacion(self):
        # Implement logic to send notifications for the order
        print("Sending notifications...")

    def rollback_autenticar_usuario(self):
        # Implement compensating action for authenticating user
        print("Rolling back user authentication...")

    def rollback_procesar_cambio(self):
        # Implement compensating action for processing changes
        print("Rolling back changes processing...")

    def rollback_mandar_notificacion(self):
        # Implement compensating action for sending notifications
        print("Rolling back notification sending...")

    def execute(self):
        try:
            self.autenticar_usuario()
            self.procesar_cambio()
            self.mandar_notificacion()
        except Exception as e:
            self.rollback_autenticar_usuario()
            self.rollback_procesar_cambio()
            self.rollback_mandar_notificacion()
            raise e

# Example usage
if __name__ == "__main__":
    order_id = 12345
    saga = OrderSaga(order_id)
    saga.execute()


'''bytes_io = io.BytesIO()
            writer = DatumWriter(propiedad_schema)
            encoder = BinaryEncoder(bytes_io)
            writer.write(propiedad_data, encoder)
            encoded_data = bytes_io.getvalue()  
            client = Client('pulsar://10.182.0.2:6650')
            producer_comandos_propiedad = client.create_producer('persistent://public/default/comandos-propiedades', chunking_enabled=True) 
            producer_comandos_propiedad.send(encoded_data)
            client.close()'''