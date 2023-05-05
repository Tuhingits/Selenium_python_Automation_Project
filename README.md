# Basic Selenium_python_Automation_Project
This is my first test automation project based on Selenium-Webdriver with Python. It's still developing package of automated tests of some website. The collection of tests contains:

- user login tests 
- A SignUp page 
- Bookin a an doctor appoinment
- Youtube targetd video channel finding

# Setup Instructions
## Python Setup
You can use any OS: Windows, macOS, Linux, etc.

Your requires Python 3.8 or higher. You can download the latest Python version from Python.org.

And also requires pipenv. To install pipenv, run pip install pipenv from the command line.

You should also have a Python editor/IDE of your choice. Good choices include PyCharm and Visual Studio Code.

You will also need Git to copy this project code. If you are new to Git, try learning the basics.

# WebDriver Setup
For Web UI testing, you will need to install the latest versions of Google Chrome and Mozilla Firefox. You can use other browsers with Selenium WebDriver, but here I use Chrome.
You will also need to install the latest versions of the WebDriver executables for these browsers: ChromeDriver for Chrome and geckodriver for Firefox. Each test case  launch the WebDriver executable for its target browser.
ChromeDriver and geckodriver must be installed on the system path.
## instead of chrome path Using Option
Using options with webdriver.Chrome() method allows you to customize the Chrome browser that will be launched by Selenium WebDriver. You can set various options and preferences for Chrome, such as the window size, the user-agent string, the language, and many others.
![image](https://user-images.githubusercontent.com/44814788/236533488-bc3bbf1a-58f3-44ee-a3d9-a033c424c22a.png)
One of the experimental options that can be added is "detach". When "detach" is set to True, it means that the Chrome browser will continue running even after the Python script has finished executing. This is useful when you want to keep the browser open for further interaction or inspection after the script has completed. If "detach" is not set to True, the browser window will close as soon as the script has finished running.

Using the Chrome file path, on the other hand, requires you to manually specify the path to the Chrome executable on your system. This method is useful if you have a specific version of Chrome that you want to use with Selenium, or if you want to use a Chrome profile with specific settings.

In summary, using options with webdriver.Chrome() method provides more flexibility and control over the Chrome browser that will be launched, while using the Chrome file path is useful for specifying a specific version of Chrome or profile.


# Setup Selenium On your project
Select the project you want to install Selenium on. Click the tab "Python Interpreter" within the project tab. Click the + symbol to add a new library to the project. Type "Selenium" into the new library search box, select the "Selenium" library and confirm by clicking "install

# Code preview

![image](https://user-images.githubusercontent.com/44814788/236527715-7c1aa8da-7f59-4b04-9777-2caf05bd063b.png)
If you want to see screen video Click the link: https://www.linkedin.com/posts/tuhin-hossain-73a791157_technology-sqa-automation-activity-7058337329026908160-SLTE?utm_source=share&utm_medium=member_desktop
