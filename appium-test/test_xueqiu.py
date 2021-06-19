from time import sleep

from appium import webdriver

desire_cap = {
        "platformName": "android",
        "deviceName": "emulator-5554",
        "appPackage": "com.baidu.searchbox",
        "appActivity": ".MainActivity",
        "noReset": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)
sleep(10)

el1 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]")
el1.click()
sleep(6)
el2 = driver.find_element_by_id("com.baidu.searchbox:id/SearchTextInput")
el2.send_keys("测试")
sleep(5)
el3 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/com.baidu.searchbox.widget.SlidingPaneLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
el3.click()
