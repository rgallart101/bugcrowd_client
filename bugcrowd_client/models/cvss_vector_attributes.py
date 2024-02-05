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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, field_validator
from pydantic import Field
from bugcrowd_client.models.cvss_attack_vector_options_enum import CvssAttackVectorOptionsEnum
from bugcrowd_client.models.cvss_high_low_options_enum import CvssHighLowOptionsEnum
from bugcrowd_client.models.cvss_scope_options_enum import CvssScopeOptionsEnum
from bugcrowd_client.models.cvss_user_interaction_options_enum import CvssUserInteractionOptionsEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CvssVectorAttributes(BaseModel):
    """
    CvssVectorAttributes
    """ # noqa: E501
    attack_complexity: Optional[CvssHighLowOptionsEnum] = None
    attack_vector: Optional[CvssAttackVectorOptionsEnum] = None
    authorization_scope: Optional[CvssScopeOptionsEnum] = None
    availability_impact: Optional[CvssHighLowOptionsEnum] = None
    confidentiality_impact: Optional[CvssHighLowOptionsEnum] = None
    integrity_impact: Optional[CvssHighLowOptionsEnum] = None
    privileges_required: Optional[CvssHighLowOptionsEnum] = None
    score: Optional[Union[StrictFloat, StrictInt]] = None
    user_interaction: Optional[CvssUserInteractionOptionsEnum] = None
    version: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="CVSS version number")
    __properties: ClassVar[List[str]] = ["attack_complexity", "attack_vector", "authorization_scope", "availability_impact", "confidentiality_impact", "integrity_impact", "privileges_required", "score", "user_interaction", "version"]

    @field_validator('version')
    def version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (2, 3):
            raise ValueError("must be one of enum values (2, 3)")
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
        """Create an instance of CvssVectorAttributes from a JSON string"""
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
        """Create an instance of CvssVectorAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attack_complexity": obj.get("attack_complexity"),
            "attack_vector": obj.get("attack_vector"),
            "authorization_scope": obj.get("authorization_scope"),
            "availability_impact": obj.get("availability_impact"),
            "confidentiality_impact": obj.get("confidentiality_impact"),
            "integrity_impact": obj.get("integrity_impact"),
            "privileges_required": obj.get("privileges_required"),
            "score": obj.get("score"),
            "user_interaction": obj.get("user_interaction"),
            "version": obj.get("version")
        })
        return _obj


