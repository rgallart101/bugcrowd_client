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

from bugcrowd_client.models.create_monetary_reward_request_data_attributes import CreateMonetaryRewardRequestDataAttributes

class TestCreateMonetaryRewardRequestDataAttributes(unittest.TestCase):
    """CreateMonetaryRewardRequestDataAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateMonetaryRewardRequestDataAttributes:
        """Test CreateMonetaryRewardRequestDataAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateMonetaryRewardRequestDataAttributes`
        """
        model = CreateMonetaryRewardRequestDataAttributes()
        if include_optional:
            return CreateMonetaryRewardRequestDataAttributes(
                amount_cents = 1,
                comment = ''
            )
        else:
            return CreateMonetaryRewardRequestDataAttributes(
                amount_cents = 1,
        )
        """

    def testCreateMonetaryRewardRequestDataAttributes(self):
        """Test CreateMonetaryRewardRequestDataAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
