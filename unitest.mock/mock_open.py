import json
import unittest
from unittest import mock
from unittest.mock import (
    Mock,
    mock_open)


class DUT:

    _PATH = '???'

    def __init__(self):
        self._path = DUT._PATH

    def get(self):
        return self._load(self._path)

    def set(self, key, value):
        content = self._load(self._path)
        content[key] = value
        self._store(self._path, content)

    def delete(self, key):
        content = self._load(self._path)
        del content[key]
        self._store(self._path, content)

    @classmethod
    def _load(cls, path):
        with open(path, 'r', encoding='utf-8') as data_file:
            return json.load(data_file)

    @classmethod
    def _store(cls, path, content):
        with open(path, 'w', encoding='utf-8') as data_file:
            json.dump(
                content,
                data_file,
                ensure_ascii=False)


class OutputStream:

    def __init__(self):
        self._result = ''

    def __str__(self):
        return self._result

    def write(self, obj):
        self._result += obj


class TestDUT(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch("builtins.open", mock.mock_open(read_data='{"key":"value"}'))
    def test_get_ShouldPass(self):
        # act
        dut = DUT()
        content = dut.get()

        # assert
        golden_unit = {'key': 'value'}

        self.assertEqual(
            content,
            golden_unit)

    @mock.patch("builtins.open", return_value=Mock())
    def test_set_ShouldPass(self, mock_open):
        # arrange
        output = OutputStream()

        file_mock = Mock()
        file_mock.read.return_value = '{}'
        file_mock.write = output.write

        mock_open.return_value.__enter__ = Mock(return_value=file_mock)
        mock_open.return_value.__exit__ = Mock()

        # act
        dut = DUT()
        dut.set('key', 'value')

        # assert
        golden_unit = {'key': 'value'}

        self.assertEqual(
            json.loads(str(output)),
            golden_unit)

    @mock.patch("builtins.open", return_value=Mock())
    def test_delete_ShouldPass(self, mock_open):
        # arrange
        output = OutputStream()

        file_mock = Mock()
        file_mock.read.return_value = '{"key":"value"}'
        file_mock.write = output.write

        mock_open.return_value.__enter__ = Mock(return_value=file_mock)
        mock_open.return_value.__exit__ = Mock()

        # act
        dut = DUT()
        dut.delete('key')

        # assert
        golden_unit = {}

        self.assertEqual(
            json.loads(str(output)),
            golden_unit)
