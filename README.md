# Docfind
Docfind is a webapp where you can details of doctors around Bangladesh. The goal is to keep a centralized database and ease of navigation for finding doctors easily. It also incorporates some advanced filters for searching doctors.

**Current Features:**
Has a search bar and can search doctors by `name`, `hospital`,`bio`,`speciality`,`disease treatments`,`hospital location`,`appointment`.

**Bugs:**
So far we haven't seen any bug yet. However, the webpage isn't responsive and may break on mobile devices/smaller screens. We also initally intended to add some additional filters but couldn't implement yet.

**Future Plans:**
We will be working on this project until we feel it's ready. Our plans / roadmap includes:

```
1. Additional filter for cross database searching
2. Improved and personalized search results by adding user account and Machine Learning search detection algorithm
3. Ability to favorite doctors and save them in user profiles
4. Ability for doctors to add / edit their profile along with appointment links
5. Ability for users to book appointment to hospitals that don't have options yet
6. Adding ability for doctors to host appointments/ online medical session via video conferencing
```
## Development
The project doesn't include any complex or sophisticated framework. It is built with the fundamental features of the Django framework and basic HTML, CSS. Following are steps to download the project on your machine and start developing.

***N.B.: It is recommended to fork the project and `git clone` it to your machine for additional development. It will later help us if you wish to merge you developments with pull requests.***

### Pre-requisites

This project requires at least `python 3.6` or above. `pip` should also installed which will be used to install required python packages. To check python version type following in terminal:
```
python3 --version
```
if it doesn't show then `python3` must be installed first.

If you are on Ubuntu/Ubuntu based distros with `apt` package manager you install via the following command.

### On Linux Distros with `apt` package manager
```
sudo apt-get update
sudo apt-get install sudo apt install build-essential libssl-dev libffi-dev python3-dev python3-pip
```

On other operating systems, please follow the link [**here**](https://www.python.org/downloads/).

### Installing packages

After installing `pip` and `python` the required packages must be downloaded. It **Strongly Recommended** to setup a separate virtual environment for the project.

**Setting up virtual environment:**
```
pip3 install venv
python3 -m venv myvirtualenv
```
This will create the virtual environment. Now activate the virtual environment using the following command(On MacOS/Linux):
```
source myvirtualenv/bin/activate
```
*If you are using Windows CLI/Powershell then don't type the `source` command*

**Installing packages:**
The packages are written in the `requirements.txt` file. To install them all at once type the following command:
```
pip install -r requirements.txt
```
Run the command again if you face any errors. This should set you up to run the project on localhost.

### Running on localhost/browser
To check any errors, you must run `manage.py`.
```
python manage.py check
```
It may or may not give some warnings. If doesn't show any errors/tracebacks run the project using:
```
python manage.py runserver
```
now go to `localhost` or `127.0.0.1:8000/` to check whether it ran properly or not.

**That's it. You are ready to go for development.**
