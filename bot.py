# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def main():
    """ Пример использования bots longpoll
        https://vk.com/dev/bots_longpoll
    """

    vk_session = vk_api.VkApi(token='6b153c5922e2003d584eb8bd85a8e9daea8dc0152fdb887baac9cf3e876215ca066f3f5f0d2f1878f82e3')

    longpoll = VkBotLongPoll(vk_session, '210930943')

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            print('Для меня от: ', end='')

            print(event.obj.from_id)

            print('Текст:', event.obj.text)
            print()

        elif event.type == VkBotEventType.MESSAGE_REPLY:
            print('Новое сообщение:')

            print('От меня для: ', end='')

            print(event.obj.peer_id)

            print('Текст:', event.obj.text)
            print()

        elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print('Печатает ', end='')

            print(event.obj.from_id, end=' ')

            print('для ', end='')

            print(event.obj.to_id)
            print()

        elif event.type == VkBotEventType.GROUP_JOIN:
            print(event.obj.user_id, end=' ')

            print('Вступил в группу!')
            print()

        elif event.type == VkBotEventType.GROUP_LEAVE:
            print(event.obj.user_id, end=' ')

            print('Покинул группу!')
            print()

        else:
            print(event.type)
            print()


if __name__ == '__main__':
    main()
