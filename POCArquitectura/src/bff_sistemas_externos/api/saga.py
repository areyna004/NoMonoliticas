class OrderSaga:
    def __init__(self, order_id):
        self.order_id = order_id

    def step1(self):
        print("Step 1: Perform action 1 for order", self.order_id)

    def step2(self):
        print("Step 2: Perform action 2 for order", self.order_id)

    def step3(self):
        print("Step 3: Perform action 3 for order", self.order_id)

    def compensate_step1(self):
        print("Compensating Step 1 for order", self.order_id)

    def compensate_step2(self):
        print("Compensating Step 2 for order", self.order_id)

    def compensate_step3(self):
        print("Compensating Step 3 for order", self.order_id)

    def execute(self):
        try:
            self.step1()
            self.step2()
            self.step3()
        except Exception as e:
            self.compensate_step3()
            self.compensate_step2()
            self.compensate_step1()
            raise e



'''bytes_io = io.BytesIO()
            writer = DatumWriter(propiedad_schema)
            encoder = BinaryEncoder(bytes_io)
            writer.write(propiedad_data, encoder)
            encoded_data = bytes_io.getvalue()  
            client = Client('pulsar://10.182.0.2:6650')
            producer_comandos_propiedad = client.create_producer('persistent://public/default/comandos-propiedades', chunking_enabled=True) 
            producer_comandos_propiedad.send(encoded_data)
            client.close()'''