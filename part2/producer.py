import pika
import sys
import json
from datetime import datetime
from faker import Faker
from mongo_connect import connect
from models import Contact

url = "amqps://ecgrlsyf:2csYfV8RBfo5grfson_REYHa2ujEPBjz@albatross.rmq.cloudamqp.com/ecgrlsyf"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='email_task_mock', exchange_type='direct')
channel.queue_declare(queue='email_task_queue', durable=True)
channel.queue_bind(exchange='email_task_mock', queue='email_task_queue')

def create_users(amount): 
    fake_data = Faker() 
    for _ in range(amount):
        new_contact = Contact(
            name = fake_data.name(),
            email = fake_data.email()
        )
        new_contact.save()


def main():

    create_users(20)

    contacts = Contact.objects(send_message=False)
    i = 0
    for contact in contacts:
        i += 1
        message = {
            "id": i ,
            "payload": f"Task #{i}",
            "date": datetime.now().isoformat(),
            "ObjektId": str(contact.id),
            "email": contact.email
        }
        channel.basic_publish(
            exchange='',
            routing_key='email_task_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(" [x] Sent %r" % message)
    
    connection.close()
    
    
if __name__ == '__main__':
    main()

