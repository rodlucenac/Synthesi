import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class SalasPageTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome('/path/to/chromedriver')
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_elements_on_salas_page(self):
        self.driver.get(f'{self.live_server_url}/caminho/para/salas')

        self.assertTrue(self.driver.find_element(By.ID, "salas").is_displayed())
        self.assertTrue(self.driver.find_element(By.ID, "folha_salas").is_displayed())
        self.assertTrue(self.driver.find_element(By.ID, "elipse1").is_displayed())

if __name__ == '__main__':
    unittest.main()
