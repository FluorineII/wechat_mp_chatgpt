from common import cache
from config import conf


class Session(object):
    @staticmethod
    def build_session_query(query, user_id):
        """
        build query with conversation history
        e.g.  [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
        :param query: query content
        :param user_id: from user id
        :return: query content with conversation
        """
        session = cache.get(Session.get_session_key(user_id))
        if not session:
            session = []
            system_prompt = conf()["character_desc"]
            system_item = {'role': 'system', 'content': system_prompt}
            session.append(system_item)
        user_item = {'role': 'user', 'content': query}
        session.append(user_item)
        return session

    @staticmethod
    def save_session(query, answer, user_id, used_tokens=0):
        max_tokens = conf()["conversation_max_tokens"]
        if not max_tokens or max_tokens > 4000:
            # default value
            max_tokens = 1000
        session = query
        if session:
            # append conversation
            gpt_item = {'role': 'assistant', 'content': answer}
            session.append(gpt_item)

        if used_tokens > max_tokens and len(session) >= 3:
            # pop first conversation (TODO: more accurate calculation)
            session.pop(1)
            session.pop(1)
        cache.set_key(Session.get_session_key(user_id), session)

    @staticmethod
    def clear_session(user_id):
        cache.del_key(Session.get_session_key(user_id))

    @staticmethod
    def get_session_key(user_id):
        return user_id + "session"
