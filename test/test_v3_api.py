# coding: utf-8

"""
    Catalog Next API.

    This documentation describes the Catalog Next API for all versions and other miscellaneous endpoints.  # noqa: E501

    OpenAPI spec version: 1.16.3+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dcs_catalog_client
from dcs_catalog_client.api.v3_api import V3Api  # noqa: E501
from dcs_catalog_client.rest import ApiException


class TestV3Api(unittest.TestCase):
    """V3Api unit test stubs"""

    def setUp(self):
        self.api = dcs_catalog_client.api.v3_api.V3Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_catalog_search_v3(self):
        """Test case for catalog_search_v3

        Catalog v3 search  # noqa: E501
        """
        pass

    def test_catalog_subjects_pivoted_by_subject_v3(self):
        """Test case for catalog_subjects_pivoted_by_subject_v3

        Catalog v3 listing pivoted on subject by a given subject (e.g. /v3/subjects/Open_Bible_Stories.json)  # noqa: E501
        """
        pass

    def test_catalog_subjects_pivoted_search_v3(self):
        """Test case for catalog_subjects_pivoted_search_v3

        Catalog v3 search pivoted by subject/language  # noqa: E501
        """
        pass

    def test_catalog_subjects_pivoted_v3(self):
        """Test case for catalog_subjects_pivoted_v3

        Catalog v3 listing pivoted by subject/language, back-port of https://api.door43.org/v3/subjects/pivoted.json  # noqa: E501
        """
        pass

    def test_catalog_v3(self):
        """Test case for catalog_v3

        Catalog v3 listing by language, back-port of https://api.door43.org/v3/catalog.json  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
