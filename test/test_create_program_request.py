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

from bugcrowd_client.models.create_program_request import CreateProgramRequest

class TestCreateProgramRequest(unittest.TestCase):
    """CreateProgramRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateProgramRequest:
        """Test CreateProgramRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateProgramRequest`
        """
        model = CreateProgramRequest()
        if include_optional:
            return CreateProgramRequest(
                data = bugcrowd_client.models.create_program_request_data.CreateProgramRequest_data(
                    type = 'program', 
                    attributes = bugcrowd_client.models.create_program_request_data_attributes.CreateProgramRequest_data_attributes(
                        name = '', 
                        code = '', ), 
                    relationships = bugcrowd_client.models.create_customer_asset_request_data_relationships.CreateCustomerAssetRequest_data_relationships(
                        organization = bugcrowd_client.models.organization_not_nullable.OrganizationNotNullable(
                            data = bugcrowd_client.models.organization_not_nullable_data.OrganizationNotNullable_data(
                                id = '', 
                                type = 'organization', ), ), ), )
            )
        else:
            return CreateProgramRequest(
                data = bugcrowd_client.models.create_program_request_data.CreateProgramRequest_data(
                    type = 'program', 
                    attributes = bugcrowd_client.models.create_program_request_data_attributes.CreateProgramRequest_data_attributes(
                        name = '', 
                        code = '', ), 
                    relationships = bugcrowd_client.models.create_customer_asset_request_data_relationships.CreateCustomerAssetRequest_data_relationships(
                        organization = bugcrowd_client.models.organization_not_nullable.OrganizationNotNullable(
                            data = bugcrowd_client.models.organization_not_nullable_data.OrganizationNotNullable_data(
                                id = '', 
                                type = 'organization', ), ), ), ),
        )
        """

    def testCreateProgramRequest(self):
        """Test CreateProgramRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
