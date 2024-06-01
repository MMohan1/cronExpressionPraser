from typing import Dict, List, Union
from cron_expression_parser.formatters.base_formatter import BaseFormatter
from cron_expression_parser.utils.log import get_logger

logger = get_logger(__name__)


class TableFormatter(BaseFormatter):
    def format(self, parsed_cron: Dict[str, Union[List[int], str]]) -> str:
        logger.debug(f"Formatting parsed cron output as table: {parsed_cron}")
        output = []
        for field_name, times in parsed_cron.items():
            if field_name != "command":
                times_str = " ".join(map(str, times))
            else:
                times_str = times
            output.append(f"{field_name:<14}{times_str}")
        formatted_output = "\n".join(output)
        #logger.debug(f"Formatted output: {formatted_output}")
        return formatted_output
