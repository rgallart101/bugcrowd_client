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
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
from bugcrowd_client.models.scheduled_crowd_member import ScheduledCrowdMember
from bugcrowd_client.models.scheduled_crowd_member_include_response_inner import ScheduledCrowdMemberIncludeResponseInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetScheduledCrowdMemberResponse(BaseModel):
    """
    GetScheduledCrowdMemberResponse
    """ # noqa: E501
    data: ScheduledCrowdMember
    included: Optional[Annotated[List[ScheduledCrowdMemberIncludeResponseInner], Field(max_length=300)]] = None
    __properties: ClassVar[List[str]] = ["data", "included"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GetScheduledCrowdMemberResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in included (list)
        _items = []
        if self.included:
            for _item in self.included:
                if _item:
                    _items.append(_item.to_dict())
            _dict['included'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetScheduledCrowdMemberResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": ScheduledCrowdMember.from_dict(obj.get("data")) if obj.get("data") is not None else None,
            "included": [ScheduledCrowdMemberIncludeResponseInner.from_dict(_item) for _item in obj.get("included")] if obj.get("included") is not None else None
        })
        return _obj


