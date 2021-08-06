# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.base.utils.models.fields import get_default_field_value


def shared_gstatus_path(field, value):
    return '/opt/datadog-agent/embedded/sbin/gstatus'


def shared_service(field, value):
    return get_default_field_value(field, value)


def instance_check_generic_tags(field, value):
    return False


def instance_disable_generic_tags(field, value):
    return False


def instance_empty_default_hostname(field, value):
    return False


def instance_min_collection_interval(field, value):
    return 60


def instance_service(field, value):
    return get_default_field_value(field, value)


def instance_tags(field, value):
    return get_default_field_value(field, value)


def instance_use_sudo(field, value):
    return True
