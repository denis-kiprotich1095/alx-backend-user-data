#!/usr/bin/env python3
"""Regex-ing"""
import re
from typing import List
import logging
import os


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """returns the log message obfuscated"""
    for text in fields:
        message = re.sub(
                f'{text}=.*?{separator}', f'{text}={redaction}{separator}',
                message)
    return (message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> str:
        """__init__"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: str) -> str:
        """filter values in incoming log records using filter_datum"""
        record.msg = filter_datum(
                self.fields, self.REDACTION, record.getMessage(
                    ), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """Creating logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logging.StreamHandler(RedactingFormatter)
