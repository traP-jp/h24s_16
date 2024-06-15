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


class BotEventResult(str, Enum):
    """
    イベント配送結果
    """

    """
    allowed enum values
    """
    OK = 'ok'
    NG = 'ng'
    NE = 'ne'
    DP = 'dp'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BotEventResult from a JSON string"""
        return cls(json.loads(json_str))


