from time import sleep
from bs4 import BeautifulSoup as bs
import weberror

def util_universal_hku_login(browser, credential):
    username = browser.find_element_by_id('username')
    username.send_keys(credential['username'])
    password = browser.find_element_by_id('password')
    password.send_keys(credential['password'])
    password.submit()
    # browser.wait(1)

def util_getELEMfromProperties(selenium_object, tag_name, feature_dict):
    """
    This function is for getting the selenium object from other properties.  
    the selenium_boject is a selenium object, get from self.browser or self.browser.find('......')
    the feature_dict is like {'class': 'abc'} that for BS4
    the tag_name is a string of the tag name of the target element
    """
    targets = selenium_object.find_elements_by_tag_name(tag_name)        
    
    for target in targets:
        match = True
        for key, value in feature_dict.items():
            if match:   
                if target.get_attribute(key) != value:
                    match = False
        if match:
            return target

def util_HTMLtable2List(HTML_str):
    result = []    
    soup = bs(HTML_str, features = 'lxml')    
    thead = soup.find('thead')
    if thead:
        trs = thead.find_all('tr')
        result += [tr.find_all(['td','th']) for tr in trs]
    tbody = soup.find('tbody')
    if tbody:
        trs = tbody.find_all('tr')
        result += [tr.find_all(['td','th']) for tr in trs]
    if not thead and not tbody:
        trs = soup.find_all('tr')        
        result += [tr.find_all(['td','th']) for tr in trs]
    return result