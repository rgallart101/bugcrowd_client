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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateCustomerAssetRequestDataAttributesTags(BaseModel):
    """
    To hold an object that contains tags of various categories. Commonly provided tag categories are `cve`, `cpe` or `additional` tags.  `cpe`- A Common Platform Enumeration tag which abides by the standard of the CPE Version and is a single long string. Schema for `cpe` tag - `cpe:<cpe_version>:<part>:<vendor>:<product>:<version>:<update>:<edition>:<language>:<sw_edition>:<target_sw>:<target_hw>:<other>`  `cve`- A list of Common Vulnerabilities and Exposures tags. They are often CVE IDs that can have four (4) or more digits in the sequence number portion of the ID. For example, CVE-YYYY-NNNN with 4 digits in the sequence number, CVE-YYYY-NNNNN with 5 digits in the sequence number, CVE-YYYY-NNNNNNN with 7 digits in the sequence number, and so on.  `additional`- A list of additional tags which help in describing the asset and can have any used defined string as a tag value.  Update will replace the entire list of previously added tags with list specified here. 
    """ # noqa: E501
    cpe: Optional[StrictStr] = None
    cve: Optional[Annotated[List[StrictStr], Field(max_length=100)]] = None
    additional: Optional[Annotated[List[StrictStr], Field(max_length=100)]] = None
    __properties: ClassVar[List[str]] = ["cpe", "cve", "additional"]

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
        """Create an instance of UpdateCustomerAssetRequestDataAttributesTags from a JSON string"""
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
        """Create an instance of UpdateCustomerAssetRequestDataAttributesTags from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpe": obj.get("cpe"),
            "cve": obj.get("cve"),
            "additional": obj.get("additional")
        })
        return _obj


