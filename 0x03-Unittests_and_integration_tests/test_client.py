#!/usr/bin/env python3
""" module containing unit tests
"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized_class
from client import GithubOrgClient
import requests
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """fourth unit test for client.GithubOrgClient
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns
        the correct JSON response.
        """
        url = f"https://api.github.com/orgs/{org_name}"
        expected_org = {"login": org_name, 'url': url}
        mock_get_json.return_value = expected_org

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_org)
        mock_get_json.assert_called_once_with(url)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that GithubOrgClient._public_repos_url
        returns the correct JSON response.
        """
        url = "https://api.github.com/orgs/google/repos"
        mock_org.return_value = {"repos_url": url}

        client = GithubOrgClient("google")
        expected_url = "https://api.github.com/orgs/google/repos"
        self.assertEqual(client._public_repos_url, expected_url)

        mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos
        returns the correct JSON response.
        """
        mock_repo_data = [
                {"name": "repo1", "license": {"key": "mit"}},
                {"name": "repo2", "license": {"key": "apache-2.0"}},
        ]
        mock_get_json.return_value = mock_repo_data

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            url = 'https://api.github.com/orgs/google/repos'
            mock_public_repos_url.return_value = url
            client = GithubOrgClient("google")
            repos = client.public_repos()

            self.assertEqual(repos, [repo["name"] for repo in mock_repo_data])
            mock_get_json.assert_called_once_with(url)
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, r, l_key, exp):
        """Test that GithubOrgClient.has_license
        returns the correct JSON response.
        """
        self.assertEqual(GithubOrgClient.has_license(r, l_key), exp)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class."""

    def setUp(self):
        """Set up common test components."""
        self.client = GithubOrgClient('some_org')
        self.mock_get_patcher = patch('client.get_json')
        self.mocked_get_json = self.mock_get_patcher.start()

    def tearDown(self):
        """Clean up after tests."""
        self.mock_get_patcher.stop()

    def test_public_repos_returns_expected_repos_list(self):
        """Test GithubOrgClient.public_repos returns
        expected repository list."""
        self.mocked_get_json.side_effect = [org_payload, repos_payload]
        self.assertEqual(self.client.public_repos(), expected_repos)
        self.mocked_get_json.assert_called()

    def test_public_repos_with_specific_license_returns_filtered_repos(self):
        """Test GithubOrgClient.public_repos with a license
        filter returns correctly filtered repositories."""
        self.mocked_get_json.side_effect = [org_payload, repos_payload]
        self.assertEqual(self.client.public_repos(license="apache-2.0"),
                         apache2_repos)
        self.mocked_get_json.assert_called()
