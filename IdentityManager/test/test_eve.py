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


from eve import Eve
from eve.tests import TestMinimal

from IdentityManager import eve_settings_file
from IdentityManager import MyBasicAuth


class TestTokenAuth(TestMinimal):

    def setUp(self, settings_file=eve_settings_file):
        super(TestTokenAuth, self).setUp(eve_settings_file)
        self.app = Eve(settings=eve_settings_file, auth=MyBasicAuth)
        self.test_client = self.app.test_client()
        self.valid_auth = [
            ('Authorization', 'Basic yaiT6eequi7faig7aeSh0phi9id3iu3B')]
        self.app.set_defaults()

    def test_custom_auth(self):
        self.assertEqual(type(self.app.auth), MyBasicAuth)

    def def_home_not_found(self):
        r = self.test_client.get('/')
        self.assert404(r.status_code)

    def test_restricted_v1(self):
        r = self.test_client.get('/' + self.app.config['API_VERSION'])
        self.assert301(r.status_code)
