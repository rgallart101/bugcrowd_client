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

from bugcrowd_client.models.create_access_invitation_request_data_attributes import CreateAccessInvitationRequestDataAttributes

class TestCreateAccessInvitationRequestDataAttributes(unittest.TestCase):
    """CreateAccessInvitationRequestDataAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAccessInvitationRequestDataAttributes:
        """Test CreateAccessInvitationRequestDataAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAccessInvitationRequestDataAttributes`
        """
        model = CreateAccessInvitationRequestDataAttributes()
        if include_optional:
            return CreateAccessInvitationRequestDataAttributes(
                grantee_email = ''
            )
        else:
            return CreateAccessInvitationRequestDataAttributes(
                grantee_email = '',
        )
        """

    def testCreateAccessInvitationRequestDataAttributes(self):
        """Test CreateAccessInvitationRequestDataAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
