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

from bugcrowd_client.models.archive_customer_asset_request import ArchiveCustomerAssetRequest

class TestArchiveCustomerAssetRequest(unittest.TestCase):
    """ArchiveCustomerAssetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArchiveCustomerAssetRequest:
        """Test ArchiveCustomerAssetRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArchiveCustomerAssetRequest`
        """
        model = ArchiveCustomerAssetRequest()
        if include_optional:
            return ArchiveCustomerAssetRequest(
                data = bugcrowd_client.models.archive_customer_asset_request_data.ArchiveCustomerAssetRequest_data(
                    type = 'customer_asset', 
                    attributes = bugcrowd_client.models.archive_customer_asset_request_data_attributes.ArchiveCustomerAssetRequest_data_attributes(
                        reason = 'stopped_existing', 
                        comment = '', ), 
                    relationships = bugcrowd_client.models.update_customer_asset_request_data_relationships.UpdateCustomerAssetRequest_data_relationships(
                        organization = bugcrowd_client.models.organization_nullable.OrganizationNullable(
                            data = bugcrowd_client.models.organization_nullable_data.OrganizationNullable_data(
                                id = '', 
                                type = 'organization', ), ), ), )
            )
        else:
            return ArchiveCustomerAssetRequest(
                data = bugcrowd_client.models.archive_customer_asset_request_data.ArchiveCustomerAssetRequest_data(
                    type = 'customer_asset', 
                    attributes = bugcrowd_client.models.archive_customer_asset_request_data_attributes.ArchiveCustomerAssetRequest_data_attributes(
                        reason = 'stopped_existing', 
                        comment = '', ), 
                    relationships = bugcrowd_client.models.update_customer_asset_request_data_relationships.UpdateCustomerAssetRequest_data_relationships(
                        organization = bugcrowd_client.models.organization_nullable.OrganizationNullable(
                            data = bugcrowd_client.models.organization_nullable_data.OrganizationNullable_data(
                                id = '', 
                                type = 'organization', ), ), ), ),
        )
        """

    def testArchiveCustomerAssetRequest(self):
        """Test ArchiveCustomerAssetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()