import pika

url = "amqps://ecgrlsyf:2csYfV8RBfo5grfson_REYHa2ujEPBjz@albatross.rmq.cloudamqp.com/ecgrlsyf"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()