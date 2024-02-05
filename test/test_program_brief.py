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

from bugcrowd_client.models.program_brief import ProgramBrief

class TestProgramBrief(unittest.TestCase):
    """ProgramBrief unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProgramBrief:
        """Test ProgramBrief
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProgramBrief`
        """
        model = ProgramBrief()
        if include_optional:
            return ProgramBrief(
                id = '',
                type = 'program_brief',
                links = bugcrowd_client.models.self_link.SelfLink(
                    self = '', ),
                attributes = bugcrowd_client.models.program_brief_attributes.ProgramBrief_attributes(
                    coordinated_disclosure = True, 
                    created_at = '', 
                    demo = True, 
                    description = '', 
                    tagline = '', 
                    rewards_overview = '', 
                    targets_overview = '', ),
                relationships = bugcrowd_client.models.program_brief_relationships.ProgramBrief_relationships(
                    program = bugcrowd_client.models.single_relationship.SingleRelationship(
                        links = bugcrowd_client.models.single_relationship_links.SingleRelationshipLinks(
                            related = bugcrowd_client.models.single_relationship_links_related.SingleRelationshipLinks_related(
                                href = '', ), ), 
                        data = bugcrowd_client.models.basic_object.BasicObject(
                            id = '', 
                            type = '', ), ), 
                    target_groups = bugcrowd_client.models.many_relationship.ManyRelationship(
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
                            ], ), )
            )
        else:
            return ProgramBrief(
                id = '',
                type = 'program_brief',
        )
        """

    def testProgramBrief(self):
        """Test ProgramBrief"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()