from __future__ import absolute_import, division, print_function, unicode_literals

import os

from grit import Git
from grit import Project
from grit.command import Import
from grit.command import Start
from grit.command import Test

SAFE = False

HELP = """
grit clone <branch> [directory]
    Clones an existing branch of the current project.

    If the branch name is purely numeric, it's a pull request.

    If the branch name contains a :, it's a remote branch.

    If the directory name is not given, it adds a numeric suffix to the current
    directory.
"""

def clone(branch='', directory=''):
    directory = Start.clone(directory)
    base_branch = Project.settings('clone').get('base_branch', 'develop')
    if branch and branch != base_branch:
        Import.run_import(branch, cwd=directory)
    Test.run_test(directory)
