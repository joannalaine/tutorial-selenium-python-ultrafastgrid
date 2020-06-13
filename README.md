# Eyes Python Selenium Ultrafastgrid Tutorial
### Pre-requisites:

1. Python 3 is installed on your machine.  [Install Python 3.](https://realpython.com/installing-python/) 
2. Package manager pip is installed on your machine.  [Install pip](https://pip.pypa.io/en/stable/installing/)
3. Virtual Python Environment builder virtualenv is installed on your machine. [Install virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
4. Chrome browser is installed on your machine. [Install Chrome browser](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en&oco=0)  
5. Chrome Webdriver is on your machine and is in the environment variable PATH. Here are some resources from the internet that'll help you.
   * [Download Chrome Webdriver](https://chromedriver.chromium.org/downloads), [Read the docs](https://splinter.readthedocs.io/en/0.1/setup-chrome.html), [Stackoverflow](https://stackoverflow.com/questions/38081021/using-selenium-on-mac-chrome), [Youtube](https://www.youtube.com/watch?time_continue=182&v=dz59GsdvUF8)
6. Git is installed on your machine. [Install git](https://www.atlassian.com/git/tutorials/install-git)
7. If you want to run example from IDE, install any IDE for Python (e.g. [PyCharm](https://www.jetbrains.com/pycharm/download/) )

### Run the example
Start with the ready-to-run code [Github repo](https://github.com/joannalaine/tutorial-selenium-python-ultrafastgrid)
1. Git clone this repo
`git clone git@github.com:joannalaine/tutorial-selenium-python-ultrafastgrid.git`, or download [this as a Zip file](https://github.com/joannalaine/tutorial-selenium-python-ultrafastgrid/archive/master.zip) and unzip it
2. `cd tutorial-selenium-python-ultrafastgrid`
3. Set the APPLITOOLS_API_KEY environment variable
    - Mac: `export APPLITOOLS_API_KEY='YOUR_API_KEY'`
    - Windows: `set APPLITOOLS_API_KEY='YOUR_API_KEY'`
4. Create/activate your virtualenv
    ```
    python -m venv .venv
    source .venv/bin/activate
    ```
5. Install requirements `pip install -r requirements.txt`
6. Run `ultrafastgrid_demo.py` by calling `python ultrafastgrid_demo.py` 
7. If you want run from IDE - start PyCharm, open just cloned project, set project interpreter by File > Settings > Project: > Project Interpreter  choose interpreter by dropdown box; tap Run and choose `ultrafastgrid_demo`.

Read more here: https://www.applitools.com/tutorials/selenium-python.html
