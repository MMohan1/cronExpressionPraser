from typing import Dict, List, Set, Union

from cron_expression_parser.utils.log import get_logger
from ..constants import ERROR_INVALID_CRON_EXPRESSION,ERROR_INVALID_DELIMITER_FOUND



from cron_expression_parser.parser.cron_parser.base_cron_parser import BaseCronParser
from cron_expression_parser.parser.field_parser.concrete_parsers import (
    MinuteParser, HourParser, DayOfMonthParser, MonthParser, DayOfWeekParser)


logger = get_logger(__name__)


class StandardCronParser(BaseCronParser):

    def initialize_parsers(self) -> Dict[str, object]:
        return {
            'minute': MinuteParser(),
            'hour': HourParser(),
            'day of month': DayOfMonthParser(),
            'month': MonthParser(),
            'day of week': DayOfWeekParser()
        }

    def validate(self):
        parts = self.cron_string.split()
        valid_delimiters = self.field_parser.expanders.keys()
        valid_chars = set("0123456789") | set(valid_delimiters)
        for part in parts[:-1]:  # Excluding the command part
            if any(char not in valid_chars for char in part):
                logger.error(f"{ERROR_INVALID_DELIMITER_FOUND}: {part}")
                raise ValueError(f"{ERROR_INVALID_DELIMITER_FOUND}: {part}")
    
    def parse(self) -> Dict[str, Union[List[int], str]]:
        logger.debug(f"Parsing cron expression: {self.cron_string}")
        self.validate()
        parts = self.cron_string.split()
        if len(parts) != 6:
            logger.error(ERROR_INVALID_CRON_EXPRESSION)
            raise ValueError(ERROR_INVALID_CRON_EXPRESSION)


        minute, hour, dom, month, dow, command = parts

        self.parsed_cron = {
            'minute': self.parsers['minute'].parse(minute),
            'hour': self.parsers['hour'].parse(hour),
            'day of month': self.parsers['day of month'].parse(dom),
            'month': self.parsers['month'].parse(month),
            'day of week': self.parsers['day of week'].parse(dow),
            'command': command
        }
    
        logger.debug(f"Parsed cron expression: {self.parsed_cron}")
        return self.parsed_cron
