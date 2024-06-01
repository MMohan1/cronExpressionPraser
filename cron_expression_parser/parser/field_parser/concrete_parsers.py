
from cron_expression_parser.parser.field_parser.base_field_parser import BaseParser
from cron_expression_parser.parser.constants import MINUTE_RANGE, HOUR_RANGE, DOM_RANGE, MONTH_RANGE, DOW_RANGE

from cron_expression_parser.utils.log import get_logger
from ..constants import ERROR_INVALID_CRONE_FIELD, ERROR_INVALID_FIELD_VALUE


logger = get_logger(__name__)


class MinuteParser(BaseParser):
    def parse(self, field: str) -> list:
        try:
            out_put =  self.expand(field, MINUTE_RANGE)
            if not self.is_valid_range(out_put, MINUTE_RANGE):
                err_msg = ERROR_INVALID_FIELD_VALUE.format(f_type="Minute", field=field, min_value=MINUTE_RANGE[0], max_value=MINUTE_RANGE[-1])
                raise ValueError(err_msg)
            return out_put
        except Exception as e:
            logger.error(e)
            raise ValueError(e)
            

class HourParser(BaseParser):
    def parse(self, field: str) -> list:
        try:
             out_put = self.expand(field, HOUR_RANGE)

             if not self.is_valid_range(out_put, HOUR_RANGE):
                err_msg = ERROR_INVALID_FIELD_VALUE.format(f_type="Hour", field=field, min_value=HOUR_RANGE[0], max_value=HOUR_RANGE[-1])
                raise ValueError(err_msg)
             
             return out_put
        except Exception as e:
            logger.error(e)
            raise ValueError(e)

class DayOfMonthParser(BaseParser):
    def parse(self, field: str) -> list:
        try:
            out_put = self.expand(field, DOM_RANGE)

            if not self.is_valid_range(out_put, DOM_RANGE):
                err_msg = ERROR_INVALID_FIELD_VALUE.format(f_type="Day of Month",field=field, min_value=DOM_RANGE[0], max_value=DOM_RANGE[-1])
                raise ValueError(err_msg)
            
            return out_put
        except Exception as e:
            logger.error(e)
            raise ValueError(e)

class MonthParser(BaseParser):
    def parse(self, field: str) -> list:
        try:
            out_put = self.expand(field, MONTH_RANGE)

            if not self.is_valid_range(out_put, MONTH_RANGE):
                err_msg = ERROR_INVALID_FIELD_VALUE.format(f_type="Month", field=field, min_value=MONTH_RANGE[0], max_value=MONTH_RANGE[-1])
                raise ValueError(err_msg)

            return out_put
        except Exception as e:
            logger.error(e)
            raise ValueError(e)
        

class DayOfWeekParser(BaseParser):
    def parse(self, field: str) -> list:
        try:
            out_put = self.expand(field, DOW_RANGE)

            if not self.is_valid_range(out_put, DOW_RANGE):
                err_msg = ERROR_INVALID_FIELD_VALUE.format(f_type="Day of Week" ,field=field, min_value=DOW_RANGE[0], max_value=DOW_RANGE[-1])
                raise ValueError(err_msg)
            
            return out_put
        except Exception as e:
            logger.error(e)
            raise ValueError(e)


