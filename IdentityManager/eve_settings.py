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
Eve settings
'''

# Log file
LOG_FILE = '/tmp/identity-manager.log'

# Debug: set False in production!
DEBUG = True

# Database

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = None  # 'user'
MONGO_PASSWORD = None  # 'user'
MONGO_DBNAME = 'identitymanager'

# let's not forget the API entry point
SERVER_NAME = 'localhost:8001'

# api version
API_VERSION = 'v1'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.
users = {
    # 'title' tag used in item links.
    'item_title': 'user',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/people/<lastname>/'.
    'additional_lookup': {
        'url': '[\w]+',
        'field': 'email',
    },

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {

        'username': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 32,
            'required': False,
            'unique': True,
        },

        'firstname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 64,
        },

        'lastname': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 64,
            'required': True,
            'unique': False,
        },

        'email': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 64,
            'required': True,
            'unique': True,
        },

        'sex': {
            'type': 'list',
            'allowed': ["M", "F"],
            'required': False,
        },

        'password': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 64,
            'required': True,
            'unique': False,
        },

        'born': {
            'type': 'datetime',
            'required': False,
            'unique': False,
        },

        # This will be the web-friendly username: eg: user-name
        'slug': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 64,
            'required': False,
            'unique': True,
        },

        # A short bio
        'biography': {
            'type': 'string',
            'minlength': 0,
            'maxlength': 150,
            'required': False,
            'unique': False,
        },

        # Location
        'location': {
            'type': 'string',
            'minlength': 0,
            'maxlength': 128,
            'required': False,
            'unique': False,
        },

        'website': {
            'type': 'string',
            'minlength': 0,
            'maxlength': 256,
            'required': False,
            'unique': False,
        },

        # photo
        'photo': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': False,
            'unique': False,
        },

        'tags': {
            'type': 'list',
            'schema': {
                'type': 'string',
                'data_relation': {
                    'collection': 'tags',
                    'field': 'slug',
                },
            },
            'required': False,
            'unique': False,
        },
    },
    'datasource': {
        'projection': {
            'username': 1,
            'firstname': 1,
            'lastname': 1,
            'email': 1,
            'born': 1,
            'created': 1,
            'updated': 1,
            'slug': 1,
            'biography': 1,
            'location': 1,
            'website': 1,
            'photo': 1,
            'tags': 1,
            'sex': 1,
        },
    },
}

apps = {
    # if 'item_title' is not provided Eve will just strip the final
    # 's' from resource name, and use it as the item_title.
    'item_title': 'apps',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': {
        'name': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'description': {
            'type': 'string',
        },
        'token': {
            'type': 'string',
            'required': True,
        },
    },
}

tags = {
    'schema': {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True,
            'unique': False,
        },
        'slug': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True,
            'unique': False,
        },
        'scheme': {
            'required': False,
            'type': 'string',
            'data_relation': {
                'collection': 'schemes',
                'field': 'name',
            },
        },
        'weight': {
            'type': 'integer',
            'required': False,
            'unique': False,
        },
    }
}

schemes = {
    'schema': {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 256,
            'required': True,
            'unique': True,
        },
    },
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'users': users,
    'apps': apps,
    'tags': tags,
    'schemes': schemes,
}
