import pika
import ast
import json
import tomllib

from whisperwave.usecases.define_actions import DefineActions


def rpc_callback(body) -> str:
    body_bytes = ast.literal_eval(body)
    body_str = body_bytes.decode('utf-8')

    actions = DefineActions()
    return actions.execute_action(body_str)


class RpcConsumer:
    def __init__(self) -> None:
        with open("config.toml", "rb") as f:
            config = tomllib.load(f)

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=str(config["rabbit"]["host"])))
        self.channel = self.connection.channel()

    def on_request(self, ch, method, props, body):
        n = str(body)

        print(f" [.] rpc_callback({n})")
        response = rpc_callback(n)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id = props.correlation_id),
                         body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def set_queue(self, queue):
        self.channel.queue_declare(queue=queue)

    def consume(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='rpc_persistence', on_message_callback=self.on_request)

        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()
