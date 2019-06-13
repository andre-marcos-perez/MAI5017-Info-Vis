from linkedin.Company import Company
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from time import sleep

def company_scraper(companies, username, password):
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
    for company in companies:
        print(" - " + company.name)
        try:
            sleep(2)
            element = chrome.find_element_by_id("ember33")
            element.find_element_by_tag_name("input").clear()
            element.find_element_by_tag_name("input").click()
            sleep(2)
            for substr in company.name.split(" "):
                element.find_element_by_tag_name("input").send_keys(substr + " ")
                sleep(0.5)
            sleep(2)
            element = chrome.find_element_by_id("nav-search-artdeco-typeahead").get_attribute('innerHTML')
            sleep(2)
            with open("data/companies/" + company.name + ".html", mode="w", encoding="utf-8") as file:
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
                print(" - Could not process company due to: " + str(e))
                failure = failure + 1
        finally:
            if previous_failed:
                fail_counter = fail_counter + 1
    print(" - Finished with " + str(success) + " companies successfully scraped and " + str(failure) + " failures.")
    chrome.quit()
