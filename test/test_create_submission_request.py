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

from bugcrowd_client.models.create_submission_request import CreateSubmissionRequest

class TestCreateSubmissionRequest(unittest.TestCase):
    """CreateSubmissionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSubmissionRequest:
        """Test CreateSubmissionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSubmissionRequest`
        """
        model = CreateSubmissionRequest()
        if include_optional:
            return CreateSubmissionRequest(
                data = bugcrowd_client.models.create_submission_request_data.CreateSubmissionRequest_data(
                    type = 'submission', 
                    attributes = bugcrowd_client.models.create_submission_request_data_attributes.CreateSubmissionRequest_data_attributes(
                        bug_url = '', 
                        custom_fields = {"custom_field_label":"custom_value"}, 
                        description = '', 
                        extra_info = '', 
                        http_request = '', 
                        researcher_email = '', 
                        severity = 2, 
                        state = 'new', 
                        submitted_at = '2018-11-13T20:20:39Z', 
                        title = '', 
                        cvss_string = 'CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L', 
                        vrt_id = 'cross_site_scripting_xss', ), 
                    relationships = bugcrowd_client.models.create_submission_request_data_relationships.CreateSubmissionRequest_data_relationships(
                        program = bugcrowd_client.models.program_not_nullable.ProgramNotNullable(
                            data = bugcrowd_client.models.program_not_nullable_data.ProgramNotNullable_data(
                                id = '', 
                                type = 'program', ), ), 
                        target = bugcrowd_client.models.target_not_nullable.TargetNotNullable(
                            data = bugcrowd_client.models.target_not_nullable_data.TargetNotNullable_data(
                                id = '', 
                                type = 'target', ), ), ), )
            )
        else:
            return CreateSubmissionRequest(
                data = bugcrowd_client.models.create_submission_request_data.CreateSubmissionRequest_data(
                    type = 'submission', 
                    attributes = bugcrowd_client.models.create_submission_request_data_attributes.CreateSubmissionRequest_data_attributes(
                        bug_url = '', 
                        custom_fields = {"custom_field_label":"custom_value"}, 
                        description = '', 
                        extra_info = '', 
                        http_request = '', 
                        researcher_email = '', 
                        severity = 2, 
                        state = 'new', 
                        submitted_at = '2018-11-13T20:20:39Z', 
                        title = '', 
                        cvss_string = 'CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L', 
                        vrt_id = 'cross_site_scripting_xss', ), 
                    relationships = bugcrowd_client.models.create_submission_request_data_relationships.CreateSubmissionRequest_data_relationships(
                        program = bugcrowd_client.models.program_not_nullable.ProgramNotNullable(
                            data = bugcrowd_client.models.program_not_nullable_data.ProgramNotNullable_data(
                                id = '', 
                                type = 'program', ), ), 
                        target = bugcrowd_client.models.target_not_nullable.TargetNotNullable(
                            data = bugcrowd_client.models.target_not_nullable_data.TargetNotNullable_data(
                                id = '', 
                                type = 'target', ), ), ), ),
        )
        """

    def testCreateSubmissionRequest(self):
        """Test CreateSubmissionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
