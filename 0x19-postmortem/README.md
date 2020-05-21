# Website outage incident report

## Issue Summary

On Wednesday May 21st at 10:00AM CT the Wordpress site for Holberton students went down, returning a 500 error code resulting a close connection. The 100% of the active users were afected by the outage, Users werent able to access any feature on the website. The root cause was a file that was named with a typo, in the wep-includes folder,  that result in a server error.


## Timeline (CT)
- 9:55 AM: The wp-includes folder was updated
- 10:00 AM: Outage begins
- 10:03 AM: Datadog dashboards altert send notification on error
- 10:20 AM: Devops team was involved
- 10:40 AM: Checking logs didn't throw any hints on the error root
- 11:05 AM: Root cause located using strace on the process id
- 11:10 AM: Perform server restart
- 11:11 AM: 100% trafic restored


## Root cause
While the engineers were running strace on the apache server PID they notice that the file class-wp-locale.phpp has an error of "no such file or directory" which mean that it wasn't recongnizing the file on that folder. At the moment of requesting the website, the website response was a 500 error code. 


## Resolution
A simple rename on the affected file was the resolution for that server error. The file had a simple typo on the file extension. An automated Puppet code was able to fix this error, by using the mv command on the web-includes folder.

## Corrective and Preventative Measures
After this incident we implementing an strict method for testing features before commiting to production. The preventative meausere that we took on this outage had a satisfactory result, the datadog monitoring worked as expected, alerting this behavior on the website.
