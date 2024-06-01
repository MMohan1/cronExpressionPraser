import unittest

from cron_expression_parser.parser.cron_parser.standard_cron_parser import StandardCronParser
from cron_expression_parser.formatters.table_formatter import TableFormatter
from cron_expression_parser.parser.field_parser.base_field_parser import BaseParser


class TestStandardCronParserInvalidMinMax(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.formatter = TableFormatter()
        cls.field_parser = BaseParser()
        #cls.parser = StandardCronParser(cls.cron_string)
    

    def test_pass_invalid_min_max_passed(self):
        
        invalid_cron_strings = [
            "1,70 0 1 * * /usr/bin/find",              # wrong max minute 70            
            "1,7 9-57/2 1 * * /usr/bin/find",          # wrong max hour 57               
            "1,15 9-7/2 1 * * /usr/bin/find",          # Wrong expression 9-7/2
            "1,15 9-17/2 35 * * /usr/bin/find",        # wrong max day value 35
            "1,15 9-17/2 5,15 1-22 * /usr/bin/find",   # Wrong max month 22 
            "1,15 9-17/2 5,15 1-12 -1 /usr/bin/find",  # Wrong week value -1
            "1,15 9-17/2 5,15 1-12 1-90 /usr/bin/find", # wrong max week value 90

        ]

        expacted_out_put = [
            "Invalid value for Minute 1,70. Expected values between 0 and 59.",
            "Invalid value for Hour 9-57/2. Expected values between 0 and 23.",
            "Invalid value for Hour 9-7/2. Expected values between 0 and 23.",
            "Invalid value for Day of Month 35. Expected values between 1 and 31.",
            "Invalid value for Month 1-22. Expected values between 1 and 12.",
            "invalid literal for int() with base 10: ''",
            "Invalid value for Day of Week 1-90. Expected values between 1 and 7.",
        ]

        for index,cron_string in enumerate(invalid_cron_strings):
            with self.subTest(cron_string=cron_string):
                with self.assertRaises(ValueError) as context:
                    StandardCronParser(cron_string, self.formatter, self.field_parser).parse()
                self.assertEqual(str(context.exception), expacted_out_put[index])



if __name__ == "__main__":
    unittest.main()
