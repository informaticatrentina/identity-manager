# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 
# Author: Santosh Singh <santosh@incaendo.com>
#
# This file is part of the identity manager project.
#
#
###############################################################################

import os, sys
PROJECT_DIR = '/home/santosh/ve/identity-info'
activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from flask.ext.mongokit import Connection
from IdentityManager import current_app as app
from passlib.hash import bcrypt

connection = Connection(app.config['MONGO_HOST'],
                        app.config['MONGO_PORT'])

db = connection[app.config['MONGO_DBNAME']]

if app.config['MONGO_USERNAME'] and app.config['MONGO_PASSWORD']:
    db.authenticate(
        app.config['MONGO_USERNAME'],
        app.config['MONGO_PASSWORD'])
        
def encrypt_all_password():
    res = db.users.find()
    if res.count():
        entries = res[:]
        for entry in entries:
            if entry['password'] != '! we use the civiclinks password':
                newpassword = bcrypt.encrypt(entry['password'], rounds=8)
                db.users.update({'_id': entry['_id']}, {'$set': {'password':newpassword}})