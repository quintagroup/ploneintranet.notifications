# -*- coding: utf-8 -*-

from plone.api.user import create as create_user
from ploneintranet.notifications.channel import AllChannel
from ploneintranet.notifications.message import create_message
from ploneintranet.notifications.msg_classes import fake_adapter
from ploneintranet.notifications.testing import \
    PLONEINTRANET_NOTIFICATIONS_INTEGRATION_TESTING
import unittest2 as unittest


class TestMessageLifecycle(unittest.TestCase):

    layer = PLONEINTRANET_NOTIFICATIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_create_msgs_mark_as_read_delete(self):
        predicate = 'GLOBAL_NOTICE'

        users = ['test0', 'test1', 'test2', 'test3', 'test4']
        users = map(lambda user: create_user(
            email=user+'@example.com',
            username=user).getUser(), users)

        # Step 1, something creates a bunch of messages
        actor = dict(fullname='John Doe', userid='johndoe',
                     email='join@test.com')
        obj = {'id': self.portal.id,
               'url': self.portal.absolute_url(relative=True),
               'title': 'I deleted the front page'}
        msg = create_message([actor], predicate, obj)

        # This should be an adapter
        msg_class_handler = fake_adapter(predicate)
        msg_class_handler.add(msg)

        # Step 2, test1 sees his message
        channel = AllChannel(users[0])
        first_msg = channel.get_all_messages()[0]
        first_msg.mark_as_read()

        # Step 3, the regular clean up tasks from somewhere
        # cleans up queues

        handler = fake_adapter(predicate)
        handler.cleanup()

        # Step 4, somebody else reads his messages

        channel = AllChannel(users[1])
        first_msg = channel.get_all_messages()[0]
        first_msg.mark_as_read()

        # Final result

        self.assertEqual(0, len(AllChannel(users[0]).get_unread_messages(
            keep_unread=True)))
        self.assertEqual(0, len(AllChannel(users[1]).get_unread_messages(
            keep_unread=True)))
        self.assertEqual(1, len(AllChannel(users[1]).get_all_messages()))
        self.assertEqual(1, len(AllChannel(users[2]).get_unread_messages(
            keep_unread=True)))
        self.assertEqual(1, len(AllChannel(users[3]).get_unread_messages(
            keep_unread=True)))
        self.assertEqual(1, len(AllChannel(users[4]).get_unread_messages(
            keep_unread=True)))
