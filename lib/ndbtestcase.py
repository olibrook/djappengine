import unittest

from google.appengine.ext import ndb, testbed


class NdbTestCase(unittest.TestCase):
    """Setup and teardown common to tests involving ndb entities"""

    @property
    def datastore_v3_stub_kwargs(self):
        return {}

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub(**self.datastore_v3_stub_kwargs)
        self.testbed.init_memcache_stub()
        self.testbed.init_modules_stub()
        self.testbed.init_taskqueue_stub('.')
        self.testbed.init_user_stub()
        self.testbed.init_modules_stub()
        self.clear_datastore()

    def tearDown(self):
        self.clear_datastore()
        self.testbed.deactivate()

    def clear_datastore(self):
        for kind_name, kind in ndb.Model._kind_map.iteritems():
            ndb.delete_multi(kind.query().fetch(keys_only=True))

    def users_login(self, email, user_id=None, is_admin=False):
        self.testbed.setup_env(
            USER_EMAIL=email,
            USER_ID=user_id or '98211821748316341', # Random ID
            USER_IS_ADMIN=str(int(is_admin)),
            AUTH_DOMAIN='testbed',
            overwrite=True,
        )


if __name__ == '__main__':
    unittest.main()
