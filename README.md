### Methor
This is an "delete Gmail email by **SpecificLabel**" task automation tool based on [Selenium](http://www.seleniumhq.org/) for lazy people like me. I've built it for my self and thought, why not share with world!
Here it is, it's not perfect but it's get the job done for me. Please, change it as your need.

> Note: Currently it supports only Windows and Linux and also your Gmail language settings must be English. Only Chrome driver 
is supported for [Selenium](http://www.seleniumhq.org/) :(

Here's some instruction which will help you to get up and running with this tool.
1. Install python and pip for your platform
2. Open terminal
3. Run `pip install selenium` (For Linux use `sudo`)
4. Clone the repository
5. Enter into this directory
6. Run `python gmail_delete_mesage_by_label.py`

At this point the script will ask for 3 things, 
1. Your Gmail username/email
2. Your account password (Don't worry nobody will see them)
3. Specific Label name (of which emails you want to delete)

A browser will pop up and do all the things on behalf of you. Just sit back and observer :)
