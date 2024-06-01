from typing import Dict

from ..constants import ERROR_INVALID_CRONE_STEP_FIELD, ERROR_INVALID_CRONE_EXPAND_ALL_FIELD
from cron_expression_parser.utils.log import get_logger
from cron_expression_parser.parser.field_parser.field_parser import FieldParser





logger = get_logger(__name__)


class BaseParser(FieldParser):
    def __init__(self):
        self.expanders = self.initialize_expanders()

    def initialize_expanders(self) -> Dict[str, object]:
        return {
            '/': self._expand_step,
            ',': self._expand_list,
            '-': self._expand_range,
            '*': self._expand_all,  
        }
    

    def is_valid_range(self, value_range, valid_range) -> bool:
        if not value_range:
            return False
        if value_range[0] < valid_range[0] or value_range[-1] > valid_range[-1]:
            return False
        return True

    def _expand_all(self, field: str, range_values: range) -> list:
        #import pdb;pdb.set_trace()
        start, end = field.split("*")
        if start.isdigit() and end.isdigit():
            logger.error(f"{ERROR_INVALID_CRONE_EXPAND_ALL_FIELD} {field}")
            raise ValueError(f"{ERROR_INVALID_CRONE_EXPAND_ALL_FIELD} {field}")
        return list(range_values)

    def _expand_list(self, field: str, range_values: range) -> list:
        results = []
        for part in field.split(','):
            results.extend(self.expand(part, range_values))
        return sorted(set(results))

    def _expand_range(self, field: str, range_values: range) -> list:
        start, end = map(int, field.split('-'))
        return list(range(start, end + 1))

    def _expand_step(self, field: str, range_values: range) -> list:
        base, step = field.split('/')

        if base.isdigit() and step.isdigit():
            logger.error(f"{ERROR_INVALID_CRONE_STEP_FIELD} {field}")
            raise ValueError(f"{ERROR_INVALID_CRONE_STEP_FIELD} {field}")
        base = self.expand(base, range_values)
        step = int(step)
        return base[::step]

    def expand(self, field: str, range_values: range) -> list:
        for delimiter, expander in self.expanders.items():
            if delimiter in field:
                return expander(field, range_values)
        return [int(field)]
            
    
    def parse(self):
        raise NotImplementedError
