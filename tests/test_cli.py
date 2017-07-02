# python3 -m pytest -v test_cli.py


import click
from click.testing import CliRunner
import book_flight

def url_check(monkeypatch, data_console, data_params):
    params = {}
    monkeypatch.setattr(book_flight, 'json_parsing', lambda x: params.update(x))
    runner = CliRunner()
    result = runner.invoke(book_flight.url, data_console)
    assert result.exit_code == 0
    assert params == data_params

def test_url_simple(monkeypatch):
    data_console = ['--date', '2017-10-13', '--from', 'LHR', '--to', 'DXB']
    data_params = {'flyFrom': 'LHR',
                   'to': 'DXB',
                   'dateFrom': '13/10/2017',
                   'dateTo': '13/10/2017',
                   'typeFlight': 'oneway',
                   'sort': 'price',
    }
    url_check(monkeypatch, data_console, data_params)

def test_url_one_way(monkeypatch):
    data_console = ['--date', '2017-10-13', '--from', 'LHR', '--to', 'DXB', '--one-way']
    data_params = {'flyFrom': 'LHR',
                   'to': 'DXB',
                   'dateFrom': '13/10/2017',
                   'dateTo': '13/10/2017',
                   'typeFlight': 'oneway',
                   'sort': 'price',
    }
    url_check(monkeypatch, data_console, data_params)

def test_url_return(monkeypatch):
    data_console = ['--date', '2017-10-13', '--from', 'LHR', '--to', 'DXB', '--return', '5']
    data_params = {'flyFrom': 'LHR',
                   'to': 'DXB',
                   'dateFrom': '13/10/2017',
                   'dateTo': '13/10/2017',
                   'sort': 'price',
                   'daysInDestinationFrom': '5',
                   'daysInDestinationTo': '5',
    }
    url_check(monkeypatch, data_console, data_params)

def test_url_cheapest(monkeypatch):
    data_console = ['--date', '2017-10-13', '--from', 'LHR', '--to', 'DXB', '--cheapest']
    data_params = {'flyFrom': 'LHR',
                   'to': 'DXB',
                   'dateFrom': '13/10/2017',
                   'dateTo': '13/10/2017',
                   'typeFlight': 'oneway',
                   'sort': 'price',
    }
    url_check(monkeypatch, data_console, data_params)

def test_url_shortest(monkeypatch):
    data_console = ['--date', '2017-10-13', '--from', 'LHR', '--to', 'DXB', '--shortest']
    data_params = {'flyFrom': 'LHR',
                   'to': 'DXB',
                   'dateFrom': '13/10/2017',
                   'dateTo': '13/10/2017',
                   'typeFlight': 'oneway',
                   'sort':'duration',
    }
    url_check(monkeypatch, data_console, data_params)

def test_url_without_from():
    runner = CliRunner()
    result = runner.invoke(book_flight.url, ['--date', '2017-10-13'])
    assert result.exit_code == 1

def test_url_oneway_return():
    runner = CliRunner()
    result = runner.invoke(book_flight.url, ['--date', '2017-10-13',  '--from', 'LHR', '--to', 'DXB', '--one-way', '--return', '5'])
    assert result.exit_code == 1
