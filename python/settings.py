import datetime
import os
import socket

"""
This file contains global setting for the project
and oher utility functions
"""

# global settings for the project
pwd = os.path.dirname(os.path.abspath(__file__))
host = socket.gethostname()

settings = {
    # Paths
    'project_directory': pwd,
    'italy': os.path.abspath(os.path.join(pwd, '../images/photography/italy/')),
    'france': os.path.abspath(os.path.join(pwd, '../images/photography/france/')),
    'usa': os.path.abspath(os.path.join(pwd, '../images/photography/usa/')),
    # Project settings
    'today': datetime.date.today(),
    'author': 'Benjamin Vatter',
    'dependencies': [
        'pandas', 'numpy', 'scipy', 'seaborn', 'matplotlib', 'sklearn',
        'tqdm', 'numba', 'numexpr', 'bottleneck'
    ],
}
