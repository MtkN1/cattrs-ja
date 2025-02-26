#!/bin/bash

uv run sphinx-build -M html ./downloads/cattrs/docs ./build -D language=ja -D locale_dirs=../../../locales "$@"
