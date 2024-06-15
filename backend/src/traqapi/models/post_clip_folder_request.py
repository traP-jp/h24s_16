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



from pydantic import BaseModel, Field, constr

class PostClipFolderRequest(BaseModel):
    """
    クリップフォルダ作成リクエスト  # noqa: E501
    """
    name: constr(strict=True, max_length=30, min_length=1) = Field(..., description="フォルダ名")
    description: constr(strict=True, max_length=1000) = Field(..., description="説明")
    __properties = ["name", "description"]

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
    def from_json(cls, json_str: str) -> PostClipFolderRequest:
        """Create an instance of PostClipFolderRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostClipFolderRequest:
        """Create an instance of PostClipFolderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostClipFolderRequest.parse_obj(obj)

        _obj = PostClipFolderRequest.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description")
        })
        return _obj


