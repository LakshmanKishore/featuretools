from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from dask import dataframe as dd
from scipy import stats
from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import (
    Boolean,
    BooleanNullable,
    Datetime,
    Double,
    IntegerNullable,
)

from featuretools.primitives.aggregation.standard.count import Count
from featuretools.primitives.core.aggregation_primitive import AggregationPrimitive
from featuretools.utils import convert_time_units
from featuretools.utils.gen_utils import Library


class Sum(AggregationPrimitive):
    """Calculates the total addition, ignoring `NaN`.

    Examples:
        >>> sum = Sum()
        >>> sum([1, 2, 3, 4, 5, None])
        15.0
    """

    name = "sum"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(semantic_tags={"numeric"})
    stack_on_self = False
    stack_on_exclude = [Count]
    default_value = 0
    compatibility = [Library.PANDAS, Library.DASK, Library.SPARK]
    description_template = "the sum of {}"

    def get_function(self, agg_type=Library.PANDAS):
        if agg_type in [Library.DASK, Library.SPARK]:
            return "sum"

        return np.sum
