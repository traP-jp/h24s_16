# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class BotState(int, Enum):
    """
    BOT状態 0: 停止 1: 有効 2: 一時停止
    """

    """
    allowed enum values
    """
    deactivated = 0
    active = 1
    suspended = 2

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BotState from a JSON string"""
        return cls(json.loads(json_str))


