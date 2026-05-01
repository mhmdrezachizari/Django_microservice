# users/producer.py
import pika
import json

def publish_user_created(event: dict):
    credentials = pika.PlainCredentials("admin", "admin")

    params = pika.ConnectionParameters(
        host="rabbitmq",
        credentials=credentials
    )

    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue='user_events', durable=True)

    # همین event که از view آمده را می‌فرستیم
    channel.basic_publish(
        exchange='',
        routing_key='user_events',
        body=json.dumps(event),
        properties=pika.BasicProperties(
            delivery_mode=2  # persistent
        )
    )

    connection.close()
