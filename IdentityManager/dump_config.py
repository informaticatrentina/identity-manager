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
Convenience Module for dumping configuration
'''

from flask.ext.script import Command

from IdentityManager import app


class DumpConf(Command):
    """Dump configuration"""

    def run(self):
        """Dump pair of config key/values"""
        key_list = app.config.keys()
        key_list.sort()
        for i in key_list:
            print "%s: %s" % (i, app.config[i])
