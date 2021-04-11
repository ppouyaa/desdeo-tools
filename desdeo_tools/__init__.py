"""
This module implements various small tools that may be useful during optimization using
either the MCDM or the EA methods.
"""

__all__ = [
    "dominates",
    "non_dominated",
    "fast_non_dominated_sort",
    "fast_non_dominated_sort_indices",
    "classification_to_reference_point",
]

from desdeo_tools.utilities.fast_non_dominated_sorting import (
    dominates,
    non_dominated,
    fast_non_dominated_sort,
    fast_non_dominated_sort_indices,
)

from desdeo_tools.utilities.preference_converters import (
    classification_to_reference_point,
)

