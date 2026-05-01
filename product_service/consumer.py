import os
import django
import pika
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.db import transaction
from products.models import Product

credentials = pika.PlainCredentials("admin", "admin")

params = pika.ConnectionParameters(
    host="rabbitmq",
    credentials=credentials
)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='user_events', durable=True)


def callback(ch, method, properties, body):
    data = json.loads(body)

    if data["event"] == "USER_CREATED":

        user_id = data["id"]

        with transaction.atomic():
            Product.objects.create(
                name="Starter Product",
                price=0,
                owner_id=user_id
            )

    ch.basic_ack(method.delivery_tag)


channel.basic_consume(
    queue='user_events',
    on_message_callback=callback
)

print("Product worker running...")
channel.start_consuming()
