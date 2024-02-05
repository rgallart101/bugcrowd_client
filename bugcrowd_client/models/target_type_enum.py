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


class TargetTypeEnum(str, Enum):
    """
    TargetTypeEnum
    """

    """
    allowed enum values
    """
    WEBSITE = 'website'
    API = 'api'
    IOS = 'ios'
    ANDROID = 'android'
    IOT = 'iot'
    HARDWARE = 'hardware'
    NETWORK = 'network'
    OTHER = 'other'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TargetTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


