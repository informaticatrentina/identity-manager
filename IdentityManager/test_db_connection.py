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
Convenience Module for testing db connection
'''

from flask.ext.script import Command


class TestConnection(Command):
    """Test DB connection"""

    def run(self):
        """Run the test"""
        # There is no need to do some explicit command.  Due the way
        # python-eve works the exception is already raised.
        pass
