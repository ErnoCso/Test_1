#!/usr/bin/env python3

if __name__ == '__main__':
    name = input('Hello! Who are you? ')

    year_now = int(input('What year is it today? '))
    year_born = int(input('What year were you born? '))

    age = year_now - year_born

    print(f'Hello, {name}! This year you will be/are {age} years old.')