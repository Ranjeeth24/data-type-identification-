"""
Purpose: Data types used in DataDisca applications are defined here

Contributors:
<Your Name(s)>

Sponsor: DataDisca Pty Ltd. Australia
https://github.com/DataDisca
"""

import pytest
import pandas as pd
from type_transforms import BooleanTransformedData, NumericTransformedData, TypeTransformedData
from type_transforms import CategoryTransformedData, DateTimeTransformedData, StringTransformedData
import pandas as pd


def test__import_kwargs():
    srs = pd.Series([1, 2, 3])
    typetransformdata = BooleanTransformedData(srs)
    typetransformdata._import_kwargs(threshold=40, sample_size=8, iterations=3, success_count=50)
    assert typetransformdata.threshold == 40
    assert typetransformdata.sample_size == 8
    assert typetransformdata.iterations == 3
    assert typetransformdata.success_count != 50


def test_is_my_type():
    test_df1 = pd.read_csv('readings1.csv')
    test_df2 = pd.read_csv("readings2.csv")
    test_df3 = pd.read_csv("readings3.csv")
    test_df4 = pd.read_csv("validation1.csv")
    dataset1_type_list = [2, 4, 8, 8, 2, 3, 3, 3]
    dataset2_type_list = [2, 4, 8, 8, 2, 3, 3, 3]
    dataset3_type_list = [2, 4, 8, 8, 2, 3, 3, 3]
    dataset4_type_list = [2, 2, 4, 4 ]

    def type_test(col):
        srs = col
        true_count = 0
        series_type = 0
        boolean_object = BooleanTransformedData(srs)
        if boolean_object.is_my_type() == True:
            true_count += 1
            series_type = boolean_object.data_type
        if true_count == 0:
            numeric_object = NumericTransformedData(srs)

            if numeric_object.is_my_type() == True:
                true_count += 1

                series_type = numeric_object.data_type
        if true_count == 0:
            category_object = CategoryTransformedData(srs)
            if category_object.is_my_type() == True:
                true_count += 1
                series_type = category_object.data_type
        if true_count == 0:
            datetime_object = DateTimeTransformedData(srs)
            if datetime_object.is_my_type() == True:
                true_count += 1
                series_type = datetime_object.data_type
        if true_count == 0:
            string_object = StringTransformedData(srs)
            if string_object.is_my_type() == True:
                series_type = string_object.data_type
                true_count += 1
        return series_type

    test1_type_list = list(test_df1.apply(type_test))
    test2_type_list = list(test_df2.apply(type_test))
    test3_type_list = list(test_df3.apply(type_test))
    test4_type_list = list(test_df4.apply(type_test))
    print(test3_type_list)
    print(test1_type_list)
    print(test2_type_list)
    print(test4_type_list)



