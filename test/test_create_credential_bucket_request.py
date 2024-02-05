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

from bugcrowd_client.models.create_credential_bucket_request import CreateCredentialBucketRequest

class TestCreateCredentialBucketRequest(unittest.TestCase):
    """CreateCredentialBucketRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCredentialBucketRequest:
        """Test CreateCredentialBucketRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCredentialBucketRequest`
        """
        model = CreateCredentialBucketRequest()
        if include_optional:
            return CreateCredentialBucketRequest(
                data = bugcrowd_client.models.create_credential_bucket_request_data.CreateCredentialBucketRequest_data(
                    type = 'credential_bucket', 
                    attributes = bugcrowd_client.models.create_credential_bucket_request_data_attributes.CreateCredentialBucketRequest_data_attributes(
                        name = 'My Credential Bucket', 
                        credential_type = 'email', 
                        credentials_per_researcher = 1, 
                        description = 'This bucket is for storing email credentials', 
                        is_ready = True, 
                        low_balance_threshold = 10, ), 
                    relationships = bugcrowd_client.models.create_credential_bucket_request_data_relationships.CreateCredentialBucketRequest_data_relationships(
                        program = bugcrowd_client.models.program_not_nullable.ProgramNotNullable(
                            data = bugcrowd_client.models.program_not_nullable_data.ProgramNotNullable_data(
                                id = '', 
                                type = 'program', ), ), ), )
            )
        else:
            return CreateCredentialBucketRequest(
                data = bugcrowd_client.models.create_credential_bucket_request_data.CreateCredentialBucketRequest_data(
                    type = 'credential_bucket', 
                    attributes = bugcrowd_client.models.create_credential_bucket_request_data_attributes.CreateCredentialBucketRequest_data_attributes(
                        name = 'My Credential Bucket', 
                        credential_type = 'email', 
                        credentials_per_researcher = 1, 
                        description = 'This bucket is for storing email credentials', 
                        is_ready = True, 
                        low_balance_threshold = 10, ), 
                    relationships = bugcrowd_client.models.create_credential_bucket_request_data_relationships.CreateCredentialBucketRequest_data_relationships(
                        program = bugcrowd_client.models.program_not_nullable.ProgramNotNullable(
                            data = bugcrowd_client.models.program_not_nullable_data.ProgramNotNullable_data(
                                id = '', 
                                type = 'program', ), ), ), ),
        )
        """

    def testCreateCredentialBucketRequest(self):
        """Test CreateCredentialBucketRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
