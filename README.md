# Allure Report Integration with Pytest

This project demonstrates how to integrate Allure for reporting with Pytest in a Python testing environment. Allure is used to generate beautiful and detailed test reports for better insight into your testing process.

## Project Setup

Follow these instructions to set up Allure and run your tests:

### 1. Install Allure Command-Line Tool

First, download and install the Allure Command-Line tool:

```bash
wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.9/allure-commandline-2.13.9.tgz
**After downloading, extract the contents:**
tar -xzf allure-commandline-2.13.9.tgz
sudo mv allure-2.13.9 /opt/allure
sudo ln -s /opt/allure/bin/allure /usr/local/bin/allure
allure --version
pip install allure-pytest
python -m pytest allure_report.py --alluredir='./allure-dir-path'
allure serve allure-dir-path
