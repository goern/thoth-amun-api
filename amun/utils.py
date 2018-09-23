#!/usr/bin/env python3
# Amun
# Copyright(C) 2018 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Utility functions for Amun API."""


def create_dockerfile(specification: dict) -> str:
    """Create a Dockerfile based on software stack specification."""
    dockerfile = "FROM " + specification['base'] + "\n\n"

    # Install native packages.
    if specification['packages']:
        dockerfile += 'RUN '
        for package in specification['packages']:
            dockerfile += package['name'] + ('-' + package['version'] if package else '')
        dockerfile += '\n'

            
    pass
