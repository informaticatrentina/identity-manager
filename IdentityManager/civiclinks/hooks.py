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
This module contains the code for the eve hooks
===============================================

'''


import requests

from datetime import datetime

from eve.utils import parse_request

# TODO: maybe put the urls in a config file?
auth_url = 'https://www.civiclinks.it/it/l/users/'
det_url = 'https://www.civiclinks.it/it/l/s/get_user_details/'


# TODO: investigate a little bit more the following line ;-)
from flask import current_app as app

auth = None
verify = True

# # If you are using the testing serve you may need an additional auth
#
# from requests.auth import HTTPBasicAuth
# auth = HTTPBasicAuth(username, password)
# verify = False  # do not verifiy ssl, it is fake!


def check_for_users_on_cl(documents):
    '''
    - search the user on civiclinks
    - if found returns it
      and if it is not already added add it to the identity manager db

    TODO: should we update also the user data if they are changed?:
    - First Name
    - Last Name
    - email?

    TODO: what if the user change the email?  This is a remote case,
    currently there is no user interface that allows this on civiclinks.

    TODO: hanlde network errors
    '''

    app.logger.info('Starting to check for the user on civiclinks')

    up_req = parse_request('users')
    payload = {'where': up_req.where}

    ds_req = requests.get(auth_url, params=payload, verify=False, auth=auth)

    data = ds_req.json()
    if 'user_key' in data.keys():
        user_key = str(data['user_key'])
        det_req = requests.get(det_url + user_key + '/', params=payload,
                               verify=verify, auth=auth)
        # here we can create the user and return it verify it in
        # production
        data = det_req.json()
        res = app.data.driver.db['users'].find({'email': data['email']})
        if not res.count():
            now = datetime.now()
            # INFO: remember that the insert do not perfom any schema
            # validation
            res2 = app.data.driver.db['users'].insert({
                'updated': now,
                'created': now,
                'email': data['email'],
                'firstname': data['first_name'],
                'lastname': data['last_name'],
                'password': '! we use the civiclinks password',
            })
            app.logger.info('Add to the user db: %s' % data['email'])
            rdata = app.data.driver.db['users'].find_one(res2)
        else:
            rdata = res.next()
            app.logger.info('User already migrated: %s' % rdata['email'])
        # Remove the password manually, TODO: use the Eve filter
        del rdata['password']
        documents.append(rdata)
    else:
        # We do not have any matching document
        pass
