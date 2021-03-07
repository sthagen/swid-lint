#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
""""Visit folder tree with SWID documents, validate the latter, and generate reports."""
import os
import sys

import swid_lint.swid as ag


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    ag.main(argv)
 
