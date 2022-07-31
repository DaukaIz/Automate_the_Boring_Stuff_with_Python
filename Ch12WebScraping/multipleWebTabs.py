#! python3
# multipleWebTabs.py - Open several links in separate browser tabs.
# The code was taken from https://stackoverflow.com/questions/26114930/opening-tabs-using-webbrowser-module-in-python

import webbrowser


def main():
    # print(webbrowser._browsers) # for Python 3.x to determine .get() arg
    browser = webbrowser.get("firefox")

    url1 = "http://www.stackoverflow.com"
    url2 = "https://www.linkedin.com"
    url3 = "https://inventwithpython.com"

    urls = [url1, url2, url3]

    first = True
    for url in urls:
        if first:
            browser.open_new(url)
            first = False
        else:
            browser.open_new_tab(url)


if __name__ == "__main__":
    main()
