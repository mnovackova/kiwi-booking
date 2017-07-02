#!/usr/bin/env python3

import click
from datetime import datetime
import requests
import sys

TITLE = 'Mrs'
NAME = 'Marketa'
LASTNAME = 'Novackova'
DOCUMENTID = '552125164566'
BIRTHDAY = '1987-11-04'
EMAIL = 'marketa@novackovi.cz'

@click.command()
@click.option('--date')
@click.option('--from', 'from_')
@click.option('--to', default='')
@click.option('--one-way', is_flag=True)
@click.option('--return', 'return_')
@click.option('--cheapest', is_flag=True)
@click.option('--shortest', is_flag=True)
def url(date, from_, to, one_way, return_, cheapest, shortest):
    ''' Prepare data for a url string '''

    if one_way and return_:
        print("You can't use one_way and return together.")
        sys.exit(1)
    if not from_:
        print("Departure airport is required.")
        sys.exit(1)

    date_parsed = datetime.strptime(date, '%Y-%m-%d')
    date_formated = date_parsed.strftime('%d/%m/%Y')

    params = {'flyFrom': from_,
              'to': to,
              'dateFrom': date_formated,
              'dateTo': date_formated,
    }

    if shortest:
        params['sort'] = 'duration' # shortest
    else:
        params['sort'] = 'price'  # =default cheapest

    #only one flight for faster search - doesn't work:
    #params['one_per_date'] = '1'

    if return_:
        params['daysInDestinationFrom'] = return_
        params['daysInDestinationTo'] = return_ # return
    else:
        params['typeFlight'] = 'oneway' # =default one-way

    json_parsing(params)


def json_parsing(params):
    '''Send request and make from json data for booking'''
    response = requests.get("https://api.skypicker.com/flights", params=params)

    if not response.ok:
        print('Sorry, flights API error:', response.status_code)
        sys.exit(1)

    json = response.json()

    try:
        json["data"][0]["booking_token"]
    except IndexError:
        print("No flight found.")
        sys.exit(1)

    json_booking = {"booking_token": json["data"][0]["booking_token"],
                    "currency": json["currency"],
                    "passengers": [{"title": TITLE,
                                    "firstName": NAME,
                                    "lastName": LASTNAME,
                                    "documentID": DOCUMENTID,
                                    "birthday": BIRTHDAY,
                                    "email": EMAIL,
                                    },
                                ],
    }

    booking(json_booking)


def booking(json_booking):
    '''Make reservation for the flight '''
    response = requests.post('http://37.139.6.125:8080/booking', json=json_booking)

    if not response.ok:
        print('Sorry, booking API error:', response.status_code)
        sys.exit(1)

    json = response.json()
    print(json["pnr"])
    return json["pnr"]


if __name__ == '__main__':
    url()
