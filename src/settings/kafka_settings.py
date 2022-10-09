import os


class KafkaTopic:
    GMAIL_NOTIFY = os.environ.get("KAFKA_TOPIC", "gmail_notify")


CONFLUENT_KAFKA_PROD_CONFIG = {
    "bootstrap.server": os.environ.get("BOOTSTRAP_SERVERS", "localhost:9092"),
    "security.protocol": os.environ.get("SECURITY_PROTOCOL", "SASL_SSL"),
    "sasl.mechanisms": os.environ.get("SASL_MECHANISMS", "PLAIN"),
    "sasl.username": os.environ.get("SASL_USERNAME", ""),
    "sasl.password": os.environ.get("SASL_PASSWORD", ""),
    "session.timeout.ms": os.environ.get("SESSION_TIMEOUT_MS", 45000),
    "schema.registry.url": os.environ.get("SCHEMA_REGISTRY_URL", "https://{{ SR_ENDPOINT }}"),
    "basic.auth.credentials.source": os.environ.get("BASIC_AUTH_CREDENTIALS_SOURCE", "USER_INFO"),
    "basic.auth.user.info": os.environ.get("BASIC_AUTH_USER_INFO", ""),
    "group.id": os.environ.get("GROUP_ID", "default_group"),
    "auto.offset.reset": os.environ.get("AUTO_OFFSET_RESET", "earliest")
}
