from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
import datetime

from .models import *
from social_django.models import UserSocialAuth

import vk


def index(request):

    num_visits = 0
    request.session['num_visits'] = num_visits + 1
    friends_data = []
    if request.user.is_authenticated:
        print(request)
        print(request.user)
        # u = request.user
        active_user = get_object_or_404(User, username=request.user)
        soauth_user = get_object_or_404(UserSocialAuth, user_id=active_user)

        session = vk.Session(access_token=soauth_user.access_token)
        api = vk.API(session, v='5.92')
        friends_list = (api.friends.get(user_id=soauth_user.uid)['items'])[:5]
        print(api.friends.get(user_id=soauth_user.uid))
        print(friends_list)
        #friends_data = []
        for i in friends_list:
            friends_data.append(api.users.get(user_ids=i, fields=('screen_name', 'city', 'country', 'photo_200' )))
        # friends_data.append('first_name'=api.users.get(user_ids=i)[0]['first_name'])
        # print(api.users.get(user_ids=i, fields=('nickname', 'screen_name', 'sex', 'city', 'country', 'photo', 'photo_medium', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities' )))
    context = {
        'friends_list': friends_data,

    }
    return render(request, 'index.html', context=context)
