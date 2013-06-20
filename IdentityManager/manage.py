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
The manager of “Identity Manager”
=================================
'''

from flask.ext.script import Manager, Server
from IdentityManager import app
from IdentityManager.load_initial_data import LoadData
from IdentityManager.test_db_connection import TestConnection
from IdentityManager.dump_config import DumpConf

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    port=8001,
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
)

# Add data loading
manager.add_command('load_demo_data', LoadData())

# Add test db connection
manager.add_command("testdb", TestConnection())

# Add dump configuration
manager.add_command("dumpconfig", DumpConf())


def main():
    '''Convenience function to run the manager'''
    manager.run()


if __name__ == "__main__":
    main()
