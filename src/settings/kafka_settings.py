import os
from autotech_sdk.kafka import ConfluentPublisherConfig, ConfluentConsumerConfig


class KafkaTopic:
    GMAIL_NOTIFY = "gmail_notify"
    SEND_MESSENGER_NOTIFY = "send_messenger_notify"


CONFLUENT_KAFKA_CONSUMER_CONFIG = ConfluentConsumerConfig(
    bootstrap_servers=os.environ.get("BOOTSTRAP_SERVERS", "localhost:9092"),
    security_protocol=os.environ.get("SECURITY_PROTOCOL", "SASL_SSL"),
    sasl_mechanisms=os.environ.get("SASL_MECHANISMS", "PLAIN"),
    sasl_username=os.environ.get("SASL_USERNAME", ""),
    sasl_password=os.environ.get("SASL_PASSWORD", ""),
    session_timeout_ms=os.environ.get("SESSION_TIMEOUT_MS", 45000),
    group_id=os.environ.get("GROUP_ID", "default_group"),
    auto_offset_reset=os.environ.get("AUTO_OFFSET_RESET", "earliest")
)


CONFLUENT_KAFKA_PRODUCER_CONFIG = ConfluentPublisherConfig(
    bootstrap_servers=os.environ.get("BOOTSTRAP_SERVERS", "localhost:9092"),
    security_protocol=os.environ.get("SECURITY_PROTOCOL", "SASL_SSL"),
    sasl_mechanisms=os.environ.get("SASL_MECHANISMS", "PLAIN"),
    sasl_username=os.environ.get("SASL_USERNAME", ""),
    sasl_password=os.environ.get("SASL_PASSWORD", ""),
)
