class OrderSaga:
    def __init__(self):
        ...

    def step1(self, propiedad_json):
        print("Step 1: Perform action 1 for order")

    def step2(self, propiedad_json):
        print("Step 2: Perform action 2 for order")

    def step3(self, propiedad_json):
        print("Step 3: Perform action 3 for order")

    def compensate_step1(self, propiedad_json):
        print("Compensating Step 1 for order")

    def compensate_step2(self, propiedad_json):
        print("Compensating Step 2 for order")

    def compensate_step3(self, propiedad_json):
        print("Compensating Step 3 for order")

    def execute(self, propiedad_json):
        self.propiedad_json = propiedad_json
        try:
            self.step1(self.propiedad_json)
            self.step2(self.propiedad_json)
            self.step3(self.propiedad_json)
        except Exception as e:
            self.compensate_step3(self.propiedad_json)
            self.compensate_step2(self.propiedad_json)
            self.compensate_step1(self.propiedad_json)
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