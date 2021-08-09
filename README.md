# Docfind
Docfind is a webapp where you can find details of doctors around Bangladesh. The goal is to keep a centralized database and ease of navigation for finding doctors easily. It also incorporates some advanced filters for searching doctors.

**Current Features:**
Has a search bar and can search doctors by `name`, `hospital`,`bio`,`speciality`,`disease treatments`,`hospital location`,`appointment`.

**Bugs:**
This project is in its very early state and contains numerous issues that we are working on to fix. For starters, the webpage isn't responsive and may break on mobile devices/smaller screens. The search filters don't work properly as well as it is not supplied with any default fonts which can cause weird glitchings.

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

***N.B.: It is recommended to fork the project and `git clone` it to your machine for additional development. It will later help us if you wish to merge your developments with pull requests.***

### Pre-requisites

This project requires at least `python 3.6` or above. `pip` should also required to install required python packages. To check python version type following in terminal:
```
python3 --version
```
if it doesn't show then `python3` must be installed first.

If you are on Ubuntu/Ubuntu based distros with `apt` package manager you install via the following command.

### On Linux Distros with `apt` package manager
```
sudo apt-get update
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev python3-pip
```

Most linux distribution come with some package manager using which `python` along with `pip` can be installed. Synaptic package manager also contains python distribution.

On other operating systems(Windows/MacOS), please follow the link [**here**](https://www.python.org/downloads/). On MacOS, Python installation is also available using `brew`.

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
Since now you are in a virtual environment it is not necessary to use `pip3` or `python3` (because it doesn't have any other python installation). Instead `pip` and `python` can be used without issue.

The packages are written in the `requirements.txt` file. To install them all at once type the following command:
```
pip install -r requirements.txt
```
Run the command again to ensure all packages installed properly. This should set you up to run the project on localhost.

### Running on localhost/browser
To check any errors, you must run `manage.py`.
```
python manage.py check
```
It may or may not give some warnings. Warnings won't stop the project from running. Unless it doesn't show any errors/tracebacks, run the project using:
```
python manage.py runserver
```
Now go to `localhost` or `127.0.0.1:8000/` to check whether it ran properly or not.

**That's it. You are ready to go for development.**

If you still face any issues, try searching StackOverflow or other forums. It is likely that they will have the solution. Still if you can't solve, mail me  [**here**](mailto:dr6j0wkjg@relay.firefox.com).
