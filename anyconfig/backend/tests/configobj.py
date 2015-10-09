#
# Copyright (C) 2013 - 2015 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
# pylint: disable=missing-docstring
from __future__ import absolute_import

import anyconfig.backend.configobj as TT
import anyconfig.backend.tests.ini


CNF_0_S = """\
# This is the 'initial_comment'
# Which may be several lines
keyword1 = value1
'keyword 2' = 'value 2'

[ "section 1" ]
# This comment goes with keyword 3
keyword 3 = value 3
'keyword 4' = value4, value 5, 'value 6'

    [[ sub-section ]]    # an inline comment
    # sub-section is inside "section 1"
    'keyword 5' = 'value 7'
    'keyword 6' = '''A multiline value,
that spans more than one line :-)
The line breaks are included in the value.'''

        [[[ sub-sub-section ]]]
        # sub-sub-section is *in* 'sub-section'
        # which is in 'section 1'
        'keyword 7' = 'value 8'

[section 2]    # an inline comment
keyword8 = "value 9"
keyword9 = value10     # an inline comment
# The 'final_comment'
# Which also may be several lines
"""

_ML_0 = """A multiline value,
that spans more than one line :-)
The line breaks are included in the value."""

CNF_0 = {'keyword 2': 'value 2',
         'keyword1': 'value1',
         'section 1': {'keyword 3': 'value 3',
                       'keyword 4': ['value4', 'value 5', 'value 6'],
                       'sub-section': {'keyword 5': 'value 7',
                                       'keyword 6': _ML_0,
                                       'sub-sub-section': {
                                           'keyword 7': 'value 8'}}},
         'section 2': {'keyword8': 'value 9', 'keyword9': 'value10'}}


class Test10(anyconfig.backend.tests.ini.Test10):

    cnf = CNF_0
    cnf_s = CNF_0_S
    load_options = dict(raise_errors=True)
    dump_options = dict(indent_type="  ")

    def setUp(self):
        self.psr = TT.Parser()


class Test20(anyconfig.backend.tests.ini.Test20):

    cnf = CNF_0
    cnf_s = CNF_0_S
    cnf_fn = "conf0.ini"

    def setUp(self):
        super(Test20, self).setUp()
        self.psr = TT.Parser()

# vim:sw=4:ts=4:et:
