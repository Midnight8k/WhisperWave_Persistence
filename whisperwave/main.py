from whisperwave.messaging.consumer import Consumer
from whisperwave.messaging.rpc_consumer import RpcConsumer
import threading


def simpe_consume_task():
    consumer = Consumer()
    consumer.set_queue("persistence")
    consumer.consume_queue()

def rpc_consume_task():
    consumer = RpcConsumer()
    consumer.set_queue("rpc_persistence")
    consumer.consume()

def main():
    print("Persistence microservice")

    simple_consume = threading.Thread(target=simpe_consume_task)
    rpc_consume = threading.Thread(target=rpc_consume_task)

    simple_consume.start()
    rpc_consume.start()
