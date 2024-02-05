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

from bugcrowd_client.models.program_not_nullable_data import ProgramNotNullableData

class TestProgramNotNullableData(unittest.TestCase):
    """ProgramNotNullableData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProgramNotNullableData:
        """Test ProgramNotNullableData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProgramNotNullableData`
        """
        model = ProgramNotNullableData()
        if include_optional:
            return ProgramNotNullableData(
                id = '',
                type = 'program'
            )
        else:
            return ProgramNotNullableData(
                id = '',
                type = 'program',
        )
        """

    def testProgramNotNullableData(self):
        """Test ProgramNotNullableData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
