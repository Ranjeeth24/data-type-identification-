"""
Purpose: Data types used in DataDisca applications are defined here

Contributors:
Ranjeeth Sheshala
Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""

from datetime import datetime
import pytest
from meta_data import DateTimeTransforms

def test_to_date_str():
    my_date = datetime.strptime("1/1/1970", '%d/%m/%y')
    assert DateTimeTransforms.to_date_str(my_date) == "1/1/1970"


def test_to_time_str():
    my_date = datetime.strptime("1/1/1970", '%d/%m/%y')
    assert DateTimeTransforms.to_time_str(my_date) == "00:00:00"


def test_to_datetime_str():
    my_date = datetime.strptime("1/1/1970", '%d/%m/%y')
    assert DateTimeTransforms.to_datetime_str(my_date) == "1/1/1970 00:00:00"


def test_to_short_time_str():
    my_date = datetime.strptime("1/1/1970", '%d/%m/%y')
    assert DateTimeTransforms.to_short_time_str(my_date) == "00:00"


def test_to_short_datetime_str():
    my_date = datetime.strptime("1/1/1970", '%d/%m/%y')
    assert (DateTimeTransforms.to_short_datetime_str(my_date)
            == "1/1/1970 00:00")