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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateCredentialBucketRequestDataAttributes(BaseModel):
    """
    CreateCredentialBucketRequestDataAttributes
    """ # noqa: E501
    name: StrictStr
    credential_type: StrictStr
    credentials_per_researcher: Annotated[int, Field(strict=True, ge=0)]
    description: StrictStr
    is_ready: StrictBool
    low_balance_threshold: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    __properties: ClassVar[List[str]] = ["name", "credential_type", "credentials_per_researcher", "description", "is_ready", "low_balance_threshold"]

    @field_validator('credential_type')
    def credential_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('email', 'text'):
            raise ValueError("must be one of enum values ('email', 'text')")
        return value

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
        """Create an instance of CreateCredentialBucketRequestDataAttributes from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateCredentialBucketRequestDataAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "credential_type": obj.get("credential_type"),
            "credentials_per_researcher": obj.get("credentials_per_researcher"),
            "description": obj.get("description"),
            "is_ready": obj.get("is_ready"),
            "low_balance_threshold": obj.get("low_balance_threshold")
        })
        return _obj


