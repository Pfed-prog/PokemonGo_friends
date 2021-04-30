from selenium import webdriver

code = 839428349643 ## enter your pokemon go code here
driver = webdriver.Firefox(executable_path=f'geckodriver')
driver.get('https://www.pokemongofriendcodes.com/')
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form/div[1]/div[1]/input").send_keys(code)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form/div[2]/div/button").click()
