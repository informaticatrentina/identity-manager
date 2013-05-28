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
Convenience Module for loading initial data
'''

from os import path
from json import load

from flask.ext.script import Command, Option

from IdentityManager import app


class LoadData(Command):
    """Import demo data for contest and grant"""

    option_list = (
        Option('--from-file', '-f', dest='data_file',
               help='Load data from DATA_FILE instead of default'),
    )

    def run(self, data_file=None):
        """Run the loading"""

        apps = app.data.driver.db['apps']

        if not data_file:
            data_file = path.join(path.dirname(path.abspath(__file__)),
                                  'demo', 'data', 'contestandgrants.json')

        data_json = load(open(data_file))

        # TODO: with direct insertion there is no check for uniqueness
        ret = apps.insert(data_json)
        print "data loaded as %s" % ret
