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

from bugcrowd_client.models.get_credential_bucket_response import GetCredentialBucketResponse

class TestGetCredentialBucketResponse(unittest.TestCase):
    """GetCredentialBucketResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCredentialBucketResponse:
        """Test GetCredentialBucketResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCredentialBucketResponse`
        """
        model = GetCredentialBucketResponse()
        if include_optional:
            return GetCredentialBucketResponse(
                data = bugcrowd_client.models.credential_bucket.CredentialBucket(
                    id = '', 
                    type = 'credential_bucket', 
                    links = bugcrowd_client.models.self_link.SelfLink(
                        self = '', ), 
                    attributes = bugcrowd_client.models.credential_bucket_attributes.CredentialBucket_attributes(
                        credential_type = '', 
                        credentials_per_researcher = 56, 
                        description = '', 
                        is_ready = True, 
                        low_balance_threshold = 56, 
                        name = '', ), 
                    relationships = bugcrowd_client.models.credential_bucket_relationships.CredentialBucket_relationships(
                        credentials = bugcrowd_client.models.many_relationship.ManyRelationship(
                            links = bugcrowd_client.models.many_relationship_links.ManyRelationshipLinks(
                                related = bugcrowd_client.models.many_relationship_links_related.ManyRelationshipLinks_related(
                                    href = '', 
                                    meta = bugcrowd_client.models.relationship_count_meta_data.RelationshipCountMetaData(
                                        count = 56, 
                                        total_hits = 56, ), ), ), 
                            data = [
                                bugcrowd_client.models.basic_object.BasicObject(
                                    id = '', 
                                    type = '', )
                                ], ), 
                        bounty = bugcrowd_client.models.single_relationship.SingleRelationship(
                            links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                                related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                                    href = '', ), ), 
                            data = bugcrowd_client.models.basic_object.BasicObject(
                                id = , 
                                type = '', ), ), ), ),
                included = [
                    bugcrowd_client.models.credential.Credential(
                        id = '', 
                        type = 'credential', 
                        links = bugcrowd_client.models.self_link.SelfLink(
                            self = '', ), 
                        attributes = bugcrowd_client.models.credential_attributes.Credential_attributes(
                            user_id = '', 
                            credential_bucket_id = '', 
                            data = { }, ), )
                    ],
                links = bugcrowd_client.models.self_link.SelfLink(
                    self = '', )
            )
        else:
            return GetCredentialBucketResponse(
                data = bugcrowd_client.models.credential_bucket.CredentialBucket(
                    id = '', 
                    type = 'credential_bucket', 
                    links = bugcrowd_client.models.self_link.SelfLink(
                        self = '', ), 
                    attributes = bugcrowd_client.models.credential_bucket_attributes.CredentialBucket_attributes(
                        credential_type = '', 
                        credentials_per_researcher = 56, 
                        description = '', 
                        is_ready = True, 
                        low_balance_threshold = 56, 
                        name = '', ), 
                    relationships = bugcrowd_client.models.credential_bucket_relationships.CredentialBucket_relationships(
                        credentials = bugcrowd_client.models.many_relationship.ManyRelationship(
                            links = bugcrowd_client.models.many_relationship_links.ManyRelationshipLinks(
                                related = bugcrowd_client.models.many_relationship_links_related.ManyRelationshipLinks_related(
                                    href = '', 
                                    meta = bugcrowd_client.models.relationship_count_meta_data.RelationshipCountMetaData(
                                        count = 56, 
                                        total_hits = 56, ), ), ), 
                            data = [
                                bugcrowd_client.models.basic_object.BasicObject(
                                    id = '', 
                                    type = '', )
                                ], ), 
                        bounty = bugcrowd_client.models.single_relationship.SingleRelationship(
                            links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                                related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                                    href = '', ), ), 
                            data = bugcrowd_client.models.basic_object.BasicObject(
                                id = , 
                                type = '', ), ), ), ),
        )
        """

    def testGetCredentialBucketResponse(self):
        """Test GetCredentialBucketResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()