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

from bugcrowd_client.models.update_submission_request_data_attributes import UpdateSubmissionRequestDataAttributes

class TestUpdateSubmissionRequestDataAttributes(unittest.TestCase):
    """UpdateSubmissionRequestDataAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSubmissionRequestDataAttributes:
        """Test UpdateSubmissionRequestDataAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSubmissionRequestDataAttributes`
        """
        model = UpdateSubmissionRequestDataAttributes()
        if include_optional:
            return UpdateSubmissionRequestDataAttributes(
                bug_url = '',
                custom_fields = {"custom_field_label":"custom_value"},
                http_request = '',
                remediation_advice = '',
                severity = 2,
                state = 'new',
                title = '',
                vrt_id = 'cross_site_scripting_xss',
                vulnerability_references = ''
            )
        else:
            return UpdateSubmissionRequestDataAttributes(
        )
        """

    def testUpdateSubmissionRequestDataAttributes(self):
        """Test UpdateSubmissionRequestDataAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
