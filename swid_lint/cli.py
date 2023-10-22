"""Visit folder tree with SWID documents, validate the latter, and generate reports."""
import sys
from typing import no_type_check

import swid_lint.lint as swid_lint


@no_type_check
def main(argv=None):
    """Process the job."""
    argv = sys.argv[1:] if argv is None else argv
    swid_lint.main(argv)
