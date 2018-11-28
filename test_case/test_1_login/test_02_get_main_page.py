import unittest
from testcase.api.login.login_all_api import LoginApi
from testcase.api.main_page.service_detail.get_service_detail import GetServiceDetail
from utils.config import NewConfig


class TestGetServicesDetail(unittest.TestCase):
    def setUp(self):
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info(devices_name="vivox6")
        self.t = LoginApi()
        self.access_token = self.t.get_access_token(self.common, self.headers)
        self.s_detail = GetServiceDetail(self.common, self.headers, self.access_token)
        self.response = self.s_detail.get_service_detail()

    def test_services_detail_shareEnabled(self):
        assert self.response.get('shareEnabled') == True

    def test_services_detail_servicePrice(self):
        assert self.response.get('servicePrice') == '2598'

    def test_services_detail_P150(self):
        assert self.response.get('serviceID') == 'P150'

    def test_services_detail_short_name(self):
        assert self.response.get('serviceShortName') == '150 分精英班'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()