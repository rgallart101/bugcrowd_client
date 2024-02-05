# coding: utf-8

"""
    Bugcrowd REST API

    This is Bugcrowd's primary REST API and follows the [JSON API specification](https://jsonapi.org/format/).  For more information on how to get started check out the [usage documentation](https://docs.bugcrowd.com/api/usage/) 

    The version of the OpenAPI document: 2024-01-11
    Contact: support@bugcrowd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SubstateEnum(str, Enum):
    """
    SubstateEnum
    """

    """
    allowed enum values
    """
    NEW = 'new'
    OUT_OF_SCOPE = 'out_of_scope'
    NOT_APPLICABLE = 'not_applicable'
    NOT_REPRODUCIBLE = 'not_reproducible'
    TRIAGED = 'triaged'
    UNRESOLVED = 'unresolved'
    RESOLVED = 'resolved'
    INFORMATIONAL = 'informational'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SubstateEnum from a JSON string"""
        return cls(json.loads(json_str))


