import sys, names, time, random, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    # Sets OS
    OS = sys.argv[1]
    if OS.startswith('win'):
        OS += '.exe'

    # Store number
    storeNumber = sys.argv[2]
    storeNumXpath = '//button[@data-number="{}"]'.format(storeNumber)

    # Sets area code
    areaCode = sys.argv[3]

    # Gets num orders
    numOrders = int(sys.argv[4])

    # Sets up random and prime list
    random.seed(time.time())
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    random.shuffle(primeList)

    # Email list
    emailList = ['@gmail.com', '@msn.com', '@yahoo.com', '@outlook.com']

    # Headless chrome
    chrome_options = None
    if len(sys.argv) > 5:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")

    # Start time
    startTime = time.time()

    # Gets random sandwich
    wichList = [
        '//*[@id="content_2_3fourthswidth2colright_2_LinksRepeater_ProductResultsDetail_1_ProductAddToCart_1_BuildMyProductButtonQV_1"]',
        '//*[@id="content_2_3fourthswidth2colright_2_LinksRepeater_ProductResultsDetail_2_ProductAddToCart_2_BuildMyProductButtonQV_2"]',
        '//*[@id="content_2_3fourthswidth2colright_2_LinksRepeater_ProductResultsDetail_3_ProductAddToCart_3_BuildMyProductButtonQV_3"]',
        '//*[@id="content_2_3fourthswidth2colright_2_LinksRepeater_ProductResultsDetail_4_ProductAddToCart_4_BuildMyProductButtonQV_4"]',
        '//*[@id="content_2_3fourthswidth2colright_2_LinksRepeater_ProductResultsDetail_9_ProductAddToCart_9_BuildMyProductButtonQV_9"]',
        '//*[@id="content_2_3fourthswidth2colright_2_LinksRepeater_ProductResultsDetail_12_ProductAddToCart_12_BuildMyProductButtonQV_12"]',
        '//*[@id="content_2_3fourthswidth2colright_2_LinksRepeater_ProductResultsDetail_14_ProductAddToCart_14_BuildMyProductButtonQV_14"]'
    ]
    
    # Creates  and sends orders
    count = 0
    while count < numOrders:
        # Gets random name
        fname, lname = names.get_full_name().split()
        phoneNumber = '{}{}{}{}{}{}{}{}'.format(areaCode, random.randint(5,9), random.randint(1,4), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9))

        # Sets up driver
        chromedriverPath = os.path.join('chromedriver', 'chromedriver-{}'.format(OS))
        driver = webdriver.Chrome(chromedriverPath, chrome_options=chrome_options)

        # Goes to URL
        driver.get('http://publix.com')

        # Handles stupid feedback popup
        try:
            # Selects store
            driver.find_element_by_partial_link_text('Store').click()
            driver.find_element_by_id('pblx-txtLocation').send_keys(storeNumber)
            driver.find_element_by_id('pblx-btnStoreSearch').click()
            time.sleep(2)
            driver.find_element_by_xpath(storeNumXpath).click()
            driver.find_element_by_xpath('//button[@class="pblx-panel-close"]').click()

            # Get to deli and select subs
            driver.find_element_by_partial_link_text('Products').click()
            driver.find_element_by_partial_link_text('Online').click()
            driver.find_element_by_partial_link_text('Deli').click()
            driver.find_element_by_partial_link_text('Sub').click()

            # Selects random sammich
            driver.find_element_by_xpath(wichList[random.randint(0, len(wichList)-1)]).click()

            # Select whole sub
            driver.find_element_by_xpath('//*[@id="content_1_3fourthswidth2colright_1_ProductQuantity_RadioButtonSection2"]/div/span').click()
            # Click Build
            driver.find_element_by_xpath('//*[@id="content_1_3fourthswidth2colright_1_ProductAddToCart_BuildMyProductButton"]').click()
            # Select random bread
            driver.find_element_by_xpath('//*[@id="content_1_BuildSubRepeater_SectionHeader_0"]/div[{}]/div/span'.format(random.randint(1,4))).click()
            # Select random cheese
            driver.find_element_by_xpath('//*[@id="content_1_BuildSubRepeater_SectionHeader_1"]/div[{}]/div/span'.format(random.randint(1,7))).click()

            # Select random toppings
            driver.find_element_by_xpath('//*[@id="content_1_BuildSubRepeater_SectionHeader_3"]/div[{}]/div/span'.format(random.randint(1, 4))).click()
            driver.find_element_by_xpath('//*[@id="content_1_BuildSubRepeater_SectionHeader_3"]/div[{}]/div/span'.format(random.randint(5, 8))).click()
            driver.find_element_by_xpath('//*[@id="content_1_BuildSubRepeater_SectionHeader_3"]/div[{}]/div/span'.format(random.randint(9, 12))).click()
            driver.find_element_by_xpath('//*[@id="content_1_BuildSubRepeater_SectionHeader_3"]/div[{}]/div/span'.format(random.randint(13, 15))).click()
            
            # Select random condiments
            driver.find_element_by_xpath('//*[@id="content_1_BuildSubRepeater_SectionHeader_4"]/div[{}]/div/span'.format(random.randint(1,2))).click()
            driver.find_element_by_xpath('//*[@id="content_1_BuildSubRepeater_SectionHeader_4"]/div[{}]/div/span'.format(random.randint(3,4))).click()
            # Heating options
            driver.find_element_by_xpath('//*[@id="content_1_BuildSubRepeater_SectionHeader_5"]/div[{}]/div/span'.format(random.randint(1,3))).click()
            # No combo
            driver.find_element_by_xpath('//*[@id="content_1_ComboSelection"]/div[1]/div[2]/div[2]/div/span').click()
            # Adds to order
            driver.find_element_by_xpath('//*[@id="content_1_MyOrderButton"]').click()
            time.sleep(2)

            # Schedule Order 
            driver.find_element_by_xpath('//*[@id="firstAvailableBtn"]').click()

            # Enters random name, email, and phone number
            email = '{}{}{}{}'.format(fname.lower(), lname.lower(), random.randint(0, 999), emailList[count % len(emailList)])
            driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(fname)
            driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(lname)
            driver.find_element_by_xpath('//*[@id="phoneNumber"]').send_keys(phoneNumber)
            driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
            driver.find_element_by_xpath('//*[@id="confirmEmail"]').send_keys(email)
            
            # Submit order
            driver.find_element_by_xpath('//*[@id="btnSubmitOrder"]').click()

            # Waits and closes
            twait = primeList[count % len(primeList)] * 60
            time.sleep(twait)
            driver.close()

            # Prints and increments count
            count += 1
            print('Sub Order Number Complete: {}'.format(count))

        # Starts order over if stupid feedback popup, pops up
        except:
            driver.close()

    # Calcs and prints time it took to finish
    seconds = int(time.time() - startTime)
    minutes = int(seconds // 60)
    hours = int(minutes // 60)
    minutes = int(minutes % 60)
    runtime = 'Runtime(h:m:s): {}:{}:{}'.format(str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2))
    print('Total Orders: {}'.format(count))
    print(runtime)

if __name__ == '__main__':
    main()
