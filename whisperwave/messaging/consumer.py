import pika
import tomllib

from whisperwave.usecases.define_actions import DefineActions


def callback(ch, method, properties, body):
    """
    Callback function that is triggered whenever a message is received from the queue.

    Parameters:
        ch (pika.channel.Channel): The channel object.
        method (pika.spec.Basic.Deliver): Delivery method from RabbitMQ.
        properties (pika.spec.BasicProperties): Properties of the received message.
        body (bytes): The message body (in bytes).

    Behavior:
        - Decodes the message body from bytes to UTF-8 string.
        - If the message is not empty, it instantiates the `DefineActions` use case
          and calls its `execute_action()` method with the decoded message.
        - Any exception during execution is silently ignored (not recommended for production).
    """
    message = body.decode('utf-8')
    try:
        if message:
            actions = DefineActions()
            actions.execute_action(message)
            
    except:
        pass


class Consumer:
    """
    Consumer class for connecting to a RabbitMQ server and consuming messages from a specified queue.

    Attributes:
        connection (pika.BlockingConnection): RabbitMQ connection object.
        channel (pika.channel.Channel): Channel for communication with RabbitMQ.
        queue (str): Name of the queue to consume messages from.
    """
    connection = None
    channel = None
    queue = None

    def __init__(self):
        """
        Initializes the Consumer object.

        - Loads configuration from `config.toml`, specifically the RabbitMQ host under the key `rabbit.host`.
        - Establishes a blocking connection to the RabbitMQ server.
        - Opens a channel for communication.
        """
        with open("config.toml", "rb") as f:
            config = tomllib.load(f)

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(str(config["rabbit"]["host"])))
        self.channel = self.connection.channel()

    def set_queue(self, queue):
        """
        Sets the queue name that the consumer will consume from.

        Parameters:
            queue (str): Name of the RabbitMQ queue.
        """
        self.queue = queue

    def consume_queue(self):
        """
        Starts consuming messages from the set queue.

        - Declares the queue (creates it if it doesn't exist).
        - Begins consuming messages using the `callback` function.
        - Automatically acknowledges messages upon receipt.
        - Blocks and continuously listens for new messages until manually stopped.
        """
        self.channel.queue_declare(queue=self.queue)
        self.channel.basic_consume(queue=self.queue, on_message_callback=callback, auto_ack=True)
        print(" [x] Awaiting for messages.")
        self.channel.start_consuming()