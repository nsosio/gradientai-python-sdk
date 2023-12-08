# coding: utf-8

"""
    Gradient AI API

    Interface for interacting with Gradient AI.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@gradient.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import gradientai.openapi.client
from gradientai.openapi.client.models.fine_tune_model_body_params import FineTuneModelBodyParams  # noqa: E501
from gradientai.openapi.client.rest import ApiException

class TestFineTuneModelBodyParams(unittest.TestCase):
    """FineTuneModelBodyParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FineTuneModelBodyParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FineTuneModelBodyParams`
        """
        model = gradientai.openapi.client.models.fine_tune_model_body_params.FineTuneModelBodyParams()  # noqa: E501
        if include_optional :
            return FineTuneModelBodyParams(
                samples = [
                    gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner.FineTuneModelBodyParams_samples_inner(
                        fine_tuning_parameters = gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner_fine_tuning_parameters.FineTuneModelBodyParams_samples_inner_fineTuningParameters(
                            multiplier = 0, ), 
                        inputs = null, )
                    ]
            )
        else :
            return FineTuneModelBodyParams(
                samples = [
                    gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner.FineTuneModelBodyParams_samples_inner(
                        fine_tuning_parameters = gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner_fine_tuning_parameters.FineTuneModelBodyParams_samples_inner_fineTuningParameters(
                            multiplier = 0, ), 
                        inputs = null, )
                    ],
        )
        """

    def testFineTuneModelBodyParams(self):
        """Test FineTuneModelBodyParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
