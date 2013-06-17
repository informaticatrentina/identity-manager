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

"""
Local Settings Template
=======================

This file is not loaded by the application by default.

This file contains all the relevant settings for local configuration,
especially the sensible ones (e.g. passwords), to be copied and changed by the
configuration manager and loaded using the ``IM_SETTINGS`` environment
variable.
"""

# Debug: set False in production!
DEBUG = True

# MongoDB
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'USERNAME'
MONGO_PASSWORD = 'PASSWORD'
MONGO_DBNAME = 'DATABASE'

# let's not forget the API entry point as domain.example.com:port
SERVER_NAME = 'URL'

# api version
API_VERSION = 'v1'

# Logs
LOG_FILE = 'PATH'
