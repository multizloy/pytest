import pytest
import source.service as service
import unittest.mock as mock
import requests


@mock.patch("source.service.getUserFromDb")
def testGetUserFromDb(mockGetUserFromDb):
    mockGetUserFromDb.return_value = "Mocked Alice"
    userName = service.getUserFromDb(1)

    assert userName == "Mocked Alice"


@mock.patch("requests.get")
def testGetUsers(mockGet):
    mockResponse = mock.Mock()
    mockResponse.status_code = 200
    mockResponse.json.return_value = {"id": 1, "name": "John Doe"}
    mockGet.return_value = mockResponse
    data = service.getUsers()
    assert data == {"id": 1, "name": "John Doe"}


@mock.patch("requests.get")
def testGetUsersError(mockGet):
    mockResponse = mock.Mock()
    mockResponse.status_code = 400
    mockGet.return_value = mockResponse
    with pytest.raises(requests.HTTPError):
        service.getUsers()
