#!/usr/bin/env python3

import csv
import sys
import uuid

def main():
    registration_file=sys.argv[1]; # File with registrations from Google Form

    ballots=[];
    votes={};
    ballot_dict={};

    print("Opening file...");

    registration_list = list(csv.DictReader(open(registration_file)));
    if "Are you attending in person or remotely?" in registration_list[0]:
        any_remote = True
    else:
        any_remote = False

    attendanceWriter = csv.DictWriter(open('attendance.csv', 'w', newline=''), ['name','org','remote','attend'], quoting = csv.QUOTE_ALL);
    attendanceWriter.writeheader();
    registrationWriter = csv.DictWriter(open('registration.csv', 'w', newline=''), ['name','org','email','uuid'], quoting = csv.QUOTE_ALL);
    registrationWriter.writeheader();

    print("Writing attendance.csv and registration.csv...");

    names = {};

    for registration in iter(registration_list):
        name = registration['What is your full name?'];
        org = registration['What organization will you be representing?'];
        email = registration['Email Address'];

        if any_remote and registration['Are you attending in person or remotely?'] == "Remotely":
            remote = 1
        else:
            remote = 0

        if name in names:
            print("Omitting duplicate name: " + name);
            continue;
        else:
            names[name] = 1;

        attendanceWriter.writerow({'name': name, 'org': org, 'remote': remote, 'attend': '1'});
        registrationWriter.writerow({'name': name, 'org': org, 'email': email, 'uuid': uuid.uuid1()});

    print("\n=====\n");

    print("Move attendance.csv to the appropriate folder.");

if __name__ == '__main__':
    main()
