# Copyright (c) 2023 Ansible, Inc.
# All Rights Reserved.

from django.urls import re_path

import awx.api.views.state as state


urls = [
    re_path(r'^$', state.StateList.as_view(), name='state_list'),
    re_path(r'^(?P<pk>[0-9]+)/$', state.StateView.as_view(), name='state_detail'),
]

__all__ = ['urls']
