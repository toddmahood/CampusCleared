# CampusCleared
A POC script to automatically complete the CampusClear COVID-19 symptom screener each day.

This script was written in the Fall of 2020. It was inspired by my growing ambition to automate daily tasks and the fear that I would inevitably forget to complete my screener. 

![Relevant xkcd](https://imgs.xkcd.com/comics/is_it_worth_the_time.png)

## Reflections:
Looking back, this script could've been written using the `schedule` or `Timer` module. My hacky solution that checks the day every two hours probably left some performance on the table. Although, at the time, it was quicker for me to implement it this way. This could've also been accomplished with a cron job or scheduled task in Window's Task Scheduler. If I had the opportunity to write this script again, I probably would invest my time differently. While this was a neat way to practice my Python skills, it really defeats the purpose of the app.

## Disclaimer: 
This should not be used in place of screening yourself each day using the app. I have only decided to publish it because the app no longer allows for new installations and many schools have long abandoned the daily screening requirement. I have also removed all relevant POST data leaving only the endpoint.
