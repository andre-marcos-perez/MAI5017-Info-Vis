from linkedin.User import User
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep

def user_scraper(users, username, password):
    failure = 0
    success = 0
    fail_counter = 0
    previous_failed = False
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized");
    chrome = webdriver.Chrome("C:\chromedriver.exe", chrome_options=options)
    chrome.implicitly_wait(10)
    chrome.get("https://www.linkedin.com/")
    try:
        chrome.find_element_by_class_name("nav__button-secondary").click()
        element = chrome.find_element_by_id("username")
        element.send_keys(username)
        element = chrome.find_element_by_id("password")
        element.send_keys(password)
    except NoSuchElementException:
        chrome.find_element_by_class_name("sign-in-link").click()
        element = chrome.find_element_by_id("username")
        element.send_keys(username)
        element = chrome.find_element_by_id("password")
        element.send_keys(password)
    except Exception as e:
        raise
    for user in users:
        print(" - " + user.forename + " " + user.surname)
        try:
            sleep(3)
            element = chrome.find_element_by_id("ember33")
            element.find_element_by_tag_name("input").clear()
            element.find_element_by_tag_name("input").click()
            sleep(3)
            element.find_element_by_tag_name("input").send_keys(user.forename + " " + user.surname)
            sleep(3)
            chrome.find_element_by_id("nav-search-artdeco-typeahead-results-result-0").click()
            sleep(3)
            try:
                chrome.find_element_by_class_name("pv-top-card-section__summary-toggle-button").click()
                sleep(1)
            except NoSuchElementException:
                pass
            element = chrome.find_element_by_id("profile-content").get_attribute('innerHTML')
            with open("data/users/" + user.forename + "_" + user.surname + ".html", mode="w", encoding="utf-8") as file:
                file.write(element)
            print(" - Success")
            print()
            fail_counter = 0
            success = success + 1
            previous_failed = False
        except TimeoutException:
            raise
        except Exception as e:
            previous_failed = True
            if fail_counter > 1:
                print(" - LinkedIn got you, try again")
                raise
            else:
                print(" - Could not process user due to: " + str(e))
                failure = failure + 1
        finally:
            if previous_failed:
                fail_counter = fail_counter + 1
    print(" - Finished with " + str(success) + " users successfully scraped and " + str(failure) + " failures.")
    chrome.quit()
