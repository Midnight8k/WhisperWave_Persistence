from whisperwave.messaging.consumer import Consumer
from whisperwave.messaging.rpc_consumer import RpcConsumer
import threading


def simpe_consume_task():
    """
    Task function to start consuming messages from the 'persistence' RabbitMQ queue.

    Initializes a Consumer instance, sets the queue to 'persistence', 
    and begins consuming messages indefinitely.
    """
    consumer = Consumer()
    consumer.set_queue("persistence")
    consumer.consume_queue()

def rpc_consume_task():
    """
    Task function to start consuming messages from the 'rpc_persistence' RabbitMQ queue.

    Initializes an RpcConsumer instance, sets the queue to 'rpc_persistence',
    and begins consuming RPC messages indefinitely.
    """    
    consumer = RpcConsumer()
    consumer.set_queue("rpc_persistence")
    consumer.consume()

def main():
    """
    Entry point for the persistence microservice.

    Starts two separate threads to handle concurrent message consumption:
    - One thread for standard message consumption from the 'persistence' queue.
    - Another thread for RPC message consumption from the 'rpc_persistence' queue.

    Prints a startup message and initiates both threads to run indefinitely.
    """
    print("Persistence microservice")

    simple_consume = threading.Thread(target=simpe_consume_task)
    rpc_consume = threading.Thread(target=rpc_consume_task)

    simple_consume.start()
    rpc_consume.start()
