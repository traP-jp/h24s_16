# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, constr, validator

class PostUserRequest(BaseModel):
    """
    ユーザー登録リクエスト  # noqa: E501
    """
    name: constr(strict=True) = Field(..., description="ユーザー名")
    password: Optional[constr(strict=True)] = Field(None, description="パスワード")
    __properties = ["name", "password"]

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9_-]{1,32}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9_-]{1,32}$/")
        return value

    @validator('password')
    def password_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\x20-\x7E]{10,32}$", value):
            raise ValueError(r"must validate the regular expression /^[\x20-\x7E]{10,32}$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PostUserRequest:
        """Create an instance of PostUserRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostUserRequest:
        """Create an instance of PostUserRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostUserRequest.parse_obj(obj)

        _obj = PostUserRequest.parse_obj({
            "name": obj.get("name"),
            "password": obj.get("password")
        })
        return _obj


