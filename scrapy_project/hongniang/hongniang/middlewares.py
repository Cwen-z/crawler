# -*- coding: utf-8 -*-
import random
from settings import user_agent_list


class UserAgentChoice(object):
    def process_request(self, request, spider):
        ua = random.choice(user_agent_list)
        request.headers.setdefault("User-Agent", ua)
