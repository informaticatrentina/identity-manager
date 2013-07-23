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
Test for identity manager module
'''


from nose.plugins.skip import SkipTest

from eve.tests import TestMinimal


class ExampleTest(TestMinimal):
    '''An identity manager test Class'''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def first_test(self):
        '''Human readable test name'''
        raise SkipTest('Please start writing real test!')
