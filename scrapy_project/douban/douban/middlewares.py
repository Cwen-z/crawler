import random
from settings import USER_AGENTS


class RandomUserAgent(object):

    def process_request(self, request, spider):
        agent = random.choice(USER_AGENTS)
        request.headers.setdefault("User_Agent", agent)
