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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from traqapi.models.web_rtc_user_state_sessions_inner import WebRTCUserStateSessionsInner

class WebRTCUserState(BaseModel):
    """
    WebRTC状態  # noqa: E501
    """
    user_id: StrictStr = Field(..., alias="userId", description="ユーザーUUID")
    channel_id: StrictStr = Field(..., alias="channelId", description="チャンネルUUID")
    sessions: conlist(WebRTCUserStateSessionsInner) = Field(..., description="セッションの配列")
    __properties = ["userId", "channelId", "sessions"]

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
    def from_json(cls, json_str: str) -> WebRTCUserState:
        """Create an instance of WebRTCUserState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in sessions (list)
        _items = []
        if self.sessions:
            for _item in self.sessions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sessions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebRTCUserState:
        """Create an instance of WebRTCUserState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebRTCUserState.parse_obj(obj)

        _obj = WebRTCUserState.parse_obj({
            "user_id": obj.get("userId"),
            "channel_id": obj.get("channelId"),
            "sessions": [WebRTCUserStateSessionsInner.from_dict(_item) for _item in obj.get("sessions")] if obj.get("sessions") is not None else None
        })
        return _obj


