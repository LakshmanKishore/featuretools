import numpy as np
import pandas as pd
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import (
    URL,
    Boolean,
    BooleanNullable,
    Categorical,
    Datetime,
    Double,
    EmailAddress,
    NaturalLanguage,
    Timedelta,
)

from featuretools.primitives.core.transform_primitive import TransformPrimitive
from featuretools.primitives.transform.standard.diff import Diff
from featuretools.utils.common_tld_utils import COMMON_TLDS
from featuretools.utils.gen_utils import Library

class DiffDatetime(Diff):
    """Compute the timedelta between a datetime in a list and the
    previous datetime in that list.

    Args:
        periods (int): The number of periods by which to shift the index row.
            Default is 0. Periods correspond to rows.

    Description:
        Given a list of datetimes, compute the difference from the previous
        item in the list. The result for the first element of the list will
        always be `NaT`.

    Examples:
        >>> from datetime import datetime
        >>> dt_values = [datetime(2019, 3, 1), datetime(2019, 6, 30), datetime(2019, 11, 17), datetime(2020, 1, 30), datetime(2020, 3, 11)]
        >>> diff_dt = Diff()
        >>> diff_dt(dt_values).tolist()
        [NaT, Timedelta('121 days 00:00:00'), Timedelta('140 days 00:00:00'), Timedelta('74 days 00:00:00'), Timedelta('41 days 00:00:00')]

        You can specify the number of periods to shift the values

        >>> diff_dt_periods = Diff(periods = 1)
        >>> diff_dt_periods(dt_values).tolist()
        [NaT, NaT, Timedelta('121 days 00:00:00'), Timedelta('140 days 00:00:00'), Timedelta('74 days 00:00:00')]
    """

    name = "diff_datetime"
    input_types = [ColumnSchema(logical_type=Datetime)]
    return_type = ColumnSchema(logical_type=Timedelta)
    uses_full_dataframe = True
    description_template = "the difference from the previous value of {}"

    def __init__(self, periods=0):
        super().__init__(periods)