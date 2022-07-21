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
from featuretools.utils.common_tld_utils import COMMON_TLDS
from featuretools.utils.gen_utils import Library


class NumCharacters(TransformPrimitive):
    """Calculates the number of characters in a string.

    Examples:
        >>> num_characters = NumCharacters()
        >>> num_characters(['This is a string',
        ...                 'second item',
        ...                 'final1']).tolist()
        [16, 11, 6]
    """

    name = "num_characters"
    input_types = [ColumnSchema(logical_type=NaturalLanguage)]
    return_type = ColumnSchema(semantic_tags={"numeric"})
    compatibility = [Library.PANDAS, Library.DASK, Library.SPARK]
    description_template = "the number of characters in {}"

    def get_function(self):
        def character_counter(array):
            return array.fillna("").str.len()

        return character_counter
