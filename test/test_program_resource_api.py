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

from bugcrowd_client.api.program_resource_api import ProgramResourceApi


class TestProgramResourceApi(unittest.TestCase):
    """ProgramResourceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProgramResourceApi()

    def tearDown(self) -> None:
        pass

    def test_get_program(self) -> None:
        """Test case for get_program

        Fetch program
        """
        pass

    def test_list_programs(self) -> None:
        """Test case for list_programs

        Index programs
        """
        pass


if __name__ == '__main__':
    unittest.main()
