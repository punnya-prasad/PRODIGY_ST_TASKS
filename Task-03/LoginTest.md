# Automated Login Test for a Web Application

## Objective
Automate the login functionality of a web application using a test automation library.

## Test Site
[Swag Labs - Demo Site](https://www.saucedemo.com)

- Valid usernames:
  - `standard_user`
  - `locked_out_user`
  - `problem_user`
  - `performance_glitch_user`
  - `error_user`
  - `visual_user`
- Password for all: `secret_sauce`

## Tech Stack Used
- Python + Selenium (or replace with Java/TestNG or your actual tech stack)

## Test Cases

### Positive Test
- **Login with valid username and password**  
  Expected: Redirected to dashboard.

### Negative Tests
- Invalid username / valid password → Error message
- Valid username / wrong password → Error message
- Both fields empty → Error shown
- Username field empty → Error shown
- Password field empty → Error shown

## Files

- `test_login.py` – Contains all test cases
- `requirements.txt` – Required libraries
---

## How to Run

```bash
pip install -r requirements.txt
python test_login.py
