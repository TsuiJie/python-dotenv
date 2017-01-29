import unittest
import dotenv

try:
    import mock
except ImportError:
    import unittest.mock as mock


class TestDotEnv(unittest.TestCase):

    def setUp(self):
        file = open('.env', 'w')
        file.write('TEST=ok')
        file.close()
        pass

    def test_case(self):
        env = dotenv.DotEnv()
        env.all()
        env.dump()
        env.get('TEST')
        env.has('TEST')
        pass
