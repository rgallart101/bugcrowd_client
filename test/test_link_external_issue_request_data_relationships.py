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

from bugcrowd_client.models.link_external_issue_request_data_relationships import LinkExternalIssueRequestDataRelationships

class TestLinkExternalIssueRequestDataRelationships(unittest.TestCase):
    """LinkExternalIssueRequestDataRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkExternalIssueRequestDataRelationships:
        """Test LinkExternalIssueRequestDataRelationships
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinkExternalIssueRequestDataRelationships`
        """
        model = LinkExternalIssueRequestDataRelationships()
        if include_optional:
            return LinkExternalIssueRequestDataRelationships(
                resource = bugcrowd_client.models.submission_nullable.SubmissionNullable(
                    data = bugcrowd_client.models.submission_nullable_data.SubmissionNullable_data(
                        id = '', 
                        type = 'submission', ), ),
                integration = bugcrowd_client.models.link_external_issue_request_data_relationships_integration.LinkExternalIssueRequest_data_relationships_integration(
                    data = bugcrowd_client.models.link_external_issue_request_data_relationships_integration_data.LinkExternalIssueRequest_data_relationships_integration_data(
                        type = 'jira_integration', 
                        id = '', ), )
            )
        else:
            return LinkExternalIssueRequestDataRelationships(
                resource = bugcrowd_client.models.submission_nullable.SubmissionNullable(
                    data = bugcrowd_client.models.submission_nullable_data.SubmissionNullable_data(
                        id = '', 
                        type = 'submission', ), ),
                integration = bugcrowd_client.models.link_external_issue_request_data_relationships_integration.LinkExternalIssueRequest_data_relationships_integration(
                    data = bugcrowd_client.models.link_external_issue_request_data_relationships_integration_data.LinkExternalIssueRequest_data_relationships_integration_data(
                        type = 'jira_integration', 
                        id = '', ), ),
        )
        """

    def testLinkExternalIssueRequestDataRelationships(self):
        """Test LinkExternalIssueRequestDataRelationships"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()