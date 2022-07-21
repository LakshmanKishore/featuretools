import holidays
import numpy as np
import pandas as pd
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import (
    AgeFractional,
    BooleanNullable,
    Categorical,
    Datetime,
    Ordinal,
)

from featuretools.primitives.core.transform_primitive import TransformPrimitive
from featuretools.primitives.utils import HolidayUtil
from featuretools.utils import convert_time_units
from featuretools.utils.gen_utils import Library


class Day(TransformPrimitive):
    """Determines the day of the month from a datetime.

    Examples:
        >>> from datetime import datetime
        >>> dates = [datetime(2019, 3, 1),
        ...          datetime(2019, 3, 3),
        ...          datetime(2019, 3, 31)]
        >>> day = Day()
        >>> day(dates).tolist()
        [1, 3, 31]
    """

    name = "day"
    input_types = [ColumnSchema(logical_type=Datetime)]
    return_type = ColumnSchema(
        logical_type=Ordinal(order=list(range(1, 32))),
        semantic_tags={"category"},
    )
    compatibility = [Library.PANDAS, Library.DASK, Library.SPARK]
    description_template = "the day of the month of {}"

    def get_function(self):
        def day(vals):
            return vals.dt.day

        return day
