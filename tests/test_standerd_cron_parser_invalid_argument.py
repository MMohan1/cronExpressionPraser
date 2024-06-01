import unittest

from cron_expression_parser.parser.cron_parser.standard_cron_parser import StandardCronParser
from cron_expression_parser.formatters.table_formatter import TableFormatter
from cron_expression_parser.parser.field_parser.base_field_parser import BaseParser


class TestStandardCronParserWrongArgument(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.formatter = TableFormatter()
        cls.field_parser = BaseParser()
        #cls.parser = StandardCronParser(cls.cron_string)


    def test_parse_crone_wrong_argument_passed(self):
        
        invalid_cron_strings = [
            "*/15 0 1,15 *",                      # Too few fields
            "*/15 0 1,15 * 1-5 0 /usr/bin/find",  # Too many fields
            "*/15 0 1,15 * 1-5"                   # No command provided
        ]


        for cron_string in invalid_cron_strings:
            with self.subTest(cron_string=cron_string):
                with self.assertRaises(ValueError) as context:
                    StandardCronParser(cron_string, self.formatter, self.field_parser).parse()
                self.assertEqual(str(context.exception), "Invalid cron expression. Expected 5 time fields and 1 command.")
