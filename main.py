import argparse
import sys
from cron_expression_parser.parser.cron_parser.standard_cron_parser import StandardCronParser 
from cron_expression_parser.formatters.table_formatter import TableFormatter
from cron_expression_parser.parser.field_parser.base_field_parser import BaseParser
from cron_expression_parser.constants import USAGE_MESSAGE
from cron_expression_parser.utils.log import get_logger


logger = get_logger(__name__)

def main() -> None:
    parser = argparse.ArgumentParser(description='Parse and expand cron string')
    parser.add_argument('cron_string', type=str, help='Cron string to parse')
    args = parser.parse_args()
    #import pdb;pdb.set_trace()

    formatter = TableFormatter()
    field_parser = BaseParser()
    parser = StandardCronParser(args.cron_string, formatter, field_parser)

    try:
        parser.parse()
        print(parser.format_output())
    except ValueError as e:
        logger.error(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
