#
# Copyright (C) 2011 - 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
r"""YAML backends:

- pyyaml: PyYAML, http://pyyaml.org [default]
- ruamel.yaml: ruamel.yaml, https://bitbucket.org/ruamel/yaml

Changelog:

.. versionchanged:: 0.9.8

   - Split PyYaml-based and ruamel.yaml based backend modules
   - Add support of some of ruamel.yaml specific features.
"""
try:
    from . import pyyaml
    PARSERS = [pyyaml.Parser]
except ImportError:
    PARSERS = []

try:
    from . import ruamel_yaml as ryaml
    PARSERS.append(ryaml.Parser)
except ImportError:
    ryaml = False

# vim:sw=4:ts=4:et:
