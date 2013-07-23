# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 <ahref Foundation -- All rights reserved.
# Author: Daniele Pizzolli <daniele@ahref.eu>
#
# This file is part of the identity manager project.
#
# This file can not be copied and/or distributed without the express
# permission of <ahref Foundation.
#
###############################################################################


'''
Test for the civiclinks api
'''


from json import loads

from IdentityManager import app
from eve.tests import TestMinimal


class CivicAuth(TestMinimal):
    """Test Civic Auth"""

    def setUp(self):
        '''Prepare the test fixture'''

        from pkg_resources import resource_filename
        test_config = resource_filename('IdentityManager', 'eve_settings.py')

        self.settings_file = test_config
        self.app = app

        self.test_client = self.app.test_client()
        self.setupDB()
        # Same as the demo user
        self.valid_auth = [
            ('Authorization',
             'Basic eWFpVDZlZXF1aTdmYWlnN2FlU2gwcGhpOWlkM2l1M0I6',)]

        # DROP users
        with self.app.app_context():
            self.app.data.driver.db.drop_collection('users')

    def tearDown(self):
        self.dropDB()

    def test_get_user_from_civic(self):
        '''
        Test getting user data from civiclinks

        This test is interactive as there is no easy way to get a
        working civiclinks instance for testing purposes.
        '''

        # NOTE: Raise error or skip testing when not interacive?
        import sys
        if not sys.stdout.isatty():
            raise(ValueError("Please run the test in an interactive console"))

        print "Please enter your civiclinks data"
        import getpass
        username = raw_input('Email: ')
        password = getpass.getpass()

        url = ('/v1/users/?where='
               '{"email": "%s",'
               '"password": "%s"}') % (username, password)

        r1 = self.test_client.get(url, headers=self.valid_auth)
        data1 = loads(r1.data)

        if not data1['_items']:
            raise(ValueError("Probably you username/password was wrong"))

        self.assertEqual('daniele@ahref.eu', data1['_items'][0]['email'])

        r2 = self.test_client.get(url, headers=self.valid_auth)
        data2 = loads(r2.data)
        self.assertEqual('daniele@ahref.eu', data2['_items'][0]['email'])

        self.maxDiff = None
        self.assertEqual(data1, data2)
