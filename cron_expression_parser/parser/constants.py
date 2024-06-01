MINUTE_RANGE = range(0, 60)
HOUR_RANGE = range(0, 24)
DOM_RANGE = range(1, 32)
MONTH_RANGE = range(1, 13)
DOW_RANGE = range(1, 8)


ERROR_INVALID_CRON_EXPRESSION = "Invalid cron expression. Expected 5 time fields and 1 command."
ERROR_INVALID_FIELD_VALUE = "Invalid value for {f_type} {field}. Expected values between {min_value} and {max_value}."
ERROR_INVALID_DELIMITER_FOUND = "Invalid delimiter found in cron string"
ERROR_INVALID_CRONE_FIELD = "Invalid crone field"
ERROR_INVALID_CRONE_STEP_FIELD = "Invalid field for step expression, filed: "
ERROR_INVALID_CRONE_EXPAND_ALL_FIELD = "Invalid field for expand(*) expression, filed: "
