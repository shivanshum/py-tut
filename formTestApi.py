from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def start_test(
            url,
            textQuestion, 
            paraQuestion, 
            text1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
            para1 = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea',
            btn1 ='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span',
            choice1 = '//*[@id="i13"]/div[3]/div'
    ):
    
    web = webdriver.Chrome(ChromeDriverManager().install())
    web.get(url)
    sleep(2)
    # print(text1 =='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    this = web.find_element_by_xpath(text1)
    this.send_keys(textQuestion)
   

    thisis = web.find_element_by_xpath(para1)
    thisis.send_keys(paraQuestion)

    RadioButtonThisisamultiplechoicequestion = web.find_element_by_xpath(choice1)
    RadioButtonThisisamultiplechoicequestion.click()

    Submit = web.find_element_by_xpath(btn1)
    Submit.click()

    get_confirmation_div_text = web.find_element_by_css_selector('.vHW8K')
    print(get_confirmation_div_text.text)
    if ((get_confirmation_div_text.text) == "Your confirmation will show up on the screen after form is submitted"):
        print ("test was sucessfull")
    else:
        print('test was unsucessfull')
    web.close()
    return True

if __name__ == "__main__":
    t1="shivanshu"
    p1="mishra"
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSeI8_vYyaJgM7SJM4Y9AWfLq-tglWZh6yt7bEXEOJr_L-hV1A/viewform?formkey=dGx0b1ZrTnoyZDgtYXItMWVBdVlQQWc6MQ'
    start_test(url,t1,p1)