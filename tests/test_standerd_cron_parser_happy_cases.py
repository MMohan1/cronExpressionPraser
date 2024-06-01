import unittest

from cron_expression_parser.parser.cron_parser.standard_cron_parser import StandardCronParser
from cron_expression_parser.formatters.table_formatter import TableFormatter
from cron_expression_parser.parser.field_parser.base_field_parser import BaseParser


class TestStandardCronParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.formatter = TableFormatter()
        cls.field_parser = BaseParser()
        #cls.parser = StandardCronParser(cls.cron_string)

    def test_parse_cron_expression(self):
        # Case 1: Problem input

        cron_expr = "*/15 0 1,15 * 1-5 /usr/bin/find"
        expected_output = {
            "minute": [0, 15, 30, 45],
            "hour": [0],
            "day of month": [1, 15],
            "month": list(range(1, 13)),
            "day of week": [1, 2, 3, 4, 5],
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)


    def test_parse_cron_expression_everything_star(self):
        # Case 2: everything *

        cron_expr = "* * * * * /usr/bin/find"
        expected_output = {
            "minute": list(range(0, 60)),
            "hour": list(range(0, 24)),
            "day of month": list(range(1, 32)),
            "month": list(range(1, 13)),
            "day of week": list(range(1, 8)),
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)



    def test_parse_cron_expression_case_3(self):
        # Case 3:  Every 5 Minutes, Between 1 AM and 3 AM, Every Day: Runs every 5 minutes, between 1:00 AM and 3:00 AM..

        cron_expr = "*/5 1-3 * * * /usr/bin/find"
        expected_output = {
            "minute":list(range(0, 60, 5)),
            "hour": list(range(1, 4)),
            "day of month": list(range(1, 32)),
            "month": list(range(1, 13)),
            "day of week": list(range(1, 8)),
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)


    def test_parse_cron_expression_case_4(self):
        # Case 4:  At 12:00 PM (Noon) on Every Monday, Wednesday, and Friday: Runs at 12:00 PM on Mondays, Wednesdays, and Fridays.

        cron_expr = "0 12 * * 1,3,5 /usr/bin/find"
        expected_output = {
            "minute": [0],
            "hour": [12],
            "day of month": list(range(1, 32)),
            "month": list(range(1, 13)),
            "day of week": [1, 3, 5],
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)


    def test_parse_cron_expression_case_5(self):
        # Case 5:  At 11:30 PM on the Last Day of Every Month: Runs at 11:30 PM on the last day of the month.

        cron_expr = "30 23 28-31 * * /usr/bin/find"
        expected_output = {
            "minute": [30],
            "hour": [23],
            "day of month": list(range(28, 32)),
            "month": list(range(1, 13)),
            "day of week": list(range(1, 8)),
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)


    def test_parse_cron_expression_case_6(self):

        # Case 6:  Every 15 Minutes, During Weekdays in January, April, July, and October: Runs every 15 minutes on weekdays (Monday to Friday) in January, April, July, and October.

        cron_expr = "*/15 * * 1,4,7,10 1-5 /usr/bin/find"
        expected_output = {
            "minute": list(range(0, 60, 15)),
            "hour": list(range(0, 24)),
            "day of month": list(range(1, 32)),
            "month": [1, 4, 7, 10],
            "day of week": list(range(1, 6)),
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)



    def test_parse_cron_expression_case_7(self):
        # Case 7:  At 6:00 PM on the First and Last Day of Every Month: Runs at 6:00 PM on the 1st and last day of the month.

        cron_expr = "0 18 1,28-31 * * /usr/bin/find"
        expected_output = {
            "minute": [0],
            "hour": [18],
            "day of month": [1, 28, 29, 30, 31],
            "month": list(range(1, 13)),
            "day of week": list(range(1, 8)),
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)


    def test_parse_cron_expression_case_8(self):
        # Case 8: Every 10 Minutes, on the 15th of Every Month, Except December: Runs every 10 minutes on the 15th of every month except December.

        cron_expr = "*/10 * 15 1-11 * /usr/bin/find"
        expected_output = {
            "minute": list(range(0, 60, 10)),
            "hour": list(range(0, 24)),
            "day of month": list(range(15, 16)),
            "month": list(range(1, 12)),
            "day of week": list(range(1, 8)),
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)


    def test_parse_cron_expression_case_9(self):
        # Case 9:  At 3:30 PM Every Tuesday and Thursday in the Second Quarter (April, May, June): Runs at 3:30 PM on Tuesdays and Thursdays in April, May, and June.

        cron_expr = "30 15 * 4-6 2,4 /usr/bin/find"
        expected_output = {
            "minute": [30],
            "hour": list(range(15, 16)),
            "day of month": list(range(1, 32)),
            "month": list(range(4, 7)),
            "day of week": [2, 4],
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)


    def test_parse_cron_expression_case_10(self):
        # Case 10:  Every 2 Hours, Between 9 AM and 5 PM, Monday to Friday: Runs every 2 hours between 9:00 AM and 5:00 PM on weekdays.

        cron_expr = "0 9-17/2 * * 1-5 /usr/bin/find"
        expected_output = {
            "minute": [0],
            "hour": list(range(9, 18, 2)),
            "day of month": list(range(1, 32)),
            "month": list(range(1, 13)),
            "day of week": list(range(1, 6)),
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)


    def test_parse_cron_expression_case_11(self):
        # Case 11:  At 5:00 AM Every Monday in January, March, May, July, September, and November: Runs at 5:00 AM on Mondays in specific months.

        cron_expr = "0 5 * 1,3,5,7,9,11 1 /usr/bin/find"
        expected_output = {
            "minute": [0],
            "hour": [5],
            "day of month": list(range(1, 32)),
            "month": [1,3,5,7,9,11],
            "day of week": [1],
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)

    def test_parse_cron_expression_case_12(self):
        # Case 12:  Every Minute in the First 10 Minutes of Every Hour: Runs every minute for the first 10 minutes of every hour.

        cron_expr = "0-10 * * * * /usr/bin/find"
        expected_output = {
            "minute": list(range(0, 11)),
            "hour": list(range(0, 24)),
            "day of month": list(range(1, 32)),
            "month": list(range(1, 13)),
            "day of week": list(range(1, 8)),
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)


    def test_parse_cron_expression_case_13(self):
        # Case 13:  Every 7 Minutes, During the First 20 Minutes of Every Hour on Weekdays: Runs every 7 minutes during the first 20 minutes of every hour from Monday to Friday.


        cron_expr = "0-20/7 * * * 1-5 /usr/bin/find"
        expected_output = {
            "minute": [0, 7, 14],
            "hour": list(range(0, 24)),
            "day of month": list(range(1, 32)),
            "month": list(range(1, 13)),
            "day of week": [1,2,3,4,5],
            "command": "/usr/bin/find"
        }
        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        self.assertEqual(parser.parse(), expected_output)



    def test_format_cron_output(self):
        cron_expr = "*/15 0 1,15 * 1-5 /usr/bin/find"
        parsed_cron = {
            "minute": [0, 15, 30, 45],
            "hour": [0],
            "day of month": [1, 15],
            "month": list(range(1, 13)),
            "day of week": [1, 2, 3, 4, 5],
            "command": "/usr/bin/find"
        }
        expected_output = (
            "minute        0 15 30 45\n"
            "hour          0\n"
            "day of month  1 15\n"
            "month         1 2 3 4 5 6 7 8 9 10 11 12\n"
            "day of week   1 2 3 4 5\n"
            "command       /usr/bin/find"
        )

        parser = StandardCronParser(cron_expr, self.formatter, self.field_parser)
        parser.parse()
        self.assertEqual(parser.format_output(), expected_output)

