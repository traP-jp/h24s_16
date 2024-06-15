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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from traqapi.models.file_info_thumbnail import FileInfoThumbnail
from traqapi.models.thumbnail_info import ThumbnailInfo

class FileInfo(BaseModel):
    """
    ファイル情報  # noqa: E501
    """
    id: StrictStr = Field(..., description="ファイルUUID")
    name: StrictStr = Field(..., description="ファイル名")
    mime: StrictStr = Field(..., description="MIMEタイプ")
    size: StrictInt = Field(..., description="ファイルサイズ")
    md5: StrictStr = Field(..., description="MD5ハッシュ")
    is_animated_image: StrictBool = Field(..., alias="isAnimatedImage", description="アニメーション画像かどうか")
    created_at: datetime = Field(..., alias="createdAt", description="アップロード日時")
    thumbnails: conlist(ThumbnailInfo) = Field(...)
    thumbnail: Optional[FileInfoThumbnail] = Field(...)
    channel_id: Optional[StrictStr] = Field(..., alias="channelId", description="属しているチャンネルUUID")
    uploader_id: Optional[StrictStr] = Field(..., alias="uploaderId", description="アップロード者UUID")
    __properties = ["id", "name", "mime", "size", "md5", "isAnimatedImage", "createdAt", "thumbnails", "thumbnail", "channelId", "uploaderId"]

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
    def from_json(cls, json_str: str) -> FileInfo:
        """Create an instance of FileInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in thumbnails (list)
        _items = []
        if self.thumbnails:
            for _item in self.thumbnails:
                if _item:
                    _items.append(_item.to_dict())
            _dict['thumbnails'] = _items
        # override the default output from pydantic by calling `to_dict()` of thumbnail
        if self.thumbnail:
            _dict['thumbnail'] = self.thumbnail.to_dict()
        # set to None if thumbnail (nullable) is None
        # and __fields_set__ contains the field
        if self.thumbnail is None and "thumbnail" in self.__fields_set__:
            _dict['thumbnail'] = None

        # set to None if channel_id (nullable) is None
        # and __fields_set__ contains the field
        if self.channel_id is None and "channel_id" in self.__fields_set__:
            _dict['channelId'] = None

        # set to None if uploader_id (nullable) is None
        # and __fields_set__ contains the field
        if self.uploader_id is None and "uploader_id" in self.__fields_set__:
            _dict['uploaderId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FileInfo:
        """Create an instance of FileInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FileInfo.parse_obj(obj)

        _obj = FileInfo.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "mime": obj.get("mime"),
            "size": obj.get("size"),
            "md5": obj.get("md5"),
            "is_animated_image": obj.get("isAnimatedImage"),
            "created_at": obj.get("createdAt"),
            "thumbnails": [ThumbnailInfo.from_dict(_item) for _item in obj.get("thumbnails")] if obj.get("thumbnails") is not None else None,
            "thumbnail": FileInfoThumbnail.from_dict(obj.get("thumbnail")) if obj.get("thumbnail") is not None else None,
            "channel_id": obj.get("channelId"),
            "uploader_id": obj.get("uploaderId")
        })
        return _obj


