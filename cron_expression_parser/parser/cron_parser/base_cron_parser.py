from typing import Dict
from abc import ABC, abstractmethod


from cron_expression_parser.utils.log import get_logger
from cron_expression_parser.formatters.base_formatter import BaseFormatter
from cron_expression_parser.parser.field_parser.base_field_parser import BaseParser

logger = get_logger(__name__)

class BaseCronParser(ABC):
    def __init__(self, cron_string: str, formatter: BaseFormatter, field_parser: BaseParser):
        self.cron_string = cron_string
        self.parsed_cron = None
        self.formatter = formatter
        self.field_parser = field_parser
        self.parsers = self.initialize_parsers()

    @abstractmethod
    def validate(self):
        pass


    @abstractmethod
    def initialize_parsers(self) -> Dict[str, object]:
        pass

    @abstractmethod
    def parse(self):
        pass

    def format_output(self) -> str:
        return self.formatter.format(self.parsed_cron)
