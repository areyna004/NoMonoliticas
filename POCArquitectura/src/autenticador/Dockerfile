FROM python:3

EXPOSE 5000/tcp

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "./src/autenticador/api", "run", "--host=0.0.0.0", "--port=3000"]