# coding: utf-8

"""
    Bugcrowd REST API

    This is Bugcrowd's primary REST API and follows the [JSON API specification](https://jsonapi.org/format/).  For more information on how to get started check out the [usage documentation](https://docs.bugcrowd.com/api/usage/) 

    The version of the OpenAPI document: 2024-01-11
    Contact: support@bugcrowd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from bugcrowd_client.models.create_monetary_reward_request import CreateMonetaryRewardRequest

class TestCreateMonetaryRewardRequest(unittest.TestCase):
    """CreateMonetaryRewardRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateMonetaryRewardRequest:
        """Test CreateMonetaryRewardRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateMonetaryRewardRequest`
        """
        model = CreateMonetaryRewardRequest()
        if include_optional:
            return CreateMonetaryRewardRequest(
                data = bugcrowd_client.models.create_monetary_reward_request_data.CreateMonetaryRewardRequest_data(
                    type = 'monetary_reward', 
                    attributes = bugcrowd_client.models.create_monetary_reward_request_data_attributes.CreateMonetaryRewardRequest_data_attributes(
                        amount_cents = 1, 
                        comment = '', ), 
                    relationships = bugcrowd_client.models.create_monetary_reward_request_data_relationships.CreateMonetaryRewardRequest_data_relationships(
                        submission = bugcrowd_client.models.submission_not_nullable.SubmissionNotNullable(
                            data = bugcrowd_client.models.submissions_max1_data_inner.SubmissionsMax1_data_inner(
                                id = '', 
                                type = 'submission', ), ), ), )
            )
        else:
            return CreateMonetaryRewardRequest(
                data = bugcrowd_client.models.create_monetary_reward_request_data.CreateMonetaryRewardRequest_data(
                    type = 'monetary_reward', 
                    attributes = bugcrowd_client.models.create_monetary_reward_request_data_attributes.CreateMonetaryRewardRequest_data_attributes(
                        amount_cents = 1, 
                        comment = '', ), 
                    relationships = bugcrowd_client.models.create_monetary_reward_request_data_relationships.CreateMonetaryRewardRequest_data_relationships(
                        submission = bugcrowd_client.models.submission_not_nullable.SubmissionNotNullable(
                            data = bugcrowd_client.models.submissions_max1_data_inner.SubmissionsMax1_data_inner(
                                id = '', 
                                type = 'submission', ), ), ), ),
        )
        """

    def testCreateMonetaryRewardRequest(self):
        """Test CreateMonetaryRewardRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
