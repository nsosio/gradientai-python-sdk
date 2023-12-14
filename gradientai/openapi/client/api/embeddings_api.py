# coding: utf-8

"""
    Gradient AI API

    Interface for interacting with Gradient AI.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@gradient.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import StrictStr, constr

from gradientai.openapi.client.models.generate_embedding_body_params import GenerateEmbeddingBodyParams
from gradientai.openapi.client.models.generate_embedding_success import GenerateEmbeddingSuccess
from gradientai.openapi.client.models.list_embeddings_success import ListEmbeddingsSuccess

from gradientai.openapi.client.api_client import ApiClient
from gradientai.openapi.client.api_response import ApiResponse
from gradientai.openapi.client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EmbeddingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def generate_embedding(self, slug : StrictStr, x_gradient_workspace_id : constr(strict=True, min_length=1), generate_embedding_body_params : GenerateEmbeddingBodyParams, **kwargs) -> GenerateEmbeddingSuccess:  # noqa: E501
        """Generate embeddings  # noqa: E501

        Generates normalized embeddings with the given embeddings model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_embedding(slug, x_gradient_workspace_id, generate_embedding_body_params, async_req=True)
        >>> result = thread.get()

        :param slug: (required)
        :type slug: str
        :param x_gradient_workspace_id: (required)
        :type x_gradient_workspace_id: str
        :param generate_embedding_body_params: (required)
        :type generate_embedding_body_params: GenerateEmbeddingBodyParams
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GenerateEmbeddingSuccess
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the generate_embedding_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.generate_embedding_with_http_info(slug, x_gradient_workspace_id, generate_embedding_body_params, **kwargs)  # noqa: E501

    @validate_arguments
    def generate_embedding_with_http_info(self, slug : StrictStr, x_gradient_workspace_id : constr(strict=True, min_length=1), generate_embedding_body_params : GenerateEmbeddingBodyParams, **kwargs) -> ApiResponse:  # noqa: E501
        """Generate embeddings  # noqa: E501

        Generates normalized embeddings with the given embeddings model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_embedding_with_http_info(slug, x_gradient_workspace_id, generate_embedding_body_params, async_req=True)
        >>> result = thread.get()

        :param slug: (required)
        :type slug: str
        :param x_gradient_workspace_id: (required)
        :type x_gradient_workspace_id: str
        :param generate_embedding_body_params: (required)
        :type generate_embedding_body_params: GenerateEmbeddingBodyParams
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GenerateEmbeddingSuccess, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'slug',
            'x_gradient_workspace_id',
            'generate_embedding_body_params'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_embedding" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['slug']:
            _path_params['slug'] = _params['slug']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['x_gradient_workspace_id']:
            _header_params['x-gradient-workspace-id'] = _params['x_gradient_workspace_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['generate_embedding_body_params'] is not None:
            _body_params = _params['generate_embedding_body_params']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AccessToken']  # noqa: E501

        _response_types_map = {
            '200': "GenerateEmbeddingSuccess",
            '4XX': "GenerateEmbeddingError",
        }

        return self.api_client.call_api(
            '/embeddings/{slug}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_embeddings(self, x_gradient_workspace_id : constr(strict=True, min_length=1), **kwargs) -> ListEmbeddingsSuccess:  # noqa: E501
        """List available embeddings models  # noqa: E501

        Lists the currently available embeddings models and provides basic information, such as the slug.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_embeddings(x_gradient_workspace_id, async_req=True)
        >>> result = thread.get()

        :param x_gradient_workspace_id: (required)
        :type x_gradient_workspace_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListEmbeddingsSuccess
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_embeddings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_embeddings_with_http_info(x_gradient_workspace_id, **kwargs)  # noqa: E501

    @validate_arguments
    def list_embeddings_with_http_info(self, x_gradient_workspace_id : constr(strict=True, min_length=1), **kwargs) -> ApiResponse:  # noqa: E501
        """List available embeddings models  # noqa: E501

        Lists the currently available embeddings models and provides basic information, such as the slug.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_embeddings_with_http_info(x_gradient_workspace_id, async_req=True)
        >>> result = thread.get()

        :param x_gradient_workspace_id: (required)
        :type x_gradient_workspace_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListEmbeddingsSuccess, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'x_gradient_workspace_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_embeddings" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['x_gradient_workspace_id']:
            _header_params['x-gradient-workspace-id'] = _params['x_gradient_workspace_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AccessToken']  # noqa: E501

        _response_types_map = {
            '200': "ListEmbeddingsSuccess",
            '4XX': "ListEmbeddingsError",
        }

        return self.api_client.call_api(
            '/embeddings', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
