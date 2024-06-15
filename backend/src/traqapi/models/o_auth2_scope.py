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





class OAuth2Scope(str, Enum):
    """
    OAuth2スコープ
    """

    """
    allowed enum values
    """
    OPENID = 'openid'
    PROFILE = 'profile'
    READ = 'read'
    WRITE = 'write'
    MANAGE_BOT = 'manage_bot'

    @classmethod
    def from_json(cls, json_str: str) -> OAuth2Scope:
        """Create an instance of OAuth2Scope from a JSON string"""
        return OAuth2Scope(json.loads(json_str))

