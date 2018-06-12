# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "issue.settings")
#~ from django.core.management import execute_from_command_line



from django.db import models

# Create your models here.


# coding: utf-8
from django.db import models
from django.contrib.auth.models import User



from .models import *
