from src.settings.kafka_settings import CONFLUENT_KAFKA_PRODUCER_CONFIG
from autotech_sdk.kafka import ConfluentPublisher


class Publisher(ConfluentPublisher):

    def acked(self, err, msg):
        print(msg)


def push_message_to_confluent_kafka(data, topic):
    publisher = Publisher(CONFLUENT_KAFKA_PRODUCER_CONFIG)
    publisher.push_message_to_confluent_kafka(data, topic)
