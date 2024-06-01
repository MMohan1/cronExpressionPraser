import unittest

from cron_expression_parser.parser.cron_parser.standard_cron_parser import StandardCronParser
from cron_expression_parser.formatters.table_formatter import TableFormatter
from cron_expression_parser.parser.field_parser.base_field_parser import BaseParser


class TestStandardCronParserInvalidExpression(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.formatter = TableFormatter()
        cls.field_parser = BaseParser()
        #cls.parser = StandardCronParser(cls.cron_string)

    
    def test_pass_invalid_crone_expression(self):
        
        invalid_cron_strings = [
            "*?15 0 1,15 * * /usr/bin/find",        # wrong char ?            
            "*/b15 0 1,15 * * /usr/bin/find",       # wrong char b               
            "1*15 0 1,15 * * /usr/bin/find",        # wrong field 1*15
            "1/15 0 1,15 * * /usr/bin/find",        # wrong field 1*15 
            "1/*15 0 1,15 * * /usr/bin/find"        # wrong field 1*15             
        ]

        expacted_out_put = [
            "Invalid delimiter found in cron string: *?15",
            "Invalid delimiter found in cron string: */b15",
            "Invalid field for expand(*) expression, filed:  1*15",
            "Invalid field for step expression, filed:  1/15",
            "invalid literal for int() with base 10: '*15'"
        ]


        for index,cron_string in enumerate(invalid_cron_strings):
            with self.subTest(cron_string=cron_string):
                with self.assertRaises(ValueError) as context:
                    StandardCronParser(cron_string, self.formatter, self.field_parser).parse()
                self.assertEqual(str(context.exception), expacted_out_put[index])
   