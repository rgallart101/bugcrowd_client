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

from bugcrowd_client.models.create_customer_asset_request_data_attributes import CreateCustomerAssetRequestDataAttributes

class TestCreateCustomerAssetRequestDataAttributes(unittest.TestCase):
    """CreateCustomerAssetRequestDataAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCustomerAssetRequestDataAttributes:
        """Test CreateCustomerAssetRequestDataAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCustomerAssetRequestDataAttributes`
        """
        model = CreateCustomerAssetRequestDataAttributes()
        if include_optional:
            return CreateCustomerAssetRequestDataAttributes(
                name = '',
                type = 'domain',
                description = '',
                host_name = 'example.bugcrowd.com',
                port_list = [3000,3001,8000],
                ip_address = ["192.168.6.6","192.178.7.8/24"],
                approved = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                attributes = [{"key":"custom_attribute_name","value":"custom_attribute_value"}],
                tags = {"cpe":"cpe:2.3:a:1024cms:1024_cms:1.4.1:*:*:*:*:*:*:*","cve":["CVE-2022-4258","CVE-2014-1122"],"additional":["javascript","java","golang"]}
            )
        else:
            return CreateCustomerAssetRequestDataAttributes(
                name = '',
                type = 'domain',
        )
        """

    def testCreateCustomerAssetRequestDataAttributes(self):
        """Test CreateCustomerAssetRequestDataAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
