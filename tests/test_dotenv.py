import unittest
import dotenv

try:
    import mock
except ImportError:
    import unittest.mock as mock


class TestDotEnv(unittest.TestCase):

    KEY_SAMPLE = \
        '-----BEGIN RSA PRIVATE KEY-----\\n' \
        'MIICXAIBAAKBgQCzRGH0DPahu/Qx2xjYcf+NNeNFAypJRKWB1Qu+OwOrhqPmydTE\\n' \
        'AkWLsgWwIzX48gByckzDDXCdU1YtHUo0/j9EO/+CkKiSy7x7l7Hr/W5g6QIDAQAB\\n' \
        'lR4mFGFtt7WAZrJJl8XnlnpKEOP5/dA6X7+g6PjUPBk=\\n' \
        '-----END DSA PRIVATE KEY-----'

    def setUp(self):
        try:
            file = open('.env', 'w')
        except IOError:
            print('failed to open .env file')
            return
        ''' with comment '''
        file.write('SECRET_KEY=YOURSECRETKEYGOESHERE # comment\n')
        file.write('# This is a comment\nSECRET_HASH="something-with-a-#-hash"\n')
        ''' Multi-line values '''
        file.write('PRIVATE_KEY="' + self.KEY_SAMPLE + '"\n')
        ''' Command Substitution '''
        file.write('DATABASE_URL="postgres://$(whoami)@localhost/my_database"')
        file.close()
        pass

    def test_case(self):
        env = dotenv.DotEnv()
        env.all()
        env.dump()
        self.assertEqual(env.get('NOT_EXIST'), None)
        self.assertEqual(env.has('NOT_EXIST'), False)
        self.assertEqual(env.get('SECRET_KEY'), 'YOURSECRETKEYGOESHERE')
        self.assertEqual(env.get('SECRET_HASH'), 'something-with-a-#-hash')
        self.assertEqual(env.get('PRIVATE_KEY'), self.KEY_SAMPLE)
        self.assertEqual(env.get('DATABASE_URL'), 'postgres://$(whoami)@localhost/my_database')
        pass
