#!/bin/bash

uv run sphinx-intl -c ./downloads/cattrs/docs/conf.py update -p ./build/gettext -l ja -w 0 -j 1
