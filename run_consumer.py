from dotenv import load_dotenv
load_dotenv()

from src.consumer.template_consumer import TemplateConsumer
from src.settings.kafka_settings import CONFLUENT_KAFKA_CONSUMER_CONFIG, KafkaTopic

if __name__ == '__main__':
    TemplateConsumer(CONFLUENT_KAFKA_CONSUMER_CONFIG, KafkaTopic.GMAIL_NOTIFY).run_consumer()
