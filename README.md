# ServiceMonitoringApplication
This service helps in restarting your application that are running on a specific port using the command supplied 
This service can be added to a crontab on a linux server . The crontab will handle the running of the file at different interval.
This service has been tested on MAC and linux OS.

## Requirements for installation on a linux machine
1. Python 3 
2. crontab
3. Little knowledge about linux environment

## Installation Guide
- Ensure that python 3 and crotab have been installed on your server.

- clone the repository
[You can download or clone the repository here](https://github.com/teesamuel/ServiceMonitoringApplication.git).


- Edit the file by passing the appropriate commant and application port

- `run crontab -e` 

- pass the file to crontab and save your editor

For example, to run the service every 5 minutes you can set it up like this

Command to execute a cron after every 5 minutes assuming my projedct reside in directory (/scripts/ServiceMonitoringApplication/) .	

`*/5* * * * *  /usr/bin/python /scripts/ServiceMonitoringApplication/ServiceMonitor.py`

 [For more information on crontab](https://www.adminschoice.com/crontab-quick-reference).

