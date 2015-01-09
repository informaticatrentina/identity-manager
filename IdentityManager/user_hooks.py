# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 <ahref Foundation -- All rights reserved.
# Author: Santosh Singh <santosh@incaendo.com>
#
# This file is part of the identity manager project.
#
# This file can not be copied and/or distributed without the express
# permission of <ahref Foundation.
#
###############################################################################

'''
This module contains the code for the eve hooks
===============================================

'''


import requests

from datetime import datetime

from eve.utils import parse_request

# TODO: investigate a little bit more the following line ;-)
from flask import current_app as app

from flask import json

from passlib.hash import bcrypt

dumps = json.dumps
loads = json.loads

auth = None
verify = True

def on_fetch_user(document):
	up_req = parse_request('users')
	whereObj = loads(up_req.where)
	if 'password' in whereObj:
	    res = app.data.driver.db['users'].find({'email': whereObj['email']})
	    if res.count():
	        rdata = res.next()
	        if bcrypt.verify(whereObj['password'], rdata['password']):
	            del rdata['password']
	            document['_items'].append(rdata)
            else:
                pass
        else:
            pass

def on_insert_user_callback(items):
    item = items[0]
    if 'password' in item:
        item['password'] = bcrypt.encrypt(item['password'], rounds=8)
    else:
        pass

def on_update_user_callback(updates, original):
    if 'password' in updates:
        updates['password'] = bcrypt.encrypt(updates['password'], rounds=8)
    else:
        pass