#!/usr/bin/env python

import yaml
import re
# import sys  THE OLD WAY
import os
import argparse

def main():
    
    # define command index variable
    i = 0

    # define command list
    cmd = ['netscape'] * 10

    parser = argparse.ArgumentParser(description='Choose your Browser')
    parser.add_argument('-l', '--link', help='Link to follow')
    parser.add_argument('-c', '--config', help='YAML config file')
    args = parser.parse_args()
  
    # get last argument index
    # THE OLD WAY
    # args = len(sys.argv) - 1
    # get the argument, supposedly link
    # THE OLD WAY
    # string = sys.argv[args]

    # open YAML configuration file
    
    # THE OLD WAY
    # with open("config.yaml", 'r') as stream:
    
    # THE NEW WAY
    with open(args.config, 'r') as stream:

        content = yaml.safe_load(stream)

    # iterate by browser
    for browser in content['browser']:

        # increment command index and store the instruction in the cmd list
        i += 1
        cmd[i] = content['browser'][browser]['cmd']

        # prints index, command, link
        print(i, cmd[i], args.link)

        # iterate by regex to check for matches
        for step in content['browser'][browser]['regex']:
            match = re.search(step, args.link)

            # there is a match
            if match:
                print(f"Match {browser}, running {cmd[i]} {args.link}")

                # build, excecute the command and quit
                command = cmd[i] + " " + args.link
                os.system(command)
                quit()

    # no matches found, select browser manually
    s = int(input("No matches found, select cmd by number: "))
    command = cmd[s] + " " + args.link
    os.system(command)

if __name__ == "__main__":
    main()
