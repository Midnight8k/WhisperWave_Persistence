from whisperwave.usecases.define_actions import DefineActions
import pika


def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    try:
        if message:
            actions = DefineActions()
            actions.execute_action(message)
            
    except:
        pass


class Consumer:
    connection = None
    channel = None
    queue = None

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.1.94"))
        self.channel = self.connection.channel()

    def set_queue(self, queue):
        self.queue = queue

    def consume_queue(self):
        self.channel.queue_declare(queue=self.queue)
        self.channel.basic_consume(queue=self.queue, on_message_callback=callback, auto_ack=True)
        print(" [x] Awaiting for messages.")
        self.channel.start_consuming()