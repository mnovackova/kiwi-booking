import book_flight
import json


def json_parsing_check(monkeypatch, data_json, data_json_booking):
    class fake_json:
        ok = True
        def json(self):
            with open(data_json, 'r', encoding='utf-8') as file:
                return json.load(file)

    monkeypatch.setattr(book_flight.requests, 'get', lambda url, params: fake_json())

    json_booking = {}
    monkeypatch.setattr(book_flight, 'booking', lambda x: json_booking.update(x))

    book_flight.json_parsing(None)
    assert json_booking == data_json_booking


def test_one_way(monkeypatch):
    data_json = 'data/LHR-DXB-oneway.json'
    data_json_booking = {"booking_token": 'GamFTRHoBQ/v6QB8Irykhs320XfjZPfZzlYyhc7jew13xdanm/rg7ltxzOX3QpbugQr/g2HghyllQfZyZagMDdo+TgnK8PXhoX5h96/ASm/UeSNRIWmiEo1BC+loarWssVh4Yh529450wKO0vQG4fZDv++tpC1oatlLeHjMJa+nJzooSwE72DgmCFQt+COuYiY2KhJbj6R55yKElPg8eR2wNLAfDEkIMHPoU1wto9aLttFJVNI8hzSREEkF+41kszoHc7zhkUJSVTUwvIEHzyQabg0suIPcZW5EztS4epGzNWIkW4upkFZqPSzaNj7I1tpha5fmr4t8DogX2nzC3yeGA9G9I6iMEEOgv3rDOVcgFuejWYS6Nafzfy9xWz3Azuys1186p3owLSLAGmN6IT3FvvRJaw3fcbvYzDnH+Ug9bXHHxejTOULCYZEaJiKAhUkF5IxHB6M+h25x7cu2KFg==',
                         "currency": 'EUR',
                         "passengers": [{"title": 'Mrs',
                                         "firstName": 'Marketa',
                                         "documentID": '552125164566',
                                         "birthday": '1987-11-04',
                                         "email": 'marketa@novackovi.cz',
                                         "lastName": 'Novackova'
                                         },
                                        ],
    }
    json_parsing_check(monkeypatch, data_json, data_json_booking)


def test_return(monkeypatch):
    data_json = 'data/LHR-DXB-return.json'
    data_json_booking = {"booking_token": 'GamFTRHoBQ/v6QB8Irykhs320XfjZPfZzlYyhc7jew2EQPsyf3aUbqfeasr/vG13QLe5cslzOHuE8z/xpT5cxQVK+60THjCamhXZ35wvaRC3qs1kjXWLqBR1EfXuZJotvEj6OYqr+4cZ19lfVWp8OZeQIVGVQBwnRSAVq0eRVglpzJYU71gScMdjva8JoCZi6EkCCbUVv17+wX006tgfWINkvydXIgbPRzprWmDHk/n9/eM/anA/aEU4Vz14eAMbJS8T6eC6cPCjMZheud4THpejQoYF7qKxOLpKM3RBsPAKdTUxFWDJGpkKXMoz/DY7Tmo6M4Cvns2l/Bi+rt7X+T/Z1QkqbdkSqzg7ofFeRv+mVmJ2f6PqiZ6ZMU5eu31/F/TbK+WjT3m3mWkKabAj+MWTNBXlfSUpcl8dgZh/NgqJnRM8yBx0QSwnnJsFeenz799KRYtjzIWn/fhtro6j8UMgnzv6NJ3Y8rRbA5xg+K+N8fA8oqoE3dbIrGZ1ih43',
                         "currency": 'EUR',
                         "passengers": [{"title": 'Mrs',
                                         "firstName": 'Marketa',
                                         "documentID": '552125164566',
                                         "birthday": '1987-11-04',
                                         "email": 'marketa@novackovi.cz',
                                         "lastName": 'Novackova'
                                         },
                                        ],
    }
    json_parsing_check(monkeypatch, data_json, data_json_booking)


def test_shortest(monkeypatch):
    data_json = 'data/LHR-DXB-shortest.json'
    data_json_booking = {"booking_token": 'GamFTRHoBQ/v6QB8Irykhs320XfjZPfZzlYyhc7jew1a69GAWqezecCYt+cWhnpzy1/RG8RnwFEKFYGQj4yVI+ndmggSDXCuCpx2Z7vBrcfd/Dt3+CkOtZvKMC8uxY1YNAQekQpL1OxClTLs1LmH05z5QVE6jB9BSvvWIezibIFJBBz/VOA5kAKepTWWmPX6jInGM6oorkuDE4b5MzOECix8VK5AnnPKVdmAGQvQpsymzZFWIbNmEd4K8yajoU+K+YuzONTd7aUPkyiHmFmmEYAJuSJzZZDHpnxw9bSkRaaL9ivwVT5AhI79/4/0mFRln+RUKD6/g/ObKWAsNTQyWAzysdHnnrFbq0WC07h4Ou3PCPe91MHqBJHevMf2qkjB',
                         "currency": 'EUR',
                         "passengers": [{"title": 'Mrs',
                                         "firstName": 'Marketa',
                                         "documentID": '552125164566',
                                         "birthday": '1987-11-04',
                                         "email": 'marketa@novackovi.cz',
                                         "lastName": 'Novackova'
                                         },
                                        ],
    }
    json_parsing_check(monkeypatch, data_json, data_json_booking)


def test_cheapest(monkeypatch):
    data_json = 'data/LHR-DXB-cheapest.json'
    data_json_booking = {"booking_token": 'GamFTRHoBQ/v6QB8Irykhs320XfjZPfZzlYyhc7jew13xdanm/rg7ltxzOX3QpbugQr/g2HghyllQfZyZagMDdo+TgnK8PXhoX5h96/ASm/UeSNRIWmiEo1BC+loarWsIfzIhhlXNRNMK2r+5+nuSxw21oF6/TuG9NsAWNfY+9xIvCAN5NhH4N3yArFlOFDUvn9GiDYnIiYt7m6od5zFMX9xEL2dqKqIyae1ZAbFrXxDDmGgIAmh9gWA8MGzab+akOZWUNibW2vSX7BP+3tJYmU2eAwTtoYmRKqRFDh+rzc6ZYgSBz85cZoCOygg3IZ90sZXbdvpVCiWJNe4fVqllgRv01xDM8I0f1vzxdNtiQih/e5jjfft/EXl0+2FUY+MLVEI5vX8UhZw+oSlowfGBeRnUuYfIV9tT8E+NYN4H/pw1YqM68WieBfZGa26scOXfze+g8/exPLeaqIuRsZuKA==',
                         "currency": 'EUR',
                         "passengers": [{"title": 'Mrs',
                                         "firstName": 'Marketa',
                                         "documentID": '552125164566',
                                         "birthday": '1987-11-04',
                                         "email": 'marketa@novackovi.cz',
                                         "lastName": 'Novackova'
                                         },
                                        ],
    }
    json_parsing_check(monkeypatch, data_json, data_json_booking)


def test_wrong_json(monkeypatch):
    class fake_json:
        ok = True
        def json(self):
            with open('data/empty.json', 'r', encoding='utf-8') as file:
                return json.load(file)

    monkeypatch.setattr(book_flight.requests, 'get', lambda url, params: fake_json())
    try:
        book_flight.json_parsing(None)
    except SystemExit as e:
        assert e.code == 1
    else:
        assert False


def test_wrong_api(monkeypatch):
    class fake_json:
        ok = False
        status_code = 500
        
    monkeypatch.setattr(book_flight.requests, 'get', lambda url, params: fake_json())
    try:
        book_flight.json_parsing(None)
    except SystemExit as e:
        assert e.code == 1
    else:
        assert False
