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


class UserPermission(str, Enum):
    """
    ユーザー権限
    """

    """
    allowed enum values
    """
    GET_WEBHOOK = 'get_webhook'
    CREATE_WEBHOOK = 'create_webhook'
    EDIT_WEBHOOK = 'edit_webhook'
    DELETE_WEBHOOK = 'delete_webhook'
    ACCESS_OTHERS_WEBHOOK = 'access_others_webhook'
    GET_BOT = 'get_bot'
    CREATE_BOT = 'create_bot'
    EDIT_BOT = 'edit_bot'
    DELETE_BOT = 'delete_bot'
    ACCESS_OTHERS_BOT = 'access_others_bot'
    BOT_ACTION_JOIN_CHANNEL = 'bot_action_join_channel'
    BOT_ACTION_LEAVE_CHANNEL = 'bot_action_leave_channel'
    CREATE_CHANNEL = 'create_channel'
    GET_CHANNEL = 'get_channel'
    EDIT_CHANNEL = 'edit_channel'
    DELETE_CHANNEL = 'delete_channel'
    CHANGE_PARENT_CHANNEL = 'change_parent_channel'
    EDIT_CHANNEL_TOPIC = 'edit_channel_topic'
    GET_CHANNEL_STAR = 'get_channel_star'
    EDIT_CHANNEL_STAR = 'edit_channel_star'
    GET_MY_TOKENS = 'get_my_tokens'
    REVOKE_MY_TOKEN = 'revoke_my_token'
    GET_CLIENTS = 'get_clients'
    CREATE_CLIENT = 'create_client'
    EDIT_MY_CLIENT = 'edit_my_client'
    DELETE_MY_CLIENT = 'delete_my_client'
    MANAGE_OTHERS_CLIENT = 'manage_others_client'
    UPLOAD_FILE = 'upload_file'
    DOWNLOAD_FILE = 'download_file'
    DELETE_FILE = 'delete_file'
    GET_MESSAGE = 'get_message'
    POST_MESSAGE = 'post_message'
    EDIT_MESSAGE = 'edit_message'
    DELETE_MESSAGE = 'delete_message'
    REPORT_MESSAGE = 'report_message'
    GET_MESSAGE_REPORTS = 'get_message_reports'
    CREATE_MESSAGE_PIN = 'create_message_pin'
    DELETE_MESSAGE_PIN = 'delete_message_pin'
    GET_CHANNEL_SUBSCRIPTION = 'get_channel_subscription'
    EDIT_CHANNEL_SUBSCRIPTION = 'edit_channel_subscription'
    CONNECT_NOTIFICATION_STREAM = 'connect_notification_stream'
    REGISTER_FCM_DEVICE = 'register_fcm_device'
    GET_STAMP = 'get_stamp'
    CREATE_STAMP = 'create_stamp'
    EDIT_STAMP = 'edit_stamp'
    EDIT_STAMP_CREATED_BY_OTHERS = 'edit_stamp_created_by_others'
    DELETE_STAMP = 'delete_stamp'
    ADD_MESSAGE_STAMP = 'add_message_stamp'
    REMOVE_MESSAGE_STAMP = 'remove_message_stamp'
    GET_MY_STAMP_HISTORY = 'get_my_stamp_history'
    GET_STAMP_PALETTE = 'get_stamp_palette'
    CREATE_STAMP_PALETTE = 'create_stamp_palette'
    EDIT_STAMP_PALETTE = 'edit_stamp_palette'
    DELETE_STAMP_PALETTE = 'delete_stamp_palette'
    GET_USER = 'get_user'
    REGISTER_USER = 'register_user'
    GET_ME = 'get_me'
    GET_OIDC_USERINFO = 'get_oidc_userinfo'
    EDIT_ME = 'edit_me'
    CHANGE_MY_ICON = 'change_my_icon'
    CHANGE_MY_PASSWORD = 'change_my_password'
    EDIT_OTHER_USERS = 'edit_other_users'
    GET_USER_QR_CODE = 'get_user_qr_code'
    GET_USER_TAG = 'get_user_tag'
    EDIT_USER_TAG = 'edit_user_tag'
    GET_USER_GROUP = 'get_user_group'
    CREATE_USER_GROUP = 'create_user_group'
    CREATE_SPECIAL_USER_GROUP = 'create_special_user_group'
    EDIT_USER_GROUP = 'edit_user_group'
    DELETE_USER_GROUP = 'delete_user_group'
    EDIT_OTHERS_USER_GROUP = 'edit_others_user_group'
    WEB_RTC = 'web_rtc'
    GET_MY_SESSIONS = 'get_my_sessions'
    DELETE_MY_SESSIONS = 'delete_my_sessions'
    GET_MY_EXTERNAL_ACCOUNT = 'get_my_external_account'
    EDIT_MY_EXTERNAL_ACCOUNT = 'edit_my_external_account'
    GET_UNREAD = 'get_unread'
    DELETE_UNREAD = 'delete_unread'
    GET_CLIP_FOLDER = 'get_clip_folder'
    CREATE_CLIP_FOLDER = 'create_clip_folder'
    EDIT_CLIP_FOLDER = 'edit_clip_folder'
    DELETE_CLIP_FOLDER = 'delete_clip_folder'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserPermission from a JSON string"""
        return cls(json.loads(json_str))


