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
from typing import List
from pydantic import BaseModel, Field, StrictInt, conlist
from traqapi.models.channel_stats_stamp import ChannelStatsStamp
from traqapi.models.channel_stats_user import ChannelStatsUser

class ChannelStats(BaseModel):
    """
    チャンネル統計情報  # noqa: E501
    """
    total_message_count: StrictInt = Field(..., alias="totalMessageCount", description="チャンネルの総投稿メッセージ数(削除されたものも含む)")
    stamps: conlist(ChannelStatsStamp) = Field(..., description="チャンネル上のスタンプ統計情報")
    users: conlist(ChannelStatsUser) = Field(..., description="チャンネル上のユーザー統計情報")
    datetime: datetime = Field(..., description="統計情報日時")
    __properties = ["totalMessageCount", "stamps", "users", "datetime"]

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
    def from_json(cls, json_str: str) -> ChannelStats:
        """Create an instance of ChannelStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in stamps (list)
        _items = []
        if self.stamps:
            for _item in self.stamps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stamps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChannelStats:
        """Create an instance of ChannelStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ChannelStats.parse_obj(obj)

        _obj = ChannelStats.parse_obj({
            "total_message_count": obj.get("totalMessageCount"),
            "stamps": [ChannelStatsStamp.from_dict(_item) for _item in obj.get("stamps")] if obj.get("stamps") is not None else None,
            "users": [ChannelStatsUser.from_dict(_item) for _item in obj.get("users")] if obj.get("users") is not None else None,
            "datetime": obj.get("datetime")
        })
        return _obj


