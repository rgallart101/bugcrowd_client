# coding: utf-8

"""
    Bugcrowd REST API

    This is Bugcrowd's primary REST API and follows the [JSON API specification](https://jsonapi.org/format/).  For more information on how to get started check out the [usage documentation](https://docs.bugcrowd.com/api/usage/) 

    The version of the OpenAPI document: 2024-01-11
    Contact: support@bugcrowd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictStr, field_validator

from typing import List, Optional

from bugcrowd_client.models.list_targets_response import ListTargetsResponse

from bugcrowd_client.api_client import ApiClient
from bugcrowd_client.api_response import ApiResponse
from bugcrowd_client.rest import RESTResponseType


class TargetResourceApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def list_targets(
        self,
        bugcrowd_version: Annotated[Optional[StrictStr], Field(description="The request header used to test new API versions before updating the pinned account version")] = None,
        fields_organization: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=3)]], Field(description="Limit fields for `organization` resources. If not provided, all fields will be returned")] = None,
        fields_target: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=4)]], Field(description="Limit fields for `target` resources. If not provided, all fields will be returned")] = None,
        page_limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=0)]], Field(description="Limit parameter for pagination (default page[limit] = 25)")] = None,
        page_offset: Annotated[Optional[Annotated[int, Field(le=9900, strict=True, ge=0)]], Field(description="Offset parameter for pagination (default page[offset] = 0 == first page)")] = None,
        filter_organization_id: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=10)]], Field(description="Filter by the UUID of the organization they belong to.")] = None,
        include: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=1)]], Field(description="Related associations that will be returned as a flat list of objects.")] = None,
        filter_target_group_id: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=20)]], Field(description="Filter targets by the group they belong to (Used to paginate targets on a program)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ListTargetsResponse:
        """Index targets

        Returns a list of targets belonging to the organizations of the user.

        :param bugcrowd_version: The request header used to test new API versions before updating the pinned account version
        :type bugcrowd_version: str
        :param fields_organization: Limit fields for `organization` resources. If not provided, all fields will be returned
        :type fields_organization: List[str]
        :param fields_target: Limit fields for `target` resources. If not provided, all fields will be returned
        :type fields_target: List[str]
        :param page_limit: Limit parameter for pagination (default page[limit] = 25)
        :type page_limit: int
        :param page_offset: Offset parameter for pagination (default page[offset] = 0 == first page)
        :type page_offset: int
        :param filter_organization_id: Filter by the UUID of the organization they belong to.
        :type filter_organization_id: List[str]
        :param include: Related associations that will be returned as a flat list of objects.
        :type include: List[str]
        :param filter_target_group_id: Filter targets by the group they belong to (Used to paginate targets on a program)
        :type filter_target_group_id: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_targets_serialize(
            bugcrowd_version=bugcrowd_version,
            fields_organization=fields_organization,
            fields_target=fields_target,
            page_limit=page_limit,
            page_offset=page_offset,
            filter_organization_id=filter_organization_id,
            include=include,
            filter_target_group_id=filter_target_group_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListTargetsResponse",
            '400': "ErrorContent",
            '404': "ErrorContent",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_targets_with_http_info(
        self,
        bugcrowd_version: Annotated[Optional[StrictStr], Field(description="The request header used to test new API versions before updating the pinned account version")] = None,
        fields_organization: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=3)]], Field(description="Limit fields for `organization` resources. If not provided, all fields will be returned")] = None,
        fields_target: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=4)]], Field(description="Limit fields for `target` resources. If not provided, all fields will be returned")] = None,
        page_limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=0)]], Field(description="Limit parameter for pagination (default page[limit] = 25)")] = None,
        page_offset: Annotated[Optional[Annotated[int, Field(le=9900, strict=True, ge=0)]], Field(description="Offset parameter for pagination (default page[offset] = 0 == first page)")] = None,
        filter_organization_id: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=10)]], Field(description="Filter by the UUID of the organization they belong to.")] = None,
        include: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=1)]], Field(description="Related associations that will be returned as a flat list of objects.")] = None,
        filter_target_group_id: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=20)]], Field(description="Filter targets by the group they belong to (Used to paginate targets on a program)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ListTargetsResponse]:
        """Index targets

        Returns a list of targets belonging to the organizations of the user.

        :param bugcrowd_version: The request header used to test new API versions before updating the pinned account version
        :type bugcrowd_version: str
        :param fields_organization: Limit fields for `organization` resources. If not provided, all fields will be returned
        :type fields_organization: List[str]
        :param fields_target: Limit fields for `target` resources. If not provided, all fields will be returned
        :type fields_target: List[str]
        :param page_limit: Limit parameter for pagination (default page[limit] = 25)
        :type page_limit: int
        :param page_offset: Offset parameter for pagination (default page[offset] = 0 == first page)
        :type page_offset: int
        :param filter_organization_id: Filter by the UUID of the organization they belong to.
        :type filter_organization_id: List[str]
        :param include: Related associations that will be returned as a flat list of objects.
        :type include: List[str]
        :param filter_target_group_id: Filter targets by the group they belong to (Used to paginate targets on a program)
        :type filter_target_group_id: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_targets_serialize(
            bugcrowd_version=bugcrowd_version,
            fields_organization=fields_organization,
            fields_target=fields_target,
            page_limit=page_limit,
            page_offset=page_offset,
            filter_organization_id=filter_organization_id,
            include=include,
            filter_target_group_id=filter_target_group_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListTargetsResponse",
            '400': "ErrorContent",
            '404': "ErrorContent",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_targets_without_preload_content(
        self,
        bugcrowd_version: Annotated[Optional[StrictStr], Field(description="The request header used to test new API versions before updating the pinned account version")] = None,
        fields_organization: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=3)]], Field(description="Limit fields for `organization` resources. If not provided, all fields will be returned")] = None,
        fields_target: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=4)]], Field(description="Limit fields for `target` resources. If not provided, all fields will be returned")] = None,
        page_limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=0)]], Field(description="Limit parameter for pagination (default page[limit] = 25)")] = None,
        page_offset: Annotated[Optional[Annotated[int, Field(le=9900, strict=True, ge=0)]], Field(description="Offset parameter for pagination (default page[offset] = 0 == first page)")] = None,
        filter_organization_id: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=10)]], Field(description="Filter by the UUID of the organization they belong to.")] = None,
        include: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=1)]], Field(description="Related associations that will be returned as a flat list of objects.")] = None,
        filter_target_group_id: Annotated[Optional[Annotated[List[StrictStr], Field(max_length=20)]], Field(description="Filter targets by the group they belong to (Used to paginate targets on a program)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Index targets

        Returns a list of targets belonging to the organizations of the user.

        :param bugcrowd_version: The request header used to test new API versions before updating the pinned account version
        :type bugcrowd_version: str
        :param fields_organization: Limit fields for `organization` resources. If not provided, all fields will be returned
        :type fields_organization: List[str]
        :param fields_target: Limit fields for `target` resources. If not provided, all fields will be returned
        :type fields_target: List[str]
        :param page_limit: Limit parameter for pagination (default page[limit] = 25)
        :type page_limit: int
        :param page_offset: Offset parameter for pagination (default page[offset] = 0 == first page)
        :type page_offset: int
        :param filter_organization_id: Filter by the UUID of the organization they belong to.
        :type filter_organization_id: List[str]
        :param include: Related associations that will be returned as a flat list of objects.
        :type include: List[str]
        :param filter_target_group_id: Filter targets by the group they belong to (Used to paginate targets on a program)
        :type filter_target_group_id: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_targets_serialize(
            bugcrowd_version=bugcrowd_version,
            fields_organization=fields_organization,
            fields_target=fields_target,
            page_limit=page_limit,
            page_offset=page_offset,
            filter_organization_id=filter_organization_id,
            include=include,
            filter_target_group_id=filter_target_group_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListTargetsResponse",
            '400': "ErrorContent",
            '404': "ErrorContent",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_targets_serialize(
        self,
        bugcrowd_version,
        fields_organization,
        fields_target,
        page_limit,
        page_offset,
        filter_organization_id,
        include,
        filter_target_group_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            'fields[organization]': 'csv',
            'fields[target]': 'csv',
            'filter[organization_id]': 'csv',
            'include': 'csv',
            'filter[target_group_id]': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if fields_organization is not None:
            
            _query_params.append(('fields[organization]', fields_organization))
            
        if fields_target is not None:
            
            _query_params.append(('fields[target]', fields_target))
            
        if page_limit is not None:
            
            _query_params.append(('page[limit]', page_limit))
            
        if page_offset is not None:
            
            _query_params.append(('page[offset]', page_offset))
            
        if filter_organization_id is not None:
            
            _query_params.append(('filter[organization_id]', filter_organization_id))
            
        if include is not None:
            
            _query_params.append(('include', include))
            
        if filter_target_group_id is not None:
            
            _query_params.append(('filter[target_group_id]', filter_target_group_id))
            
        # process the header parameters
        if bugcrowd_version is not None:
            _header_params['Bugcrowd-Version'] = bugcrowd_version
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/vnd.bugcrowd.v4+json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'tokenAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/targets',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


