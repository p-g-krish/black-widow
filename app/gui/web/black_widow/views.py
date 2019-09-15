"""
*********************************************************************************
*                                                                               *
* views.py -- Django views of black-widow.                                      *
*                                                                               *
********************** IMPORTANT BLACK-WIDOW LICENSE TERMS **********************
*                                                                               *
* This file is part of black-widow.                                             *
*                                                                               *
* black-widow is free software: you can redistribute it and/or modify           *
* it under the terms of the GNU General Public License as published by          *
* the Free Software Foundation, either version 3 of the License, or             *
* (at your option) any later version.                                           *
*                                                                               *
* black-widow is distributed in the hope that it will be useful,                *
* but WITHOUT ANY WARRANTY; without even the implied warranty of                *
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                 *
* GNU General Public License for more details.                                  *
*                                                                               *
* You should have received a copy of the GNU General Public License             *
* along with black-widow.  If not, see <http://www.gnu.org/licenses/>.          *
*                                                                               *
*********************************************************************************
"""

import os

from django.http import HttpResponseNotFound, FileResponse
from django.shortcuts import render

from app.gui.web.settings import STATICFILES_DIRS


# Create your views here.


def index(request):
    return render(request, 'index.html')


def user(request):
    return render(request, 'user.html')


def tables(request):
    return render(request, 'tables.html')


def typography(request):
    return render(request, 'typography.html')


def icons(request):
    return render(request, 'icons.html')


def notifications(request):
    return render(request, 'notifications.html')


def upgrade(request):
    return render(request, 'upgrade.html')


def static(request, path):
    """
    Manage requested static file (for non-DEBUG mode compatibility without web-server)
    :type path: str
    :type request: django.core.handlers.wsgi.WSGIRequest
    """
    for directory in STATICFILES_DIRS:
        static_file = os.path.join(directory, path)
        if os.path.isfile(static_file):
            return FileResponse(open(static_file, 'rb'), as_attachment=False)
    return HttpResponseNotFound()
