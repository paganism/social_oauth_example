from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from social_django.models import UserSocialAuth

import vk

VK_API_VERSION = '5.92'

def index(request):
    friends_data = []
    if request.user.is_authenticated:
        active_user = get_object_or_404(User, username=request.user)
        soauth_user = get_object_or_404(UserSocialAuth, user_id=active_user)
        session = vk.Session(access_token=soauth_user.access_token)
        api = vk.API(session, v=VK_API_VERSION)
        friends_list = (api.friends.get(user_id=soauth_user.uid)['items'])[:5]
        for i in friends_list:
            friends_data.append(api.users.get(user_ids=i, fields=('screen_name', 'city', 'country', 'photo_200')))
    context = {
        'friends_list': friends_data,

    }
    return render(request, 'index.html', context=context)
