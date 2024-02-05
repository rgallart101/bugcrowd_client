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

from bugcrowd_client.models.target_group_relationships import TargetGroupRelationships

class TestTargetGroupRelationships(unittest.TestCase):
    """TargetGroupRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TargetGroupRelationships:
        """Test TargetGroupRelationships
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TargetGroupRelationships`
        """
        model = TargetGroupRelationships()
        if include_optional:
            return TargetGroupRelationships(
                targets = bugcrowd_client.models.many_relationship.ManyRelationship(
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
                program_brief = bugcrowd_client.models.single_relationship.SingleRelationship(
                    links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                        related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                            href = '', ), ), 
                    data = bugcrowd_client.models.basic_object.BasicObject(
                        id = '', 
                        type = '', ), ),
                reward_range = bugcrowd_client.models.single_relationship.SingleRelationship(
                    links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                        related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                            href = '', ), ), 
                    data = bugcrowd_client.models.basic_object.BasicObject(
                        id = '', 
                        type = '', ), )
            )
        else:
            return TargetGroupRelationships(
        )
        """

    def testTargetGroupRelationships(self):
        """Test TargetGroupRelationships"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
