# pytest-gui

This provides a GUI based test runner for Python Unittests and py.tests.

* Load Test cases from any directory.
* Run single test, multiple selected tests or all tests.
* Auto-Discover test cases recursively; in any subdirectory under current directory.
* Display status of every test run, including test output, description, duration and any errors.
* Status text at the bottom showing how many test cases are run, passed, failed or skipped.
* Status bar shown while tests are running - showing progress bar on test completion.

## Getting Started

* If running on Mac: We need to install TKInter library:
```
brew install python-tkinter
```

* Clone the pytest-gui repository
* Install dependencies (`pip install -r requirements.txt`)
* Run command and select the directory to search/run tests from (`python main.py`)

## General Usage

Initial screen consists of a left side pane, showing all the test cases that are discovered
in the selected directory. By default, this would load tests from **_../tests_** directory. We can
load tests from any other directory using the _Reload Tests_ button.

On left side we can select one or multiple test cases. To select multiple test cases, click the control
button and select more test cases. If a parent of a test case is selected, then all tests under that
parent are selected to run.

## Commands.

### Run Button

The Run button provides option to run selected test cases. This would run all test cases that are selected.
If any higher level tests are selected (either a test class or a test file), then all tests under that test
are executed.

### Re-run Button

The Re-run button runs only failures. If no tests have been run, this is similar to Run-All button whereby
it would run all test cases.

### Run-all Button

This would run all test cases.

### Stop Button

This would stop any running test cases. The status of already run test cases would remain as is.

## Test Case Status

There are 4 test cases statuses and they are appropriately color-coded.

* **_Unrun_**: Test cases are not run yet. They would be highlighted with black color.
* **_Pass_**: Test cases are run and passing. They would be highlighted with green color. We also show a green circle on the right pane in details section.
* **_Fail_**:Test cases are run and failing. They would be highlighted with red color. We also show a red circle on the right pane in details section.
* **_Skip_**: Test cases are skipped using @unittest.skip directive. They would be highlighted with blue color. We also see a blue circle on the right pane in details section.
