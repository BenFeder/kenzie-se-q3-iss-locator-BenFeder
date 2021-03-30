#!/usr/bin/env python

import requests
import time

__author__ = 'Benjamin Feder'


def astronauts_in_space():
    """
    Function to obtain list of astronauts currently in space
    and print the total number in space, their full names, and
    the spacecraft they are currently on board
    """
    response = requests.get('http://api.open-notify.org/astros.json')
    response_data = response.json()

    total_number = response_data["number"]

    full_names_and_crafts = ""
    for person in response_data["people"]:
        full_names_and_crafts += person["name"] + ": " + person["craft"] + "; "

    print(total_number, "total people in space: ", full_names_and_crafts)


def current_location():
    """
    Function obtains current location of ISS and prints current
    lattitude and longitude along with a timestamp
    """
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response_data = response.json()

    iss_position = response_data["iss_position"]
    current_time = time.ctime(response_data["timestamp"])

    print("The ISS's current geolocation is at latitutde: ", iss_position["latitude"], ", and longitude: ",
          iss_position["longitude"], " at ", current_time, ". ")


def indianapolis_time():
    """
    Function to find out next time ISS will be overhead
    Indianapolis, Indiana and print out the time in
    human-readable format
    """
    coordinates = {'lat': 39.791, 'lon': -86.148003}
    response = requests.get(
        "http://api.open-notify.org/iss-pass.json", params=coordinates)
    response_data = response.json()

    pass_time = time.ctime(response_data["request"]["datetime"])

    print("The ISS will pass Indianapolis next at: ", pass_time)


def main():
    """
    Run three functions
    """
    astronauts_in_space()
    current_location()
    indianapolis_time()


if __name__ == '__main__':
    main()
