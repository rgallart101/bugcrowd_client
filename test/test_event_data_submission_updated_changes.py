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

from bugcrowd_client.models.event_data_submission_updated_changes import EventDataSubmissionUpdatedChanges

class TestEventDataSubmissionUpdatedChanges(unittest.TestCase):
    """EventDataSubmissionUpdatedChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventDataSubmissionUpdatedChanges:
        """Test EventDataSubmissionUpdatedChanges
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventDataSubmissionUpdatedChanges`
        """
        model = EventDataSubmissionUpdatedChanges()
        if include_optional:
            return EventDataSubmissionUpdatedChanges(
                custom_fields = {
                    'key' : bugcrowd_client.models.event_data_submission_updated_changes_custom_fields_value.EventDataSubmissionUpdated_changes_custom_fields_value(
                        from = '', 
                        to = '', )
                    },
                cvss_vector_id = bugcrowd_client.models.event_data_submission_updated_changes_cvss_vector_id.EventDataSubmissionUpdated_changes_cvss_vector_id(
                    from = '', 
                    to = '', ),
                duplicate = bugcrowd_client.models.event_data_submission_updated_changes_duplicate.EventDataSubmissionUpdated_changes_duplicate(
                    from = True, 
                    to = True, ),
                duplicate_of_id = bugcrowd_client.models.event_data_submission_updated_changes_cvss_vector_id.EventDataSubmissionUpdated_changes_cvss_vector_id(
                    from = '', 
                    to = '', ),
                encrypted_bug_url = bugcrowd_client.models.event_data_submission_updated_changes_encrypted_bug_url.EventDataSubmissionUpdated_changes_encrypted_bug_url(
                    from = '', 
                    to = '', ),
                encrypted_description = bugcrowd_client.models.event_data_submission_updated_changes_encrypted_bug_url.EventDataSubmissionUpdated_changes_encrypted_bug_url(
                    from = '', 
                    to = '', ),
                encrypted_extra_info = bugcrowd_client.models.event_data_submission_updated_changes_encrypted_bug_url.EventDataSubmissionUpdated_changes_encrypted_bug_url(
                    from = '', 
                    to = '', ),
                encrypted_http_request = bugcrowd_client.models.event_data_submission_updated_changes_encrypted_bug_url.EventDataSubmissionUpdated_changes_encrypted_bug_url(
                    from = '', 
                    to = '', ),
                remediation_advice = bugcrowd_client.models.event_data_submission_updated_changes_custom_fields_value.EventDataSubmissionUpdated_changes_custom_fields_value(
                    from = '', 
                    to = '', ),
                remediation_advice_edited = bugcrowd_client.models.event_data_submission_updated_changes_duplicate.EventDataSubmissionUpdated_changes_duplicate(
                    from = True, 
                    to = True, ),
                target_id = bugcrowd_client.models.event_data_submission_updated_changes_cvss_vector_id.EventDataSubmissionUpdated_changes_cvss_vector_id(
                    from = '', 
                    to = '', ),
                title = bugcrowd_client.models.event_data_submission_updated_changes_title.EventDataSubmissionUpdated_changes_title(
                    from = '', 
                    to = '', ),
                vrt_id = bugcrowd_client.models.event_data_submission_updated_changes_custom_fields_value.EventDataSubmissionUpdated_changes_custom_fields_value(
                    from = '', 
                    to = '', ),
                vrt_version = bugcrowd_client.models.event_data_submission_updated_changes_title.EventDataSubmissionUpdated_changes_title(
                    from = '', 
                    to = '', ),
                vulnerability_references = bugcrowd_client.models.event_data_submission_updated_changes_custom_fields_value.EventDataSubmissionUpdated_changes_custom_fields_value(
                    from = '', 
                    to = '', ),
                vulnerability_refs_edited = bugcrowd_client.models.event_data_submission_updated_changes_duplicate.EventDataSubmissionUpdated_changes_duplicate(
                    from = True, 
                    to = True, ),
                state = bugcrowd_client.models.event_data_submission_updated_changes_custom_fields_value.EventDataSubmissionUpdated_changes_custom_fields_value(
                    from = '', 
                    to = '', ),
                severity = bugcrowd_client.models.event_data_submission_updated_changes_severity.EventDataSubmissionUpdated_changes_severity(
                    from = 1, 
                    to = 1, )
            )
        else:
            return EventDataSubmissionUpdatedChanges(
        )
        """

    def testEventDataSubmissionUpdatedChanges(self):
        """Test EventDataSubmissionUpdatedChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
