import pika
import json
import sys
from channel import channel
from mongo_connect import connect
from models import Contact

def set_send_message(message):
    email = Contact.objects(id=message["ObjektId"]).first()
    if email:
        email.update(send_message=True)

def send_email_messege(email: str, email_message: str=""):
    print(f"send message in {email}")


channel.queue_declare(queue='email_task_queue', durable=True)
def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f" [x] Received {message}")

    set_send_message(message)
    send_email_messege(message["email"])

    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='email_task_queue', on_message_callback=callback)
print(' [*] Waiting for messages. To exit press CTRL+C')



if __name__ == '__main__':
    channel.start_consuming()





