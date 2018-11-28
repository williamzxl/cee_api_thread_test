import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig


class TestLogin(unittest.TestCase):
    def setUp(self):
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info()
        self.t = LoginApi()

    def test_login_success(self):
        access_token = self.t.get_access_token(self.common, self.headers)
        result = self.t.check_uname(self.common, self.headers, access_token)
        assert self.common.get('uname').split("@")[0] in result

    def test_login_fail_with_wrong_uname_right_pwd(self):
        self.common.update({'uname':self.common.get('uname') + "1"})
        access_token = self.t.get_access_token(self.common, self.headers)
        # result = self.t.check_uname(self.common, self.headers, access_token)
        assert access_token == None

    def test_login_fail_with_right_uname_wrong_pwd(self):
        self.common.update({'pwd': str(self.common.get('pwd')) + "1"})
        access_token = self.t.get_access_token(self.common, self.headers)
        # result = self.t.check_uname(self.common, self.headers, access_token)
        assert access_token == None

    def test_login_fail_with_wrong_uname_wrong_pwd(self):
        self.common.update({'uname': self.common.get('uname') + "1"})
        self.common.update({'pwd': str(self.common.get('pwd')) + "1"})
        access_token = self.t.get_access_token(self.common, self.headers)
        assert access_token == None

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()