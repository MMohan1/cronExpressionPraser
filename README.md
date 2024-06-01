# Cron Expression Parser

## Overview

The Cron Expression Parser is a command-line application that parses a cron string and expands each field to show the times at which it will run. The parser supports the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command.

## Features

- Parses standard cron expressions
- Expands each field to show all times at which it will run
- Provides detailed validation and error messages for incorrect cron expressions
- Uses an object-oriented design for easy extension and maintenance

## Installation

### Prerequisites

- Docker

### Steps

1. Unzip the repository:
    ```
    unzip cronExpressionPraser.zip
    cd cronExpressionPraser
    ```

2. Build the Docker Image:
    ```
    docker build -t cron-expression-parser .
    ```

3. Run the Docker Container:
    ```
    docker run --rm cron-expression-parser "*/15 0 1,15 * 1-5 /usr/bin/find"
    ```

4. Run Test Cases:
    ```
    docker run --rm -e RUN_TESTS=true cron-expression-parser
    ```

## Usage

To run the cron expression parser from the command line, use the following syntax:

```
docker run --rm cron-expression-parser "*/15 0 1,15 * 1-5 /usr/bin/find"

Expacted OutPut

minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
```

## Project Structure
```
cron-expression-parser/
├── cron_expression_parser/
│   ├── formatters/
│   │       ├── __init__.py
│   │       ├── base_formatter.py
│   │       ├── other_formatter.py
│   │       ├── table_formatter.py
│   ├── parser/
│   │   ├── constants.py
│   │   ├── cron_parser/
│   │   │   ├── base_cron_parser.py
│   │   │   ├── standard_cron_parser.py
│   │   └── field_parser/
│   │       ├── __init__.py
│   │       ├── base_field_parser.py
│   │       ├── concrete_parsers.py
│   │       ├── field_parser.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── log.py
├── tests
│   ├── test_standerd_cron_parser_happy_cases.py
│   ├── test_standard_cron_parser_invalid_argument.py
│   ├── test_standerd_cron_parser_invalid_min_max.py
│   ├── test_standerd_cron_parser_wrong_expression.py
├── main.py
├── requirements.txt
├── Dockerfile
├──entrypoint.sh
└── README.md
```


## Constants
    Customizable constants are defined for error messages and other configuration options.


## Running TestCases
    python3 -m unittest discover tests


## Logging

    The application uses a custom logger for logging purposes. Logs will include the line number for easier debugging.

## Extending the Parser
    The parser is designed with an object-oriented approach, making it easy to extend. To add support for new types of parsers, follow these steps:

    1. Create a new parser class in the appropriate directory.
    2. Inherit from FieldParser.
    3. Implement the parse method with the desired logic.


## Run Using Docker
    Easy to Run using Docker