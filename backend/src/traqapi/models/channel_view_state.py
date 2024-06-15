# coding: utf-8

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ChannelViewState(str, Enum):
    """
    閲覧状態
    """

    """
    allowed enum values
    """
    NONE = 'none'
    MONITORING = 'monitoring'
    EDITING = 'editing'

    @classmethod
    def from_json(cls, json_str: str) -> ChannelViewState:
        """Create an instance of ChannelViewState from a JSON string"""
        return ChannelViewState(json.loads(json_str))

