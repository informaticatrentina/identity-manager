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
Small utility to show the users
===============================

'''


from flask.ext.script import Command

from IdentityManager import app


class ShowUsers(Command):
    '''
    Show the users in the identity manager
    '''

    def run(self, data_file=None):
        """Run the ShowUsers"""
        users = app.data.driver.db['users']
        for user in users.find():
            print user
