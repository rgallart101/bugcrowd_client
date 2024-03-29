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

from bugcrowd_client.api.submission_resource_api import SubmissionResourceApi


class TestSubmissionResourceApi(unittest.TestCase):
    """SubmissionResourceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SubmissionResourceApi()

    def tearDown(self) -> None:
        pass

    def test_create_submission(self) -> None:
        """Test case for create_submission

        Create submission
        """
        pass

    def test_get_submission(self) -> None:
        """Test case for get_submission

        Fetch submission
        """
        pass

    def test_list_submissions(self) -> None:
        """Test case for list_submissions

        Index submissions
        """
        pass

    def test_update_submission(self) -> None:
        """Test case for update_submission

        Update submission
        """
        pass


if __name__ == '__main__':
    unittest.main()
