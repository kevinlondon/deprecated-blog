from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.contrib.auth.models import User

from blog.models import Post
