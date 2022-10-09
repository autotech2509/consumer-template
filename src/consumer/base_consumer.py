from confluent_kafka import Consumer
import json
from abc import ABCMeta, abstractmethod


class BaseConsumer(metaclass=ABCMeta):
    def __init__(self, config, topic):
        consumer = Consumer(config)
        self.consumer = consumer
        self.consumer.subscribe(topic)

    @abstractmethod
    def process_data(self, data):
        pass

    def run_consumer(self):
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    print("Waiting for message or event/error in poll()")
                    continue
                elif msg.error():
                    print('error: {}'.format(msg.error()))
                else:
                    record_value = msg.value()
                    data = json.loads(record_value)
                    self.process_data(data)
        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()
