from dataclasses import dataclass


@dataclass
class TemplateMessage:
    @dataclass
    class Message:
        data: str
        messageId: str
        message_id: str
        publishTime: str
        publish_time: str

    message: Message
    subscription: str
