# coding: utf-8

"""
    Harbor API
    These APIs provide services for manipulating Harbor project.
    OpenAPI spec version: 1.4.0
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import
import os
import sys
sys.path.append(os.environ["SWAGGER_CLIENT_PATH"])


import unittest
import testutils

from swagger_client.rest import ApiException
from swagger_client.models.configurations import Configurations 
from pprint import pprint

# Test search LDAP group

class TestLdapGroupSearch(unittest.TestCase):
    """UserGroup unit test stubs"""
    product_api = testutils.GetProductApi("admin", "Harbor12345")
    groupId = 0
    def setUp(self):
        result = self.product_api.configurations_put(configurations=Configurations(ldap_filter="", ldap_group_attribute_name="cn", ldap_group_base_dn="ou=groups,dc=example,dc=com", ldap_group_search_filter="objectclass=groupOfNames", ldap_group_search_scope=2))
        pprint(result)
        pass

    def tearDown(self):
        pass

    def testSearchLdapGroup(self):
        result = self.product_api.ldap_groups_search_get(groupname="harbor_users")
        pprint(result)
        self.assertTrue(len(result)>=1)
        pass

    def testSearchLdapGroupNotExist(self):
        with self.assertRaises(ApiException) as cm:
            result =  self.product_api.ldap_groups_search_get(groupname="not_found_group")
            pprint(result)
        self.assertEqual(404, cm.exception.status)


if __name__ == '__main__':
    unittest.main()
