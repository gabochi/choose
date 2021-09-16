#!/usr/bin/env python

import yaml
import re
import sys
import os

def main():
    
    # define command index variable
    i = 0

    # define command list
    cmd = ['netscape'] * 10

    # get last argument index
    args = len(sys.argv) - 1

    # get the argument, supposedly link
    string = sys.argv[args]

    # open YAML configuration file
    with open("config.yaml", 'r') as stream:
        content = yaml.safe_load(stream)

    # iterate by browser
    for browser in content['browser']:

        # increment command index and store the instruction in the cmd list
        i += 1
        cmd[i] = content['browser'][browser]['cmd']

        # prints index, command, link
        print(i, cmd[i], string)

        # iterate by regex to check for matches
        for step in content['browser'][browser]['regex']:
            match = re.search(step, string)

            # there is a match
            if match:
                print(f"Match {browser}, running {cmd[i]} {string}")

                # build, excecute the command and quit
                command = cmd[i] + " " + string
                os.system(command)
                quit()

    # no matches found, select browser manually
    s = int(input("No matches found, select command by number and press ENTER: "))
    command = cmd[s] + " " + string
    os.system(command)

if __name__ == "__main__":
    main()

