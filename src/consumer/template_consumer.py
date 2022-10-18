from autotech_sdk.kafka import ConfluentConsumer
from dacite import from_dict

from src.common.types.template_message import TemplateMessage


class TemplateConsumer(ConfluentConsumer):
    def process_error_data(self, error):
        print("error: {}".format(error))

    def process_data(self, data):
        data = from_dict(data_class=TemplateMessage, data=data)
        print(data)
