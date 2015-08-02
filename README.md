# CatFeeder
Please read LICENSE first!

## About
Our cat feeder broke. To fix it, I put a Raspberry Pi (https://www.raspberrypi.org/) in it. Its now POE (Power over ethernet) - no more D batteries!
This is what I quickly built using a simple Python script (run via cron). The Python script could probably be improved, as I have never Written python before.
This repo contains schemas and code I'm currently using in the hope that they will be useful for somebody else.

## Feeder
The feeder internally is very simple, its just a motor and a switch. The motor only goes one way.
Attached to the motor is a gear with 4 parts that hit the switch when the feeding mechanism
(which also has 4 compartments) reaches a certain point.

## Schedule (sudo crontab -e)
(Two feeds once in the morning, one at midday and another at 7PM)
```
0 6 * * * (cd /path/to/repo/CatFeeder && /path/to/repo/feed.sh && /path/to/repo/feed.sh) > /dev/null 2>&1
0 12 * * * (cd /path/to/repo/CatFeeder && /path/to/repo/feed.sh) > /dev/null 2>&1
0 19 * * * (cd /path/to/repo/CatFeeder && /path/to/repo/feed.sh) > /dev/null 2>&1
```
Note: Don't forget to set the correct time zone on your pi :)
```
#date
#sudo dpkg-reconfigure tzdata
#date
```
