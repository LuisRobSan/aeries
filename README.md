# Aeries

Desktop application for viewing your grades (version 1.0). This program only supports schools that use the Aeries Student Information System by Eagle Software.

## Requirements

External dependencies for this project are included in `requirements.txt`. They can be installed via `pip` and are listed below:

* Beautiful Soup 4.4.1
* Selenium 2.53.1

## Usage

Fork the repository and move the folder to the destination you would like it to be in. Open up a Terminal window and follow these commands.

```sh
# If not in current directory, make sure you are
$ cd "path/to/directory"

# Create and set up virtual environment
$ virtualenv venv
$ source venv/bin/activate

## Install external dependencies
(venv) $ pip install -r requirements.txt
```

To run the program, enter `python3 app.py` on an open Terminal window that has an activated virtual environment.

Note: While the program is running, files such as `grades.db`, `source.txt`, and `ghostdriver.log` might appear temporarily, but these will be deleted promptly.
