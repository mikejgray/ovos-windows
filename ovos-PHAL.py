#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
from ovos_PHAL.__main__ import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("Process interrupted by user")
        sys.exit(1)
