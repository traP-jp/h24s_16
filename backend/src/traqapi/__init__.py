# coding: utf-8

# flake8: noqa

"""
    traQ v3

    traQ v3 API

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from traqapi.api.activity_api import ActivityApi
from traqapi.api.authentication_api import AuthenticationApi
from traqapi.api.bot_api import BotApi
from traqapi.api.channel_api import ChannelApi
from traqapi.api.clip_api import ClipApi
from traqapi.api.file_api import FileApi
from traqapi.api.group_api import GroupApi
from traqapi.api.me_api import MeApi
from traqapi.api.message_api import MessageApi
from traqapi.api.notification_api import NotificationApi
from traqapi.api.oauth2_api import Oauth2Api
from traqapi.api.ogp_api import OgpApi
from traqapi.api.pin_api import PinApi
from traqapi.api.public_api import PublicApi
from traqapi.api.stamp_api import StampApi
from traqapi.api.star_api import StarApi
from traqapi.api.user_api import UserApi
from traqapi.api.user_tag_api import UserTagApi
from traqapi.api.webhook_api import WebhookApi
from traqapi.api.webrtc_api import WebrtcApi

# import ApiClient
from traqapi.api_response import ApiResponse
from traqapi.api_client import ApiClient
from traqapi.configuration import Configuration
from traqapi.exceptions import OpenApiException
from traqapi.exceptions import ApiTypeError
from traqapi.exceptions import ApiValueError
from traqapi.exceptions import ApiKeyError
from traqapi.exceptions import ApiAttributeError
from traqapi.exceptions import ApiException

# import models into sdk package
from traqapi.models.active_o_auth2_token import ActiveOAuth2Token
from traqapi.models.activity_timeline_message import ActivityTimelineMessage
from traqapi.models.bot import Bot
from traqapi.models.bot_detail import BotDetail
from traqapi.models.bot_event_log import BotEventLog
from traqapi.models.bot_event_result import BotEventResult
from traqapi.models.bot_mode import BotMode
from traqapi.models.bot_state import BotState
from traqapi.models.bot_tokens import BotTokens
from traqapi.models.bot_user import BotUser
from traqapi.models.channel import Channel
from traqapi.models.channel_event import ChannelEvent
from traqapi.models.channel_event_detail import ChannelEventDetail
from traqapi.models.channel_list import ChannelList
from traqapi.models.channel_stats import ChannelStats
from traqapi.models.channel_stats_stamp import ChannelStatsStamp
from traqapi.models.channel_stats_user import ChannelStatsUser
from traqapi.models.channel_subscribe_level import ChannelSubscribeLevel
from traqapi.models.channel_topic import ChannelTopic
from traqapi.models.channel_view_state import ChannelViewState
from traqapi.models.channel_viewer import ChannelViewer
from traqapi.models.child_created_event import ChildCreatedEvent
from traqapi.models.clip_folder import ClipFolder
from traqapi.models.clipped_message import ClippedMessage
from traqapi.models.dm_channel import DMChannel
from traqapi.models.external_provider_user import ExternalProviderUser
from traqapi.models.file_info import FileInfo
from traqapi.models.file_info_thumbnail import FileInfoThumbnail
from traqapi.models.forced_notification_changed_event import ForcedNotificationChangedEvent
from traqapi.models.get_bot200_response import GetBot200Response
from traqapi.models.get_client200_response import GetClient200Response
from traqapi.models.get_notify_citation import GetNotifyCitation
from traqapi.models.login_session import LoginSession
from traqapi.models.message import Message
from traqapi.models.message_clip import MessageClip
from traqapi.models.message_pin import MessagePin
from traqapi.models.message_search_result import MessageSearchResult
from traqapi.models.message_stamp import MessageStamp
from traqapi.models.my_channel_view_state import MyChannelViewState
from traqapi.models.my_user_detail import MyUserDetail
from traqapi.models.name_changed_event import NameChangedEvent
from traqapi.models.o_auth2_client import OAuth2Client
from traqapi.models.o_auth2_client_detail import OAuth2ClientDetail
from traqapi.models.o_auth2_prompt import OAuth2Prompt
from traqapi.models.o_auth2_response_type import OAuth2ResponseType
from traqapi.models.o_auth2_scope import OAuth2Scope
from traqapi.models.o_auth2_token import OAuth2Token
from traqapi.models.oidc_traq_user_info import OIDCTraqUserInfo
from traqapi.models.oidc_user_info import OIDCUserInfo
from traqapi.models.ogp import Ogp
from traqapi.models.ogp_media import OgpMedia
from traqapi.models.parent_changed_event import ParentChangedEvent
from traqapi.models.patch_bot_request import PatchBotRequest
from traqapi.models.patch_channel_request import PatchChannelRequest
from traqapi.models.patch_channel_subscribers_request import PatchChannelSubscribersRequest
from traqapi.models.patch_client_request import PatchClientRequest
from traqapi.models.patch_clip_folder_request import PatchClipFolderRequest
from traqapi.models.patch_group_member_request import PatchGroupMemberRequest
from traqapi.models.patch_me_request import PatchMeRequest
from traqapi.models.patch_stamp_palette_request import PatchStampPaletteRequest
from traqapi.models.patch_stamp_request import PatchStampRequest
from traqapi.models.patch_user_group_request import PatchUserGroupRequest
from traqapi.models.patch_user_request import PatchUserRequest
from traqapi.models.patch_user_tag_request import PatchUserTagRequest
from traqapi.models.patch_webhook_request import PatchWebhookRequest
from traqapi.models.pin import Pin
from traqapi.models.pin_added_event import PinAddedEvent
from traqapi.models.pin_removed_event import PinRemovedEvent
from traqapi.models.post_bot_action_join_request import PostBotActionJoinRequest
from traqapi.models.post_bot_action_leave_request import PostBotActionLeaveRequest
from traqapi.models.post_bot_request import PostBotRequest
from traqapi.models.post_channel_request import PostChannelRequest
from traqapi.models.post_client_request import PostClientRequest
from traqapi.models.post_clip_folder_message_request import PostClipFolderMessageRequest
from traqapi.models.post_clip_folder_request import PostClipFolderRequest
from traqapi.models.post_link_external_account import PostLinkExternalAccount
from traqapi.models.post_login_request import PostLoginRequest
from traqapi.models.post_message_request import PostMessageRequest
from traqapi.models.post_message_stamp_request import PostMessageStampRequest
from traqapi.models.post_my_fcm_device_request import PostMyFCMDeviceRequest
from traqapi.models.post_stamp_palette_request import PostStampPaletteRequest
from traqapi.models.post_star_request import PostStarRequest
from traqapi.models.post_unlink_external_account import PostUnlinkExternalAccount
from traqapi.models.post_user_group_admin_request import PostUserGroupAdminRequest
from traqapi.models.post_user_group_request import PostUserGroupRequest
from traqapi.models.post_user_request import PostUserRequest
from traqapi.models.post_user_tag_request import PostUserTagRequest
from traqapi.models.post_web_rtc_authenticate_request import PostWebRTCAuthenticateRequest
from traqapi.models.post_webhook_request import PostWebhookRequest
from traqapi.models.put_channel_subscribe_level_request import PutChannelSubscribeLevelRequest
from traqapi.models.put_channel_subscribers_request import PutChannelSubscribersRequest
from traqapi.models.put_channel_topic_request import PutChannelTopicRequest
from traqapi.models.put_my_password_request import PutMyPasswordRequest
from traqapi.models.put_notify_citation_request import PutNotifyCitationRequest
from traqapi.models.put_user_password_request import PutUserPasswordRequest
from traqapi.models.stamp import Stamp
from traqapi.models.stamp_history_entry import StampHistoryEntry
from traqapi.models.stamp_palette import StampPalette
from traqapi.models.stamp_stats import StampStats
from traqapi.models.stamp_with_thumbnail import StampWithThumbnail
from traqapi.models.subscribers_changed_event import SubscribersChangedEvent
from traqapi.models.tag import Tag
from traqapi.models.thumbnail_info import ThumbnailInfo
from traqapi.models.thumbnail_type import ThumbnailType
from traqapi.models.topic_changed_event import TopicChangedEvent
from traqapi.models.unread_channel import UnreadChannel
from traqapi.models.user import User
from traqapi.models.user_account_state import UserAccountState
from traqapi.models.user_detail import UserDetail
from traqapi.models.user_group import UserGroup
from traqapi.models.user_group_member import UserGroupMember
from traqapi.models.user_permission import UserPermission
from traqapi.models.user_settings import UserSettings
from traqapi.models.user_stats import UserStats
from traqapi.models.user_stats_stamp import UserStatsStamp
from traqapi.models.user_subscribe_state import UserSubscribeState
from traqapi.models.user_tag import UserTag
from traqapi.models.version import Version
from traqapi.models.version_flags import VersionFlags
from traqapi.models.visibility_changed_event import VisibilityChangedEvent
from traqapi.models.web_rtc_authenticate_result import WebRTCAuthenticateResult
from traqapi.models.web_rtc_user_state import WebRTCUserState
from traqapi.models.web_rtc_user_state_sessions_inner import WebRTCUserStateSessionsInner
from traqapi.models.webhook import Webhook