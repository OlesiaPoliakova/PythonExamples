import time
import pytest
from selenium.webdriver import Chrome, Keys


class TestBrowser:
   github_url = "https://github.com/"
   github_title ="GitHub: Where the world builds software · GitHub"
   gitlab_url ="https://about.gitlab.com/"
   gitlab_title="The One DevOps Platform | GitLab"

   @pytest.mark.browser
   def test_back_forward(self, browser):
        browser.get(self.github_url)
        assert browser.current_url == self.github_url, f"Incorrect URL for the link1: {browser.current_url}. Should be: {self.github_url}"
        assert browser.title == self.github_title, f"Incorrect title: {browser.title}, should be: {self.github_title}"

        browser.get(self.gitlab_url)
        assert browser.current_url == self.gitlab_url, f"Incorrect URL for the link1: {browser.current_url}. Should be: {self.gitlab_url}"
        assert browser.title == self.gitlab_title, f"Incorrect title: {browser.title}, should be: {self.gitlab_title}"

        browser.back()
        assert browser.current_url == self.github_url, f"Incorrect URL for the link1: {browser.current_url}. Should be: {self.github_url}"
        assert browser.title == self.github_title, f"Incorrect title: {browser.title}, should be: {self.github_title}"

        browser.forward()
        assert browser.current_url == self.gitlab_url, f"Incorrect URL for the link1: {browser.current_url}. Should be: {self.gitlab_url}"
        assert browser.title == self.gitlab_title, f"Incorrect title: {browser.title}, should be: {self.gitlab_title}"
