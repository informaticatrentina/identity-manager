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
Identity Manager Project
========================

TODO: replace this line with proper project description.
'''


import pkg_resources
pkg_resources.declare_namespace(__name__)


from os import environ, path

from eve import Eve
from eve.auth import TokenAuth

from IdentityManager import eve_settings


# TODO: move to a proper file
class MyBasicAuth(TokenAuth):
    def check_auth(self, token, allowed_roles):
        apps = app.data.driver.db['apps']
        return apps.find_one({'token': token})


# Load custom settings for eve
eve_settings_module = path.abspath(eve_settings.__file__)
eve_settings_file = eve_settings_module

# We can use only .py files!
if (
    eve_settings_module.endswith('.pyc') and
    path.exists(eve_settings_file[:-1])
):
    eve_settings_file = eve_settings_module[:-1]

# IM_SETTINGS become EVE_SETTINGS
if 'IM_SETTINGS' in environ:
    environ['EVE_SETTINGS'] = environ['IM_SETTINGS']
    del environ['IM_SETTINGS']

app = Eve(auth=MyBasicAuth, settings=eve_settings_file)


if __name__ == '__main__':
    app.run()
