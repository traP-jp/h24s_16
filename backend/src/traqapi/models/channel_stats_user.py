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



from pydantic import BaseModel, Field, StrictInt, StrictStr

class ChannelStatsUser(BaseModel):
    """
    チャンネル上の特定ユーザー統計情報  # noqa: E501
    """
    id: StrictStr = Field(..., description="ユーザーID")
    message_count: StrictInt = Field(..., alias="messageCount", description="メッセージ数")
    __properties = ["id", "messageCount"]

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
    def from_json(cls, json_str: str) -> ChannelStatsUser:
        """Create an instance of ChannelStatsUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChannelStatsUser:
        """Create an instance of ChannelStatsUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChannelStatsUser.parse_obj(obj)

        _obj = ChannelStatsUser.parse_obj({
            "id": obj.get("id"),
            "message_count": obj.get("messageCount")
        })
        return _obj


