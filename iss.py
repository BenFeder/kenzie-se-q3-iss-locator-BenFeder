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
        full_names_and_crafts += person["name"] + ": " + person["craft"] + ", "

    print(total_number, "total people.", full_names_and_crafts)


def current_location():
    """
    Function obtains current location of ISS and prints current
    lattitude and longitude along with a timestamp
    """


def indianapolis_time():
    """
    Function to find out next time ISS will be overhead
    Indianapolis, Indiana and print out the time in
    human-readable format
    """


def main():
    """
    Run three functions
    """
    astronauts_in_space()
    current_location()
    indianapolis_time()


if __name__ == '__main__':
    main()
