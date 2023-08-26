# gradientai-python-sdk
Interface for interacting with Gradient AI.

[![PyPI version](https://badge.fury.io/py/gradientai.svg)](https://badge.fury.io/py/gradientai)


The gradientai-python-sdk library provides convenient access to the [Gradient AI](https://www.gradient.ai/) from applications written in the Python language. It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses.

## Requirements

Python 3.7+

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install gradientai
```

Then import the package:

```python
import gradientai
```

## Getting Started

Please follow the installation procedure and then run the following:

```python

import time
import gradientai
from gradientai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gradient.ai/api
# See configuration.py for a list of all supported configuration parameters.
configuration = gradientai.Configuration(
    host = "https://api.gradient.ai/api"
)

# The client must configure the authentication parameter for being able to make the call. Gradient uses
# access tokens, which can be generated by going to https://auth.gradient.ai/select-workspace and selecting
# "Access tokens" under the profile drop-down.

# Configure Bearer authorization: AccessToken
configuration = gradientai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with gradientai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gradientai.ModelsApi(api_client)
    id = 'id_example' # str | 
    x_gradient_workspace_id = 'x_gradient_workspace_id_example' # str | 
    complete_model_body_params = gradientai.CompleteModelBodyParams() # CompleteModelBodyParams | 

    try:
        # Complete model
        api_response = api_instance.complete_model(id, x_gradient_workspace_id, complete_model_body_params)
        print("The response of ModelsApi->complete_model:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ModelsApi->complete_model: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ModelsApi* | [**complete_model**](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/ModelsApi.md#complete_model) | **POST** /models/{id}/complete | Complete model
*ModelsApi* | [**create_model**](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/ModelsApi.md#create_model) | **POST** /models | Create model
*ModelsApi* | [**delete_model**](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/ModelsApi.md#delete_model) | **DELETE** /models/{id} | Delete model.
*ModelsApi* | [**fine_tune_model**](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/ModelsApi.md#fine_tune_model) | **POST** /models/{id}/fine-tune | Fine-tune model
*ModelsApi* | [**get_model**](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/ModelsApi.md#get_model) | **GET** /models/{id} | Describe model
*ModelsApi* | [**list_models**](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/ModelsApi.md#list_models) | **GET** /models | List available models


## Documentation For Models

 - [BaseModel](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/BaseModel.md)
 - [CompleteModelBodyParams](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/CompleteModelBodyParams.md)
 - [CompleteModelError](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/CompleteModelError.md)
 - [CompleteModelSuccess](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/CompleteModelSuccess.md)
 - [CreateModelError](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/CreateModelError.md)
 - [CreateModelRequestBody](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/CreateModelRequestBody.md)
 - [CreateModelRequestBodyInitialHyperparameters](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/CreateModelRequestBodyInitialHyperparameters.md)
 - [CreateModelRequestBodyInitialHyperparametersLoraHyperparameters](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/CreateModelRequestBodyInitialHyperparametersLoraHyperparameters.md)
 - [CreateModelRequestBodyInitialHyperparametersTrainingArguments](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/CreateModelRequestBodyInitialHyperparametersTrainingArguments.md)
 - [CreateModelRequestBodyModel](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/CreateModelRequestBodyModel.md)
 - [CreateModelSuccess](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/CreateModelSuccess.md)
 - [DeleteModelError](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/DeleteModelError.md)
 - [FineTuneModelError](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/FineTuneModelError.md)
 - [FineTuneModelRequestBody](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/FineTuneModelRequestBody.md)
 - [FineTuneModelRequestBodySamplesInner](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/FineTuneModelRequestBodySamplesInner.md)
 - [FineTuneModelRequestBodySamplesInnerFineTuningParameters](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/FineTuneModelRequestBodySamplesInnerFineTuningParameters.md)
 - [FineTuneModelSuccess](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/FineTuneModelSuccess.md)
 - [GetModelError](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/GetModelError.md)
 - [GetModelSuccess](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/GetModelSuccess.md)
 - [ListModelsError](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/ListModelsError.md)
 - [ListModelsSuccess](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/ListModelsSuccess.md)
 - [ListModelsSuccessModelsInner](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/ListModelsSuccessModelsInner.md)
 - [ModelAdapter](https://github.com/Preemo-Inc/gradientai-python-sdk/blob/main/docs/ModelAdapter.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="AccessToken"></a>
### AccessToken

- **Type**: Bearer authentication


## Author

support@gradient.ai


