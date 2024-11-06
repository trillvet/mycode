#!/usr/bin/env python3

def main():
    switch = {"hostname":"sw1","ip":"10.0.1.1","version":"1.2","vendor":"cisco"}

    print(switch)

    print(type(switch))

    print( switch["hostname"] )
    print( switch["ip"])

    print( switch["lynx"] )

if __name__ == "__main__":
    main()
