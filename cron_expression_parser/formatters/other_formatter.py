from typing import Dict, List, Union
from .base_formatter import BaseFormatter
from cron_expression_parser.utils.log import logger


class OtherFormatter(BaseFormatter):
    def format(self, parsed_cron: Dict[str, Union[List[int], str]]) -> str:
        logger.debug(f"Formatting parsed cron output in another format: {parsed_cron}")
        # Implement your other formatting logic here
