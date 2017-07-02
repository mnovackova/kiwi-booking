import book_flight
import json

def test_booking(monkeypatch):
    class fake_json:
        ok = True
        def json(self):
            with open("data/booking.json", 'r', encoding='utf-8') as file:
                return json.load(file)

    monkeypatch.setattr(book_flight.requests, 'post', lambda url, json: fake_json())


    a = book_flight.booking(None)
    assert a == "C3TZXMA"


def test_wrong_api(monkeypatch):
    class fake_json:
        ok = False
        status_code = 500

    monkeypatch.setattr(book_flight.requests, 'post', lambda url, json: fake_json())
    try:
        book_flight.booking(None)
    except SystemExit as e:
        assert e.code == 1
    else:
        assert False
