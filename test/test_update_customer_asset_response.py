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

from bugcrowd_client.models.update_customer_asset_response import UpdateCustomerAssetResponse

class TestUpdateCustomerAssetResponse(unittest.TestCase):
    """UpdateCustomerAssetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateCustomerAssetResponse:
        """Test UpdateCustomerAssetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCustomerAssetResponse`
        """
        model = UpdateCustomerAssetResponse()
        if include_optional:
            return UpdateCustomerAssetResponse(
                data = bugcrowd_client.models.customer_asset.CustomerAsset(
                    id = '', 
                    type = 'customer_asset', 
                    links = bugcrowd_client.models.self_link.SelfLink(
                        self = '', ), 
                    attributes = bugcrowd_client.models.customer_asset_attributes.CustomerAsset_attributes(
                        name = '', 
                        type = '["executable"]', 
                        description = '', 
                        host_name = '', 
                        port_list = [3000,3006,8000], 
                        ip_address = ["192.168.6.6","192.178.7.8/24"], 
                        approved = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        source = 'platform', 
                        tags = {"cpe":"cpe:2.3:a:1024cms:1024_cms:1.4.1:*:*:*:*:*:*:*","cve":["CVE-2022-4258","CVE-2014-1122"],"additional":["javascript","java","golang"]}, 
                        last_modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    relationships = bugcrowd_client.models.customer_asset_relationships.CustomerAsset_relationships(
                        created_by = bugcrowd_client.models.single_relationship.SingleRelationship(
                            links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                                related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                                    href = '', ), ), 
                            data = bugcrowd_client.models.basic_object.BasicObject(
                                id = '', 
                                type = '', ), ), 
                        last_modified_by = bugcrowd_client.models.single_relationship.SingleRelationship(
                            links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                                related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                                    href = '', ), ), 
                            data = bugcrowd_client.models.basic_object.BasicObject(
                                id = '', 
                                type = '', ), ), 
                        organization = , ), )
            )
        else:
            return UpdateCustomerAssetResponse(
                data = bugcrowd_client.models.customer_asset.CustomerAsset(
                    id = '', 
                    type = 'customer_asset', 
                    links = bugcrowd_client.models.self_link.SelfLink(
                        self = '', ), 
                    attributes = bugcrowd_client.models.customer_asset_attributes.CustomerAsset_attributes(
                        name = '', 
                        type = '["executable"]', 
                        description = '', 
                        host_name = '', 
                        port_list = [3000,3006,8000], 
                        ip_address = ["192.168.6.6","192.178.7.8/24"], 
                        approved = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        source = 'platform', 
                        tags = {"cpe":"cpe:2.3:a:1024cms:1024_cms:1.4.1:*:*:*:*:*:*:*","cve":["CVE-2022-4258","CVE-2014-1122"],"additional":["javascript","java","golang"]}, 
                        last_modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    relationships = bugcrowd_client.models.customer_asset_relationships.CustomerAsset_relationships(
                        created_by = bugcrowd_client.models.single_relationship.SingleRelationship(
                            links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                                related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                                    href = '', ), ), 
                            data = bugcrowd_client.models.basic_object.BasicObject(
                                id = '', 
                                type = '', ), ), 
                        last_modified_by = bugcrowd_client.models.single_relationship.SingleRelationship(
                            links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                                related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                                    href = '', ), ), 
                            data = bugcrowd_client.models.basic_object.BasicObject(
                                id = '', 
                                type = '', ), ), 
                        organization = , ), ),
        )
        """

    def testUpdateCustomerAssetResponse(self):
        """Test UpdateCustomerAssetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
