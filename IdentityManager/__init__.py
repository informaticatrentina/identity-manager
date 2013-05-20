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

from flask import Flask

app = Flask(__name__)
app.config.from_object('IdentityManager.local_settings')


def register_blueprints(application):
    '''Register blueprints for application'''
    # Prevents circular imports
    from IdentityManager.Users import users
    application.register_blueprint(users)

register_blueprints(app)


if __name__ == '__main__':
    app.run()
