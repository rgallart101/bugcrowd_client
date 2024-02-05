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

from bugcrowd_client.models.event_data_submission_updated_changes_severity import EventDataSubmissionUpdatedChangesSeverity

class TestEventDataSubmissionUpdatedChangesSeverity(unittest.TestCase):
    """EventDataSubmissionUpdatedChangesSeverity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventDataSubmissionUpdatedChangesSeverity:
        """Test EventDataSubmissionUpdatedChangesSeverity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventDataSubmissionUpdatedChangesSeverity`
        """
        model = EventDataSubmissionUpdatedChangesSeverity()
        if include_optional:
            return EventDataSubmissionUpdatedChangesSeverity(
                var_from = 1,
                to = 1
            )
        else:
            return EventDataSubmissionUpdatedChangesSeverity(
        )
        """

    def testEventDataSubmissionUpdatedChangesSeverity(self):
        """Test EventDataSubmissionUpdatedChangesSeverity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
