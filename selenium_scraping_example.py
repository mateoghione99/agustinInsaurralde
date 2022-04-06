# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-ALUA/technicals/')

# Aceptamos cookies
# WebDriverWait(driver, 3)\
#     .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
#                                       'button-YKkCvwjV size-xsmall-YKkCvwjV color-brand-YKkCvwjV variant-primary-YKkCvwjV'.replace(' ', '.'))))\
#     .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
aluaprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
aluaprecio = aluaprecio.text

print('aluaprecio')
print(aluaprecio)

print('aluaprecio')

aluarsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
aluarsi = aluarsi.text                

aluarsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
aluarsiestado = aluarsiestado.text                  

aluadmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
aluadmxestado = aluadmxestado.text    

aluamacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
aluamacdestado = aluamacdestado.text  

aluamm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
aluamm30 = aluamm30.text 

aluamm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
aluamm30estado = aluamm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pealua = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pealua = pealua.text                   

pvalua = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvalua = pvalua.text

pbalua = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbalua = pbalua.text

roealua = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roealua = roealua.text

benealua = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benealua = benealua.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AALUA')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()                    
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()                          #/html/body/div[6]/div/div/div[1]/div/div[1]/span

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
aluaad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
aluaad = aluaad.text 

# Extraemos el +DI
aluadipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
aluadipo = aluadipo.text 

# Extraemos el -DI
aluadine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
aluadine = aluadine.text 

# Extraemos el macd
aluamacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
aluamacd = aluamacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C5"
data_to_write = [[aluaprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F5"
data_to_write = [[aluarsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G5"
data_to_write = [[aluarsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I5"
data_to_write = [[aluadine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J5"
data_to_write = [[aluadipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K5"
data_to_write = [[aluadmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q5"
data_to_write = [[aluaad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W5"
data_to_write = [[aluamacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y5"
data_to_write = [[aluamm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z5"
data_to_write = [[aluamm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE5"
data_to_write = [[pealua]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO5"
data_to_write = [[pvalua]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ5"
data_to_write = [[pbalua]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP5"
data_to_write = [[roealua]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ5"
data_to_write = [[benealua]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()










#Vamos con BMA

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-BMA/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
bmaprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
bmaprecio = bmaprecio.text

bmarsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
bmarsi = bmarsi.text                

bmarsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
bmarsiestado = bmarsiestado.text                  

bmadmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
bmadmxestado = bmadmxestado.text    

bmamacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
bmamacdestado = bmamacdestado.text  

bmamm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
bmamm30 = bmamm30.text 

bmamm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
bmamm30estado = bmamm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pebma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pebma = pebma.text                   

pvbma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvbma = pvbma.text

pbbma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbbma = pbbma.text

roebma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roebma = roebma.text

benebma = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benebma = benebma.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ABMA')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
bmaad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
bmaad = bmaad.text 

# Extraemos el +DI
bmadipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
bmadipo = bmadipo.text 

# Extraemos el -DI
bmadine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
bmadine = bmadine.text 

# Extraemos el macd
bmamacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
bmamacd = bmamacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C7"
data_to_write = [[bmaprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F7"
data_to_write = [[bmarsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G7"
data_to_write = [[bmarsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I7"
data_to_write = [[bmadine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J7"
data_to_write = [[bmadipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K7"
data_to_write = [[bmadmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q7"
data_to_write = [[bmaad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W7"
data_to_write = [[bmamacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y7"
data_to_write = [[bmamm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z7"
data_to_write = [[bmamm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE7"
data_to_write = [[pebma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO7"
data_to_write = [[pvbma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ7"
data_to_write = [[pbbma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP7"
data_to_write = [[roebma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ7"
data_to_write = [[benebma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()






#Vamos con BYMA
# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-BYMA/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
bymaprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
bymaprecio = bymaprecio.text

bymarsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
bymarsi = bymarsi.text                

bymarsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
bymarsiestado = bymarsiestado.text                  

bymadmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
bymadmxestado = bymadmxestado.text    

bymamacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
bymamacdestado = bymamacdestado.text  

bymamm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
bymamm30 = bymamm30.text 

bymamm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
bymamm30estado = bymamm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pebyma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pebyma = pebyma.text                   

pvbyma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvbyma = pvbyma.text

pbbyma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbbyma = pbbyma.text

roebyma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roebyma = roebyma.text

benebyma = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benebyma = benebyma.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ABYMA')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
bymaad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
bymaad = bymaad.text 

# Extraemos el +DI
bymadipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
bymadipo = bymadipo.text 

# Extraemos el -DI
bymadine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
bymadine = bymadine.text 

# Extraemos el macd
bymamacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
bymamacd = bymamacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C8"
data_to_write = [[bymaprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F8"
data_to_write = [[bymarsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G8"
data_to_write = [[bymarsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I8"
data_to_write = [[bymadine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J8"
data_to_write = [[bymadipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K8"
data_to_write = [[bymadmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q8"
data_to_write = [[bymaad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W8"
data_to_write = [[bymamacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y8"
data_to_write = [[bymamm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z8"
data_to_write = [[bymamm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE8"
data_to_write = [[pebyma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO8"
data_to_write = [[pvbyma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ8"
data_to_write = [[pbbyma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP8"
data_to_write = [[roebyma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ8"
data_to_write = [[benebyma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()








# Vamos con CEPU

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-CEPU/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
cepuprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
cepuprecio = cepuprecio.text

cepursi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
cepursi = cepursi.text                

cepursiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
cepursiestado = cepursiestado.text                  

cepudmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
cepudmxestado = cepudmxestado.text    

cepumacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
cepumacdestado = cepumacdestado.text  

cepumm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
cepumm30 = cepumm30.text 

cepumm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
cepumm30estado = cepumm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pecepu = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pecepu = pecepu.text                   

pvcepu = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvcepu = pvcepu.text

pbcepu = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbcepu = pbcepu.text

roecepu = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roecepu = roecepu.text

benecepu = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benecepu = benecepu.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ACEPU')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
cepuad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
cepuad = cepuad.text 

# Extraemos el +DI
cepudipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
cepudipo = cepudipo.text 

# Extraemos el -DI
cepudine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
cepudine = cepudine.text 

# Extraemos el macd
cepumacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
cepumacd = cepumacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C10"
data_to_write = [[cepuprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F10"
data_to_write = [[cepursi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G10"
data_to_write = [[cepursiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I10"
data_to_write = [[cepudine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J10"
data_to_write = [[cepudipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K10"
data_to_write = [[cepudmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q10"
data_to_write = [[cepuad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W10"
data_to_write = [[cepumacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y10"
data_to_write = [[cepumm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z10"
data_to_write = [[cepumm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE10"
data_to_write = [[pecepu]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO10"
data_to_write = [[pvcepu]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ10"
data_to_write = [[pbcepu]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP10"
data_to_write = [[roecepu]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ10"
data_to_write = [[benecepu]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()







# Vamos con COME

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-COME/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
comeprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
comeprecio = comeprecio.text

comersi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
comersi = comersi.text                

comersiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
comersiestado = comersiestado.text                  

comedmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
comedmxestado = comedmxestado.text    

comemacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
comemacdestado = comemacdestado.text  

comemm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
comemm30 =comemm30.text 

comemm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
comemm30estado = comemm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pecome = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pecome = pecome.text                   

pvcome = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvcome = pvcome.text

pbcome = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbcome = pbcome.text

roecome = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roecome = roecome.text

benecome = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benecome = benecome.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ACOME')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
comead = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
comead = comead.text 

# Extraemos el +DI
comedipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
comedipo = comedipo.text 

# Extraemos el -DI
comedine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
comedine = comedine.text 

# Extraemos el macd
comemacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
comemacd = comemacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C11"
data_to_write = [[comeprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F11"
data_to_write = [[comersi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G11"
data_to_write = [[comersiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I11"
data_to_write = [[comedine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J11"
data_to_write = [[comedipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K11"
data_to_write = [[comedmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q11"
data_to_write = [[comead]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W11"
data_to_write = [[comemacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y11"
data_to_write = [[comemm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z11"
data_to_write = [[comemm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE11"
data_to_write = [[pecome]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO11"
data_to_write = [[pvcome]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ11"
data_to_write = [[pbcome]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP11"
data_to_write = [[roecome]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ11"
data_to_write = [[benecome]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()








# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-CRES/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
cresprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
cresprecio = cresprecio.text

cresrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
cresrsi = cresrsi.text                

cresrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
cresrsiestado = cresrsiestado.text                  

cresdmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
cresdmxestado = cresdmxestado.text    

cresmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
cresmacdestado = cresmacdestado.text  

cresmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
cresmm30 = cresmm30.text 

cresmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
cresmm30estado = cresmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pecres = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pecres = pecres.text                   

pvcres = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvcres = pvcres.text

pbcres = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbcres = pbcres.text

roecres = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roecres = roecres.text

benecres = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benecres = benecres.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ACRES')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
cresad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
cresad = cresad.text 

# Extraemos el +DI
cresdipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
cresdipo = cresdipo.text 

# Extraemos el -DI
cresdine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
cresdine = cresdine.text 

# Extraemos el macd
cresmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
cresmacd = cresmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C12"
data_to_write = [[cresprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F12"
data_to_write = [[cresrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G12"
data_to_write = [[cresrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I12"
data_to_write = [[cresdine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J12"
data_to_write = [[cresdipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K12"
data_to_write = [[cresdmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q12"
data_to_write = [[cresad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W12"
data_to_write = [[cresmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y12"
data_to_write = [[cresmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z12"
data_to_write = [[cresmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE12"
data_to_write = [[pecres]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO12"
data_to_write = [[pvcres]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ12"
data_to_write = [[pbcres]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP12"
data_to_write = [[roecres]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ12"
data_to_write = [[benecres]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()


  # Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-CVH/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                    '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
cvhprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
cvhprecio = cvhprecio.text

cvhrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
cvhrsi = cvhrsi.text                

cvhrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
cvhrsiestado = cvhrsiestado.text                  

cvhdmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
cvhdmxestado = cvhdmxestado.text    

cvhmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
cvhmacdestado = cvhmacdestado.text  

cvhmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
cvhmm30 = cvhmm30.text 

cvhmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
cvhmm30estado = cvhmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pecvh = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pecvh = pecvh.text                   

pvcvh = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvcvh = pvcvh.text

pbcvh = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbcvh = pbcvh.text

roecvh = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roecvh = roecvh.text

benecvh = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benecvh = benecvh.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ACVH')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
cvhad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
cvhad = cvhad.text 

# Extraemos el +DI
cvhdipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
cvhdipo = cvhdipo.text 

# Extraemos el -DI
cvhdine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
cvhdine = cvhdine.text 

# Extraemos el macd
cvhmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
cvhmacd = cvhmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'



where_to_write = "MERVAL!C13"
data_to_write = [[cvhprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F13"
data_to_write = [[cvhrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G13"
data_to_write = [[cvhrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I13"
data_to_write = [[cvhdine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J13"
data_to_write = [[cvhdipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K13"
data_to_write = [[cvhdmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q13"
data_to_write = [[cvhad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W13"
data_to_write = [[cvhmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y13"
data_to_write = [[cvhmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z13"
data_to_write = [[cvhmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE13"
data_to_write = [[pecvh]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO13"
data_to_write = [[pvcvh]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ13"
data_to_write = [[pbcvh]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP13"
data_to_write = [[roecvh]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ13"
data_to_write = [[benecvh]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()






# Vamos con EDN

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-EDN/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
ednprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
ednprecio = ednprecio.text

ednrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
ednrsi = ednrsi.text                

ednrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
ednrsiestado = ednrsiestado.text                  

edndmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
edndmxestado = edndmxestado.text    

ednmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
ednmacdestado = ednmacdestado.text  

ednmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
ednmm30 = ednmm30.text 

ednmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
ednmm30estado = ednmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
peedn = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
peedn = peedn.text                   

pvedn = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvedn = pvedn.text

pbedn = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbedn = pbedn.text

roeedn = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roeedn = roeedn.text

beneedn = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
beneedn = beneedn.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AEDN')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
ednad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
ednad = ednad.text 

# Extraemos el +DI
edndipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
edndipo = edndipo.text 

# Extraemos el -DI
edndine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
edndine = edndine.text 

# Extraemos el macd
ednmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
ednmacd = ednmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'



where_to_write = "MERVAL!C14"
data_to_write = [[ednprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F14"
data_to_write = [[ednrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G14"
data_to_write = [[ednrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I14"
data_to_write = [[edndine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J14"
data_to_write = [[edndipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K14"
data_to_write = [[edndmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q14"
data_to_write = [[ednad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W14"
data_to_write = [[ednmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y14"
data_to_write = [[ednmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z14"
data_to_write = [[ednmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE14"
data_to_write = [[peedn]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO14"
data_to_write = [[pvedn]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ14"
data_to_write = [[pbedn]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP14"
data_to_write = [[roeedn]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ14"
data_to_write = [[beneedn]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()






#Vamos con GGAL
# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-GGAL/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
ggalprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
ggalprecio = ggalprecio.text

ggalrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
ggalrsi = ggalrsi.text                

ggalrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
ggalrsiestado = ggalrsiestado.text                  

ggaldmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
ggaldmxestado = ggaldmxestado.text    

ggalmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
ggalmacdestado = ggalmacdestado.text  

ggalmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
ggalmm30 = ggalmm30.text 

ggalmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
ggalmm30estado = ggalmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
peggal = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
peggal = peggal.text                   

pvggal = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvggal = pvggal.text

pbggal = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbggal = pbggal.text

roeggal = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roeggal = roeggal.text

beneggal = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
beneggal = beneggal.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AGGAL')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
ggalad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
ggalad = ggalad.text 

# Extraemos el +DI
ggaldipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
ggaldipo = ggaldipo.text 

# Extraemos el -DI
ggaldine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
ggaldine = ggaldine.text 

# Extraemos el macd
ggalmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
ggalmacd = ggalmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'



where_to_write = "MERVAL!C15"
data_to_write = [[ggalprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F15"
data_to_write = [[ggalrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G15"
data_to_write = [[ggalrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I15"
data_to_write = [[ggaldine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J15"
data_to_write = [[ggaldipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K15"
data_to_write = [[ggaldmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q15"
data_to_write = [[ggalad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W15"
data_to_write = [[ggalmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y15"
data_to_write = [[ggalmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z15"
data_to_write = [[ggalmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE15"
data_to_write = [[peggal]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO15"
data_to_write = [[pvggal]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ15"
data_to_write = [[pbggal]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP15"
data_to_write = [[roeggal]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ15"
data_to_write = [[beneggal]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()






# Vamos con HARG

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-HARG/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
hargprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
hargprecio = hargprecio.text

hargrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
hargrsi = hargrsi.text                

hargrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
hargrsiestado = hargrsiestado.text                  

hargdmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
hargdmxestado = hargdmxestado.text    

hargmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
hargmacdestado = hargmacdestado.text  

hargmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
hargmm30 = hargmm30.text 

hargmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
hargmm30estado = hargmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
peharg = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
peharg = peharg.text                   

pvharg = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvharg = pvharg.text

pbharg = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbharg = pbharg.text

roeharg = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roeharg = roeharg.text

beneharg = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
beneharg = beneharg.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AHARG')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
hargad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
hargad = hargad.text 

# Extraemos el +DI
hargdipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
hargdipo = hargdipo.text 

# Extraemos el -DI
hargdine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
hargdine = hargdine.text 

# Extraemos el macd
hargmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
hargmacd = hargmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'



where_to_write = "MERVAL!C16"
data_to_write = [[hargprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F16"
data_to_write = [[hargrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G16"
data_to_write = [[hargrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I16"
data_to_write = [[hargdine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J16"
data_to_write = [[hargdipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K16"
data_to_write = [[hargdmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q16"
data_to_write = [[hargad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W16"
data_to_write = [[hargmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y16"
data_to_write = [[hargmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z16"
data_to_write = [[hargmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE16"
data_to_write = [[peharg]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO16"
data_to_write = [[pvharg]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ16"
data_to_write = [[pbharg]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP16"
data_to_write = [[roeharg]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ16"
data_to_write = [[beneharg]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()







# Vamos con LOMA
# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-LOMA/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
lomaprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
lomaprecio = lomaprecio.text

lomarsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
lomarsi = lomarsi.text                

lomarsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
lomarsiestado = lomarsiestado.text                  

lomadmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
lomadmxestado = lomadmxestado.text    

lomamacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
lomamacdestado = lomamacdestado.text  

lomamm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
lomamm30 = lomamm30.text 

lomamm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
lomamm30estado = lomamm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
peloma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
peloma = peloma.text                   

pvloma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvloma = pvloma.text

pbloma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbloma = pbloma.text

roeloma = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roeloma = roeloma.text

beneloma = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
beneloma = beneloma.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ALOMA')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
lomaad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
lomaad = lomaad.text 

# Extraemos el +DI
lomadipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
lomadipo = lomadipo.text 

# Extraemos el -DI
lomadine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
lomadine = lomadine.text 

# Extraemos el macd
lomamacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
lomamacd = lomamacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'



where_to_write = "MERVAL!C18"
data_to_write = [[lomaprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F18"
data_to_write = [[lomarsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G18"
data_to_write = [[lomarsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I18"
data_to_write = [[lomadine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J18"
data_to_write = [[lomadipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K18"
data_to_write = [[lomadmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q18"
data_to_write = [[lomaad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W18"
data_to_write = [[lomamacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y18"
data_to_write = [[lomamm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z18"
data_to_write = [[lomamm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE18"
data_to_write = [[peloma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO18"
data_to_write = [[pvloma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ18"
data_to_write = [[pbloma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP18"
data_to_write = [[roeloma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ18"
data_to_write = [[beneloma]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-MIRG/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
mirgprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
mirgprecio = mirgprecio.text

mirgrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
mirgrsi = mirgrsi.text                

mirgrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
mirgrsiestado = mirgrsiestado.text                  

mirgdmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
mirgdmxestado = mirgdmxestado.text    

mirgmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
mirgmacdestado = mirgmacdestado.text  

mirgmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
mirgmm30 = mirgmm30.text 

mirgmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
mirgmm30estado = mirgmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pemirg = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pemirg = pemirg.text                   

pvmirg = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvmirg = pvmirg.text

pbmirg = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbmirg = pbmirg.text

roemirg = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roemirg = roemirg.text

benemirg = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benemirg = benemirg.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AMIRG')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
mirgad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
mirgad = mirgad.text 

# Extraemos el +DI
mirgdipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
mirgdipo = mirgdipo.text 

# Extraemos el -DI
mirgdine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
mirgdine = mirgdine.text 

# Extraemos el macd
mirgmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
mirgmacd = mirgmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'



where_to_write = "MERVAL!C19"
data_to_write = [[mirgprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F19"
data_to_write = [[mirgrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G19"
data_to_write = [[mirgrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I19"
data_to_write = [[mirgdine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J19"
data_to_write = [[mirgdipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K19"
data_to_write = [[mirgdmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q19"
data_to_write = [[mirgad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W19"
data_to_write = [[mirgmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y19"
data_to_write = [[mirgmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z19"
data_to_write = [[mirgmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE19"
data_to_write = [[pemirg]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO19"
data_to_write = [[pvmirg]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ19"
data_to_write = [[pbmirg]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP19"
data_to_write = [[roemirg]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ19"
data_to_write = [[benemirg]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()










#Vamos con BMA

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-PAMP/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
pampprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
pampprecio = pampprecio.text

pamprsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
pamprsi = pamprsi.text                

pamprsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
pamprsiestado = pamprsiestado.text                  

pampdmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
pampdmxestado = pampdmxestado.text    

pampmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
pampmacdestado = pampmacdestado.text  

pampmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
pampmm30 = pampmm30.text 

pampmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
pampmm30estado = pampmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pepamp = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pepamp = pepamp.text                   

pvpamp = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvpamp = pvpamp.text

pbpamp = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbpamp = pbpamp.text

roepamp = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roepamp = roepamp.text

benepamp = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benepamp = benepamp.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3APAMP')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
pampad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
pampad = pampad.text 

# Extraemos el +DI
pampdipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
pampdipo = pampdipo.text 

# Extraemos el -DI
pampdine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
pampdine = pampdine.text 

# Extraemos el macd
pampmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
pampmacd = pampmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'



where_to_write = "MERVAL!C21"
data_to_write = [[pampprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F21"
data_to_write = [[pamprsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G21"
data_to_write = [[pamprsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I21"
data_to_write = [[pampdine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J21"
data_to_write = [[pampdipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K21"
data_to_write = [[pampdmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q21"
data_to_write = [[pampad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W21"
data_to_write = [[pampmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y21"
data_to_write = [[pampmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z21"
data_to_write = [[pampmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE21"
data_to_write = [[pepamp]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO21"
data_to_write = [[pvpamp]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ21"
data_to_write = [[pbpamp]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP21"
data_to_write = [[roepamp]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ21"
data_to_write = [[benepamp]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()






#Vamos con BYMA
# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-SUPV/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
supvprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
supvprecio = supvprecio.text

supvrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
supvrsi = supvrsi.text                

supvrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
supvrsiestado = supvrsiestado.text                  

supvdmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
supvdmxestado = supvdmxestado.text    

supvmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
supvmacdestado = supvmacdestado.text  

supvmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
supvmm30 = supvmm30.text 

supvmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
supvmm30estado = supvmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pesupv = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pesupv = pesupv.text                   

pvsupv = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvsupv = pvsupv.text

pbsupv = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbsupv = pbsupv.text

roesupv = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roesupv = roesupv.text

benesupv = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benesupv = benesupv.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ASUPV')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
supvad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
supvad = supvad.text 

# Extraemos el +DI
supvdipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
supvdipo = supvdipo.text 

# Extraemos el -DI
supvdine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
supvdine = supvdine.text 

# Extraemos el macd
supvmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
supvmacd = supvmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'



where_to_write = "MERVAL!C23"
data_to_write = [[supvprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F23"
data_to_write = [[supvrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G23"
data_to_write = [[supvrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I23"
data_to_write = [[supvdine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J23"
data_to_write = [[supvdipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K23"
data_to_write = [[supvdmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q23"
data_to_write = [[supvad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W23"
data_to_write = [[supvmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y23"
data_to_write = [[supvmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z23"
data_to_write = [[supvmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE23"
data_to_write = [[pesupv]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO23"
data_to_write = [[pvsupv]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ23"
data_to_write = [[pbsupv]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP23"
data_to_write = [[roesupv]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ23"
data_to_write = [[benesupv]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()








# Vamos con CEPU

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-TECO2/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
teco2precio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
teco2precio = teco2precio.text

teco2rsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
teco2rsi = teco2rsi.text                

teco2rsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
teco2rsiestado = teco2rsiestado.text                  

teco2dmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
teco2dmxestado = teco2dmxestado.text    

teco2macdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
teco2macdestado = teco2macdestado.text  

teco2mm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
teco2mm30 = teco2mm30.text 

teco2mm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
teco2mm30estado = teco2mm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
peteco2 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
peteco2 = peteco2.text                   

pvteco2 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvteco2 = pvteco2.text

pbteco2 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbteco2 = pbteco2.text

roeteco2 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roeteco2 = roeteco2.text

beneteco2 = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
beneteco2 = beneteco2.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ATECO2')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
teco2ad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
teco2ad = teco2ad.text 

# Extraemos el +DI
teco2dipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
teco2dipo = teco2dipo.text 

# Extraemos el -DI
teco2dine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
teco2dine = teco2dine.text 

# Extraemos el macd
teco2macd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
teco2macd = teco2macd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'



where_to_write = "MERVAL!C24"
data_to_write = [[teco2precio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F24"
data_to_write = [[teco2rsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G24"
data_to_write = [[teco2rsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I24"
data_to_write = [[teco2dine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J24"
data_to_write = [[teco2dipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K24"
data_to_write = [[teco2dmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q24"
data_to_write = [[teco2ad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W24"
data_to_write = [[teco2macd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y24"
data_to_write = [[teco2mm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z24"
data_to_write = [[teco2mm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE24"
data_to_write = [[peteco2]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO24"
data_to_write = [[pvteco2]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ24"
data_to_write = [[pbteco2]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP24"
data_to_write = [[roeteco2]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ24"
data_to_write = [[beneteco2]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()







# Vamos con COME

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-TGNO4/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
tgno4precio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
tgno4precio = tgno4precio.text

tgno4rsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
tgno4rsi = tgno4rsi.text                

tgno4rsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
tgno4rsiestado = tgno4rsiestado.text                  

tgno4dmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
tgno4dmxestado = tgno4dmxestado.text    

tgno4macdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
tgno4macdestado = tgno4macdestado.text  

tgno4mm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
tgno4mm30 =tgno4mm30.text 

tgno4mm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
tgno4mm30estado = tgno4mm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
petgno4 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
petgno4 = petgno4.text                   

pvtgno4 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvtgno4 = pvtgno4.text

pbtgno4 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbtgno4 = pbtgno4.text

roetgno4 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roetgno4 = roetgno4.text

benetgno4 = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benetgno4 = benetgno4.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ATGNO4')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()                          #/html/body/div[6]/div/div/div[1]/div/div[1]/span

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
tgno4ad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
tgno4ad = tgno4ad.text 

# Extraemos el +DI
tgno4dipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
tgno4dipo = tgno4dipo.text 

# Extraemos el -DI
tgno4dine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
tgno4dine = tgno4dine.text 

# Extraemos el macd
tgno4macd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
tgno4macd = tgno4macd.text

sleep(2)
from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'



where_to_write = "MERVAL!C26"
data_to_write = [[tgno4precio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F26"
data_to_write = [[tgno4rsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G26"
data_to_write = [[tgno4rsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I26"
data_to_write = [[tgno4dine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J26"
data_to_write = [[tgno4dipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K26"
data_to_write = [[tgno4dmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q26"
data_to_write = [[tgno4ad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W26"
data_to_write = [[tgno4macd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y26"
data_to_write = [[tgno4mm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z26"
data_to_write = [[tgno4mm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE26"
data_to_write = [[petgno4]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO26"
data_to_write = [[pvtgno4]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ26"
data_to_write = [[pbtgno4]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP26"
data_to_write = [[roetgno4]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ26"
data_to_write = [[benetgno4]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()


# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-TGSU2/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
tgsu2precio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
tgsu2precio = tgsu2precio.text

tgsu2rsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
tgsu2rsi = tgsu2rsi.text                

tgsu2rsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
tgsu2rsiestado = tgsu2rsiestado.text                  

tgsu2dmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
tgsu2dmxestado = tgsu2dmxestado.text    

tgsu2macdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
tgsu2macdestado = tgsu2macdestado.text  

tgsu2mm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
tgsu2mm30 = tgsu2mm30.text 

tgsu2mm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
tgsu2mm30estado = tgsu2mm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
petgsu2 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
petgsu2 = petgsu2.text                   

pvtgsu2 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvtgsu2 = pvtgsu2.text

pbtgsu2 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbtgsu2 = pbtgsu2.text

roetgsu2 = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roetgsu2 = roetgsu2.text

benetgsu2 = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benetgsu2 = benetgsu2.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ATGSU2')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
tgsu2ad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
tgsu2ad = tgsu2ad.text 

# Extraemos el +DI
tgsu2dipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
tgsu2dipo = tgsu2dipo.text 

# Extraemos el -DI
tgsu2dine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
tgsu2dine = tgsu2dine.text 

# Extraemos el macd
tgsu2macd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
tgsu2macd = tgsu2macd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C27"
data_to_write = [[tgsu2precio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F27"
data_to_write = [[tgsu2rsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G27"
data_to_write = [[tgsu2rsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I27"
data_to_write = [[tgsu2dine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J27"
data_to_write = [[tgsu2dipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K27"
data_to_write = [[tgsu2dmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q27"
data_to_write = [[tgsu2ad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W27"
data_to_write = [[tgsu2macd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y27"
data_to_write = [[tgsu2mm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z27"
data_to_write = [[tgsu2mm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE27"
data_to_write = [[petgsu2]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO27"
data_to_write = [[pvtgsu2]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ27"
data_to_write = [[pbtgsu2]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP27"
data_to_write = [[roetgsu2]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ27"
data_to_write = [[benetgsu2]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()










#Vamos con BMA

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-TRAN/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
tranprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
tranprecio = tranprecio.text

tranrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
tranrsi = tranrsi.text                

tranrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
tranrsiestado = tranrsiestado.text                  

trandmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
trandmxestado = trandmxestado.text    

tranmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
tranmacdestado = tranmacdestado.text  

tranmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
tranmm30 = tranmm30.text 

tranmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
tranmm30estado = tranmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
petran = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
petran = petran.text                   

pvtran = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvtran = pvtran.text

pbtran = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbtran = pbtran.text

roetran = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roetran = roetran.text

benetran = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benetran = benetran.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ATRAN')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
tranad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
tranad = tranad.text 

# Extraemos el +DI
trandipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
trandipo = trandipo.text 

# Extraemos el -DI
trandine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
trandine = trandine.text 

# Extraemos el macd
tranmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
tranmacd = tranmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C28"
data_to_write = [[tranprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F28"
data_to_write = [[tranrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G28"
data_to_write = [[tranrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I28"
data_to_write = [[trandine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J28"
data_to_write = [[trandipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K28"
data_to_write = [[trandmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q28"
data_to_write = [[tranad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W28"
data_to_write = [[tranmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y28"
data_to_write = [[tranmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z28"
data_to_write = [[tranmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE28"
data_to_write = [[petran]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO28"
data_to_write = [[pvtran]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ28"
data_to_write = [[pbtran]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP28"
data_to_write = [[roetran]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ28"
data_to_write = [[benetran]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()






#Vamos con BYMA
# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-TXAR/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
txarprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
txarprecio = txarprecio.text

txarrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
txarrsi = txarrsi.text                

txarrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
txarrsiestado = txarrsiestado.text                  

txardmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
txardmxestado = txardmxestado.text    

txarmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
txarmacdestado = txarmacdestado.text  

txarmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
txarmm30 = txarmm30.text 

txarmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
txarmm30estado = txarmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
petxar = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
petxar = petxar.text                   

pvtxar = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvtxar = pvtxar.text

pbtxar = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbtxar = pbtxar.text

roetxar = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roetxar = roetxar.text

benetxar = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benetxar = benetxar.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ATXAR')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
txarad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
txarad = txarad.text 

# Extraemos el +DI
txardipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
txardipo = txardipo.text 

# Extraemos el -DI
txardine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
txardine = txardine.text 

# Extraemos el macd
txarmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
txarmacd = txarmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C29"
data_to_write = [[txarprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F29"
data_to_write = [[txarrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G29"
data_to_write = [[txarrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I29"
data_to_write = [[txardine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J29"
data_to_write = [[txardipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K29"
data_to_write = [[txardmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q29"
data_to_write = [[txarad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W29"
data_to_write = [[txarmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y29"
data_to_write = [[txarmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z29"
data_to_write = [[txarmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE29"
data_to_write = [[petxar]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO29"
data_to_write = [[pvtxar]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ29"
data_to_write = [[pbtxar]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP29"
data_to_write = [[roetxar]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ29"
data_to_write = [[benetxar]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()








# Vamos con CEPU

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-VALO/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
valoprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
valoprecio = valoprecio.text

valorsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
valorsi = valorsi.text                

valorsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
valorsiestado = valorsiestado.text                  

valodmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
valodmxestado = valodmxestado.text    

valomacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
valomacdestado = valomacdestado.text  

valomm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
valomm30 = valomm30.text 

valomm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
valomm30estado = valomm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pevalo = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pevalo = pevalo.text                   

pvvalo = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvvalo = pvvalo.text

pbvalo = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbvalo = pbvalo.text

roevalo = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roevalo = roevalo.text

benevalo = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benevalo = benevalo.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AVALO')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
vaload = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
vaload = vaload.text 

# Extraemos el +DI
valodipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
valodipo = valodipo.text 

# Extraemos el -DI
valodine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
valodine = valodine.text 

# Extraemos el macd
valomacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
valomacd = valomacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C30"
data_to_write = [[valoprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F30"
data_to_write = [[valorsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G30"
data_to_write = [[valorsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I30"
data_to_write = [[valodine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J30"
data_to_write = [[valodipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K30"
data_to_write = [[valodmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q30"
data_to_write = [[vaload]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W30"
data_to_write = [[valomacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y30"
data_to_write = [[valomm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z30"
data_to_write = [[valomm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE30"
data_to_write = [[pevalo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO30"
data_to_write = [[pvvalo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ30"
data_to_write = [[pbvalo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP30"
data_to_write = [[roevalo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ30"
data_to_write = [[benevalo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()







# Vamos con COME

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-YPFD/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
ypfdprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
ypfdprecio = ypfdprecio.text

ypfdrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
ypfdrsi = ypfdrsi.text                

ypfdrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
ypfdrsiestado = ypfdrsiestado.text                  

ypfddmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
ypfddmxestado = ypfddmxestado.text    

ypfdmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
ypfdmacdestado = ypfdmacdestado.text  

ypfdmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
ypfdmm30 =ypfdmm30.text 

ypfdmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
ypfdmm30estado = ypfdmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
peypfd = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
peypfd = peypfd.text                   

pvypfd = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvypfd = pvypfd.text

pbypfd = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbypfd = pbypfd.text

roeypfd = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roeypfd = roeypfd.text

beneypfd = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
beneypfd = beneypfd.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AYPFD')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
ypfdad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
ypfdad = ypfdad.text 

# Extraemos el +DI
ypfddipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
ypfddipo = ypfddipo.text 

# Extraemos el -DI
ypfddine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
ypfddine = ypfddine.text 

# Extraemos el macd
ypfdmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
ypfdmacd = ypfdmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C32"
data_to_write = [[ypfdprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F32"
data_to_write = [[ypfdrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G32"
data_to_write = [[ypfdrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I32"
data_to_write = [[ypfddine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J32"
data_to_write = [[ypfddipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K32"
data_to_write = [[ypfddmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q32"
data_to_write = [[ypfdad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W32"
data_to_write = [[ypfdmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y32"
data_to_write = [[ypfdmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z32"
data_to_write = [[ypfdmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE32"
data_to_write = [[peypfd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO32"
data_to_write = [[pvypfd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ32"
data_to_write = [[pbypfd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP32"
data_to_write = [[roeypfd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ32"
data_to_write = [[beneypfd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()



# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-AGRO/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()                           ##anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
agroprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
agroprecio = agroprecio.text

agrorsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
agrorsi = agrorsi.text                

agrorsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
agrorsiestado = agrorsiestado.text                  

agrodmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
agrodmxestado = agrodmxestado.text    

agromacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
agromacdestado = agromacdestado.text  

agromm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
agromm30 = agromm30.text 

agromm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
agromm30estado = agromm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
peagro = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
peagro = peagro.text                   

pvagro = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvagro = pvagro.text

pbagro = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbagro = pbagro.text

roeagro = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roeagro = roeagro.text

beneagro = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
beneagro = beneagro.text                        #anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AAGRO')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()                          #/html/body/div[6]/div/span/div[1]/div/div/div/div[23]

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()                          #/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()                          #/html/body/div[6]/div/div/div[1]/div/div[1]/span/svg

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
agroad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
agroad = agroad.text                  

# Extraemos el +DI
agrodipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
agrodipo = agrodipo.text 

# Extraemos el -DI
agrodine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
agrodine = agrodine.text 

# Extraemos el macd
agromacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
agromacd = agromacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C4"
data_to_write = [[agroprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F4"
data_to_write = [[agrorsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G4"
data_to_write = [[agrorsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I4"
data_to_write = [[agrodine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J4"
data_to_write = [[agrodipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K4"
data_to_write = [[agrodmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q4"
data_to_write = [[agroad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W4"
data_to_write = [[agromacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y4"
data_to_write = [[agromm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z4"
data_to_write = [[agromm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE4"
data_to_write = [[peagro]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO4"
data_to_write = [[pvagro]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ4"
data_to_write = [[pbagro]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP4"
data_to_write = [[roeagro]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ4"
data_to_write = [[beneagro]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()










#Vamos con BMA

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-BBAR/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
bbarprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
bbarprecio = bbarprecio.text

bbarrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
bbarrsi = bbarrsi.text                

bbarrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
bbarrsiestado = bbarrsiestado.text                  

bbardmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
bbardmxestado = bbardmxestado.text    

bbarmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
bbarmacdestado = bbarmacdestado.text  

bbarmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
bbarmm30 = bbarmm30.text 

bbarmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
bbarmm30estado = bbarmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pebbar = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pebbar = pebbar.text                   

pvbbar = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvbbar = pvbbar.text

pbbbar = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbbbar = pbbbar.text

roebbar = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roebbar = roebbar.text

benebbar = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benebbar = benebbar.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ABBAR')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
bbarad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
bbarad = bbarad.text 

# Extraemos el +DI
bbardipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
bbardipo = bbardipo.text 

# Extraemos el -DI
bbardine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
bbardine = bbardine.text 

# Extraemos el macd
bbarmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
bbarmacd = bbarmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C6"
data_to_write = [[bbarprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F6"
data_to_write = [[bbarrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G6"
data_to_write = [[bbarrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I6"
data_to_write = [[bbardine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J6"
data_to_write = [[bbardipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K6"
data_to_write = [[bbardmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q6"
data_to_write = [[bbarad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W6"
data_to_write = [[bbarmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y6"
data_to_write = [[bbarmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z6"
data_to_write = [[bbarmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE6"
data_to_write = [[pebbar]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO6"
data_to_write = [[pvbbar]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ6"
data_to_write = [[pbbbar]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP6"
data_to_write = [[roebbar]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ6"
data_to_write = [[benebbar]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()






#Vamos con BYMA
# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-MORI/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
moriprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
moriprecio = moriprecio.text

morirsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
morirsi = morirsi.text                

morirsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
morirsiestado = morirsiestado.text                  

moridmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
moridmxestado = moridmxestado.text    

morimacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
morimacdestado = morimacdestado.text  

morimm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
morimm30 = morimm30.text 

morimm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
morimm30estado = morimm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pemori = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pemori = pemori.text                   

pvmori = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvmori = pvmori.text

pbmori = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbmori = pbmori.text

roemori = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roemori = roemori.text

benemori = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benemori = benemori.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AMORI')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
moriad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
moriad = moriad.text 

# Extraemos el +DI
moridipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
moridipo = moridipo.text 

# Extraemos el -DI
moridine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
moridine = moridine.text 

# Extraemos el macd
morimacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
morimacd = morimacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C20"
data_to_write = [[moriprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F20"
data_to_write = [[morirsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G20"
data_to_write = [[morirsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I20"
data_to_write = [[moridine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J20"
data_to_write = [[moridipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K20"
data_to_write = [[moridmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q20"
data_to_write = [[moriad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W20"
data_to_write = [[morimacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y20"
data_to_write = [[morimm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z20"
data_to_write = [[morimm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE20"
data_to_write = [[pemori]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO20"
data_to_write = [[pvmori]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ20"
data_to_write = [[pbmori]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP20"
data_to_write = [[roemori]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ20"
data_to_write = [[benemori]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()








# Vamos con CEPU

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-IRSA/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
irsaprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
irsaprecio = irsaprecio.text

irsarsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
irsarsi = irsarsi.text                

irsarsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
irsarsiestado = irsarsiestado.text                  

irsadmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
irsadmxestado = irsadmxestado.text    

irsamacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
irsamacdestado = irsamacdestado.text  

irsamm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
irsamm30 = irsamm30.text 

irsamm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
irsamm30estado = irsamm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
peirsa = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
peirsa = peirsa.text                   

pvirsa = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvirsa = pvirsa.text

pbirsa = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbirsa = pbirsa.text

roeirsa = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roeirsa = roeirsa.text

beneirsa = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
beneirsa = beneirsa.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AIRSA')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
irsaad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
irsaad = irsaad.text 

# Extraemos el +DI
irsadipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
irsadipo = irsadipo.text 

# Extraemos el -DI
irsadine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
irsadine = irsadine.text 

# Extraemos el macd
irsamacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
irsamacd = irsamacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C17"
data_to_write = [[irsaprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F17"
data_to_write = [[irsarsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G17"
data_to_write = [[irsarsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I17"
data_to_write = [[irsadine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J17"
data_to_write = [[irsadipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K17"
data_to_write = [[irsadmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q17"
data_to_write = [[irsaad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W17"
data_to_write = [[irsamacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y17"
data_to_write = [[irsamm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z17"
data_to_write = [[irsamm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE17"
data_to_write = [[peirsa]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO17"
data_to_write = [[pvirsa]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ17"
data_to_write = [[pbirsa]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP17"
data_to_write = [[roeirsa]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ17"
data_to_write = [[beneirsa]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()







# Vamos con COME

# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-TGLT/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
tgltprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
tgltprecio = tgltprecio.text

tgltrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
tgltrsi = tgltrsi.text                

tgltrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
tgltrsiestado = tgltrsiestado.text                  

tgltdmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
tgltdmxestado = tgltdmxestado.text    

tgltmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
tgltmacdestado = tgltmacdestado.text  

tgltmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
tgltmm30 =tgltmm30.text 

tgltmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
tgltmm30estado = tgltmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
petglt = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
petglt = petglt.text                   

pvtglt = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvtglt = pvtglt.text

pbtglt = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbtglt = pbtglt.text

roetglt = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roetglt = roetglt.text

benetglt = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benetglt = benetglt.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ATGLT')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
tgltad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
tgltad = tgltad.text 
sleep(1)
# Extraemos el +DI
tgltdipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
tgltdipo = tgltdipo.text 
sleep(1)
# Extraemos el -DI
tgltdine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
tgltdine = tgltdine.text 
sleep(1)
# Extraemos el macd
tgltmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
tgltmacd = tgltmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C25"
data_to_write = [[tgltprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F25"
data_to_write = [[tgltrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G25"
data_to_write = [[tgltrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I25"
data_to_write = [[tgltdine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J25"
data_to_write = [[tgltdipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K25"
data_to_write = [[tgltdmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q25"
data_to_write = [[tgltad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W25"
data_to_write = [[tgltmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y25"
data_to_write = [[tgltmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z25"
data_to_write = [[tgltmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE25"
data_to_write = [[petglt]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO25"
data_to_write = [[pvtglt]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ25"
data_to_write = [[pbtglt]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP25"
data_to_write = [[roetglt]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ25"
data_to_write = [[benetglt]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()












# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-CARC/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
carcprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
carcprecio = carcprecio.text

carcrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
carcrsi = carcrsi.text                

carcrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
carcrsiestado = carcrsiestado.text                  

carcdmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
carcdmxestado = carcdmxestado.text    

carcmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
carcmacdestado = carcmacdestado.text  

carcmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
carcmm30 = carcmm30.text 

carcmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
carcmm30estado = carcmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pecarc = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pecarc = pecarc.text                   

pvcarc = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvcarc = pvcarc.text

pbcarc = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbcarc = pbcarc.text

roecarc = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roecarc = roecarc.text

benecarc = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benecarc = benecarc.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3ACARC')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
carcad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
carcad = carcad.text 

# Extraemos el +DI
carcdipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
carcdipo = carcdipo.text 

# Extraemos el -DI
carcdine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
carcdine = carcdine.text 

# Extraemos el macd
carcmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
carcmacd = carcmacd.text

import datetime

ahora = datetime.datetime.now()

ahora = ahora.strftime('%d/%m/%Y %H:%M:%S')



from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C9"
data_to_write = [[carcprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F9"
data_to_write = [[carcrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G9"
data_to_write = [[carcrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I9"
data_to_write = [[carcdine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J9"
data_to_write = [[carcdipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K9"
data_to_write = [[carcdmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q9"
data_to_write = [[carcad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W9"
data_to_write = [[carcmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y9"
data_to_write = [[carcmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z9"
data_to_write = [[carcmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE9"
data_to_write = [[pecarc]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO9"
data_to_write = [[pvcarc]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ9"
data_to_write = [[pbcarc]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP9"
data_to_write = [[roecarc]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ9"
data_to_write = [[benecarc]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

















# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-PGR/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
pgrprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
pgrprecio = pgrprecio.text

pgrrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
pgrrsi = pgrrsi.text                

pgrrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
pgrrsiestado = pgrrsiestado.text                  

pgrdmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
pgrdmxestado = pgrdmxestado.text    

pgrmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
pgrmacdestado = pgrmacdestado.text  

pgrmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
pgrmm30 = pgrmm30.text 

pgrmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
pgrmm30estado = pgrmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pepgr = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pepgr = pepgr.text                   

pvpgr = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvpgr = pvpgr.text

pbpgr = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbpgr = pbpgr.text

roepgr = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roepgr = roepgr.text

benepgr = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benepgr = benepgr.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3APGR')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
pgrad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
pgrad = pgrad.text 

# Extraemos el +DI
pgrdipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
pgrdipo = pgrdipo.text 

# Extraemos el -DI
pgrdine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
pgrdine = pgrdine.text 

# Extraemos el macd
pgrmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
pgrmacd = pgrmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C22"
data_to_write = [[pgrprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F22"
data_to_write = [[pgrrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G22"
data_to_write = [[pgrrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I22"
data_to_write = [[pgrdine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J22"
data_to_write = [[pgrdipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K22"
data_to_write = [[pgrdmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q22"
data_to_write = [[pgrad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W22"
data_to_write = [[pgrmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y22"
data_to_write = [[pgrmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z22"
data_to_write = [[pgrmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE22"
data_to_write = [[pepgr]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO22"
data_to_write = [[pvpgr]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ22"
data_to_write = [[pbpgr]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP22"
data_to_write = [[roepgr]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ22"
data_to_write = [[benepgr]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()








# Librerias
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pandas as pd
from time import sleep

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\54357\\Desktop\\CEDEARS\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.tradingview.com/symbols/BCBA-VIST/technicals/')

# Aceptamos cookies
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.button-1iktpaT1 size-s-3mait84m intent-primary-1-IOYcbg appearance-default-dMjF_2Hu'.replace(' ', '.'))))\
    .click()

#Apretamos los indicadores actuales
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > div.tv-tabs__tab.i-active')))\
    .click()

sleep(4)
time.sleep(4)

# Traemos indicadores visibles
vistprecio = driver.find_element_by_css_selector('.tv-symbol-price-quote__value span')
vistprecio = vistprecio.text

vistrsi = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]')
vistrsi = vistrsi.text                

vistrsiestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[3]')
vistrsiestado = vistrsiestado.text                  

vistdmxestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[3]')
vistdmxestado = vistdmxestado.text    

vistmacdestado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[3]')
vistmacdestado = vistmacdestado.text  

vistmm30 = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[2]')
vistmm30 = vistmm30.text 

vistmm30estado = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[7]/td[3]')
vistmm30estado = vistmm30estado.text        

sleep(2)
time.sleep(2)

#Apretamos informacion financiera
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#anchor-page-1 > div > div.tv-category-header__tabs > div > div.tv-tabs__scroll-wrap > div > a:nth-child(3)')))\
    .click()

sleep(2)
time.sleep(2)

#Apretamos estadisticas
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      '#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-feed.tv-feed--no-hindent.tv-feed--tablet-top-indent.tv-feed--no-min-height.tv-feed--no-vertical-margin > div > div > div > div > div > div.scrollWrap-3obNZqvj.noScrollBar-3obNZqvj > div > div > a:nth-child(5)')))\
    .click()                           

sleep(4)
time.sleep(4)

# Traemos informacion financiera visible
pevist = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(9) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pevist = pevist.text                   

pvvist = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(10) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pvvist = pvvist.text

pbvist = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(12) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
pbvist = pbvist.text

roevist = driver.find_element_by_css_selector('#js-category-content > div > div.tv-category__tabs-page.tv-card-exterior > div.tv-category__tab-page.tv-card-exterior > div.js-financials-block-init-ssr > div > div.container-3OdqYJdx > div.wrapper-3OdqYJdx > div > div:nth-child(17) > div.values-jKD0Exn-.values-ZmRZjHnV > div.value-25PNPwRV.additional-25PNPwRV')
roevist = roevist.text

benevist = driver.find_element_by_css_selector('#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__fundamentals.js-header-fundamentals > div.tv-fundamental-block.tv-category-header__fundamentals-block.apply-common-tooltip.common-tooltip-html.js-fund-container > div.tv-fundamental-block__value.tv-fundamental-block__value--sentence-cased.js-symbol-next-earning')
benevist = benevist.text

sleep(2)

# Abrimos grafico
driver.get('https://es.tradingview.com/chart/?symbol=BCBA%3AVIST')

# Abrimos periodos
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div/div')))\
    .click()       

sleep(2)

# seleccionamos semana
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/span/div[1]/div/div/div/div[23]/div/div[1]/div')))\
    .click()       

sleep(2)

# Abrimos los indicadores
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[5]')))\
    .click()                          

# Esperamos 1 segundo
sleep(1)

# Apretamos el indicador A/D
WebDriverWait(driver, 5)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]')))\
    .click()
    
# buscamos el dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("dm")

sleep(1)
time.sleep(1)

#apretamos el dmi
WebDriverWait(driver, 3)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[3]/div[2]/div/div/div[2]/div[1]/span[2]')))\
    .click()                      
                     
                        
time.sleep(2)

# borramos dmi
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .clear()

sleep(1)
time.sleep(1)

# buscamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.input-3n5_2-hI')))\
    .send_keys("conver")

sleep(2)
time.sleep(2)

# apretamos el macd
WebDriverWait(driver, 4)\
    .until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                      'div.main-3Ywm3-oo')))\
    .click()

sleep(2)
time.sleep(2)


# Cerramos la Ventana
WebDriverWait(driver, 2)\
    .until(expected_conditions.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[6]/div/div/div[1]/div/div[1]/span')))\
    .click()

# Esperamos 5 segundos
sleep(2)

# Extraemos el A/D
vistad = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[3]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div')
vistad = vistad.text 

# Extraemos el +DI
vistdipo = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div')
vistdipo = vistdipo.text 

# Extraemos el -DI
vistdine = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[5]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div')
vistdine = vistdine.text 

# Extraemos el macd
vistmacd = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[7]/td[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div')
vistmacd = vistmacd.text

from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1tai4r5LRGILXE-kS32jg30pmr1hrxrZsqIgsTG0rZUU'




where_to_write = "MERVAL!C31"
data_to_write = [[vistprecio]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!F31"
data_to_write = [[vistrsi]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!G31"
data_to_write = [[vistrsiestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!I31"
data_to_write = [[vistdine]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!J31"
data_to_write = [[vistdipo]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!K31"
data_to_write = [[vistdmxestado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Q31"
data_to_write = [[vistad]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!W31"
data_to_write = [[vistmacd]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Y31"
data_to_write = [[vistmm30]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!Z31"
data_to_write = [[vistmm30estado]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AE31"
data_to_write = [[pevist]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AO31"
data_to_write = [[pvvist]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AJ31"
data_to_write = [[pbvist]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AP31"
data_to_write = [[roevist]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

where_to_write = "MERVAL!AQ31"
data_to_write = [[benevist]]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)

driver.close()


