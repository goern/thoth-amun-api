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

"""Implementation of API v1."""

import logging

from thoth.common import OpenShift
from thoth.common.exceptions import NotFoundException

from .configuration import Configuration

_LOGGER = logging.getLogger('amun.api_v1')
_OPENSHIFT = OpenShift()
_PAGET_SIZE = 100


def get_inspect_log(inspection_id: str):
    parameters = {'inspection_id': inspection_id}
    try:
        log = _OPENSHIFT.get_pod_log(inspection_id, Configuration.AMUN_INSPECTION_NAMESPACE)
    except NotFoundException:
        return {
            'error': 'The given inspection id was not found',
            'parameters': inspection_id
        }, 404

    return {
        'log': log,
        'parameters': parameters
    }, 200


def get_inspect_status(inspection_id: str):
    parameters = {'inspection_id': inspection_id}

    try:
        status = _OPENSHIFT.get_pod_status_report(inspection_id, Configuration.AMUN_INSPECTION_NAMESPACE)
    except NotFoundException:
        return {
            'error': 'The given inspection id was not found',
            'parameters': parameters
        }, 404

    return {
        'status': status,
        'parameters': parameters
    }, 200


def list_inspect(page: int = None):
    # TODO: implement listing based on label
    return {}, 500


def post_inspect(*args, **kwargs):
    # TODO: implement
    return {}, 202
