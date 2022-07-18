# Interview Project

## Overview

This is a small project, based on a (contrived) real-world use-case, to take on in a pair-programming session.
It is designed to be open-ended, and adaptable to a given candidate's experience.
Early sections are routine and prescriptive, later sectons are complex and can be taken in any direction.
Some sections will present no challenge to a candidate; they may move through these quickly, or they could be skipped to focus on a different topic. 
Whenever the candidate's experience tops out, shift the exercise to pair-learning to figure out togther how to move forward with the exercise.

## Background

We have a server connected to the internet.
Team members from our company ssh to that server for their work.
Each ssh session is logged, with the IP address of the user, start and end time of the session.
The format of each log line is:

`{ip}.{ip}.{ip}.{ip} : dd/mm/yy hh:mm - dd/mm/yy hh:mm`

For example:

`80.112.125.122 : 18/07/22 01:06 - 18/07/22 01:18`

We would like to take log files like this, understand the contents, and perform some basic analysis to alert us if anything concerning is happening... things like extra long ssh sessions, or some IPs accessing repeatedly.

## Example roadmap

#### Getting started
1. Clone this repo
2. Run `generate_test_logs.py` to create some mock ssh logs to analyze
3. Create a script to read in the logfile
4. Parse the entries in the logfile into a suitable data structure
5. Convert start-end timestamps to session duration
6. For a given log file, calculate which log entries are in the 95th percentile of session length
7. For a given log file, report on whether any IPs are accessing the host multiple times

#### Streaming
8. Consider how to operate live data - run `stream_test_logs.py`, pipe to a file or socket, and read in the live data
9. Apply the same analyses to this streaming data: how can we alert on long sessions or multiple accesses?

#### Infrastructure
10. We need to deploy this to the running server. How would you set this up?
11. How would you automate the deployment/configuration of this multiple servers?

#### Architecture
12. How could we send alerts/data from multiple servers?
13. How could we consume and correlate alerts/data from multiple servers?