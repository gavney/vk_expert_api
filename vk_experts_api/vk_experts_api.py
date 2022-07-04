import requests


class Expert:
    base_url = "https://api.vk.com/method/"
    category = None

    def __init__(self, token, category, api_version='5.92'):
        """
            :param token: access_token
            :type token: str

            :param category: Идентификатор тематики
            :type token: int

            :param api_version: версия API
            :type token: str
        """
        self.token = token
        self.category = category

        self.api_version = api_version

    def getCustom(self, count=50, start_from=1, feed_id=None):
        """ Метод получения тематической ленты

            :param count: Количество постов (необязательный)
            :type count: int

            :param start_from: Идентификатор, необходимый для
             получения следующей страницы результатов (необязательный)
            :type start_from: int

            :param feed_id: Идентификатор тематики
            :type feed_id: int
        """

        if not feed_id:
            feed_id = self.category

        values = {"count": count, "start_from": start_from,
                  "feed_id": "discover_category/" + str(feed_id),
                  "v": self.api_version, "access_token": self.token}

        return makeRequest(url=self.base_url + "newsfeed.getCustom", values=values)

    def setPostVote(self, owner_id, post_id, new_vote):
        """ Метод выставления голоса посту

            :param owner_id: Идентификатор владельца поста
            :type owner_id: int

            :param post_id: Идентификатор поста
            :type post_id: int

            :param new_vote: Новый голос
             1 = положительный голос,
             0 = нейтральный голос,
            -1 = отрицательный голос
            :type new_vote: int
        """

        values = {"owner_id": owner_id, "post_id": post_id,
                  "new_vote": new_vote, "v": self.api_version,
                  "access_token": self.token}

        return makeRequest(self.base_url + "newsfeed.setPostVote", values=values)

    def setPostTopic(self, owner_id, post_id, topic_id):
        """ Метод выставления тематики поста

            :param owner_id: Идентификатор владельца поста
            :type owner_id: int

            :param post_id: Идентификатор поста
            :type post_id: int

            :param topic_id: Идентификатор тематики
            :type topic_id: int
        """

        values = {"owner_id": owner_id, "post_id": post_id,
                  "topic_id": topic_id, "v": self.api_version,
                  "access_token": self.token}

        return makeRequest(self.base_url + "newsfeed.setPostVote", values=values)

    def doubtCategory(self, owner_id, post_id):
        """ Метод жалобы на неправильную тематику поста

            :param owner_id: Идентификатор владельца поста
            :type owner_id: int

            :param post_id: Идентификатор поста
            :type post_id: int
        """

        values = {"owner_id": owner_id, "post_id": post_id,
                  "v": self.api_version, "access_token": self.token}

        return makeRequest(self.base_url + "newsfeed.setPostVote", values=values)

    def getExpertCard(self):
        """ Метод жалобы на неправильную тематику поста """

        values = {"v": self.api_version, "access_token": self.token}

        return makeRequest(self.base_url + "newsfeed.getExpertCard", values=values)


class ApiError(Exception):
    pass


def makeRequest(url, values):
    response = requests.post(
        url=url,
        params=values
    ).json()

    if "error" in response:
        raise ApiError(response["error"].get("error_msg"))

    return response["response"]
