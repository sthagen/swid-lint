#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Visit folder tree with SWID documents, validate the latter, and generate reports."""
import sys

import swid_lint.lint as swid_lint


def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    swid_lint.main(argv)
