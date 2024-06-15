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

from datetime import datetime

from pydantic import BaseModel, Field, StrictStr
from traqapi.models.channel_view_state import ChannelViewState

class ChannelViewer(BaseModel):
    """
    チャンネル閲覧者情報  # noqa: E501
    """
    user_id: StrictStr = Field(..., alias="userId", description="ユーザーUUID")
    state: ChannelViewState = Field(...)
    updated_at: datetime = Field(..., alias="updatedAt", description="更新日時")
    __properties = ["userId", "state", "updatedAt"]

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
    def from_json(cls, json_str: str) -> ChannelViewer:
        """Create an instance of ChannelViewer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChannelViewer:
        """Create an instance of ChannelViewer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChannelViewer.parse_obj(obj)

        _obj = ChannelViewer.parse_obj({
            "user_id": obj.get("userId"),
            "state": obj.get("state"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


