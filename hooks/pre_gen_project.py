#! /usr/bin/env python
try:
    from pip import main
except ImportError:
    from pip._internal.main import main

try:
    import poetry
except ImportError:
    main(["install", "poetry"])
