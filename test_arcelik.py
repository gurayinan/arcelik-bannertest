from core.arcelik import *


class ArcelikMainPageTests(unittest.TestCase, MainPage):

    def setUp(self):
        Core.__init__(self)
        self.driver.get('http://www.arcelik.com.tr')

    def test_banner(self):
        url = self.check_main_banner()
        self.assertEqual(url, self.driver.current_url, "Banner'da sorun var.")

    def test_link1(self):
        url = self.check_online_shop()
        self.assertIn(url, self.driver.current_url, "Link'de sorun var.")

    def test_link2(self):
        url = self.check_auth_tech_service()
        self.assertIn(url, self.driver.current_url, "Link'de sorun var.")

    def test_link3(self):
        url = self.check_promotions()
        self.assertIn(url, self.driver.current_url, "Link'de sorun var.")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()