# -*- coding: utf-8 -*-
"""
@Time ： 2022/7/26 13:27
@Auth ： 罗忠建

"""
from selenium.webdriver.common.by import By
from time import sleep


def work_module(driver, Parent_module, module_name):
    """定位1级模块"""
    driver.find_element(By.XPATH, "//div[text()='" + Parent_module + "']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//span[text()='" + module_name + "']").click()


def access_module(driver, Parent_module, module_name, sub_module_name):
    """定位2级模块"""
    sleep(2)
    driver.find_element(By.XPATH, "//div[text()='" + Parent_module + "']").click()
    driver.find_element(By.XPATH, "//span[text()='" + module_name + "']").click()
    driver.find_element(By.XPATH, "//span[text()='" + sub_module_name + "']").click()


if __name__ == '__main__':
    pass
