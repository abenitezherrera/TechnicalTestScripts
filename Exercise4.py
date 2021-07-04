from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import csv
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.airportia.com/mexico/licenciado-benito-juarez-international-airport/departures/")

all_iframes = driver.find_elements_by_tag_name("iframe")
if len(all_iframes) > 0:
    print("Ad Found\n")
    driver.execute_script("""
        var elems = document.getElementsByTagName("iframe"); 
        for(var i = 0, max = elems.length; i < max; i++)
             {
                 elems[i].hidden=true;
             }
                          """)
    print('Total Ads: ' + str(len(all_iframes)))
else:
    print('No frames found')



select = driver.find_element_by_xpath("//*[@id='airport_departures_date_range_date']")
option = select.find_elements_by_tag_name("option")
time.sleep(1)
print()
print("Dates available:")
for options in option:
	print(options.text)
	options.click()


time.sleep(10)

seleccionar1 = Select(driver.find_element_by_xpath("//*[@id='airport_departures_date_range_date']"))
seleccionar1.select_by_index(2)
WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='airport_departures_go']"))).click()
time.sleep(10)

#Getting hidden values in table
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/table')))
texto = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/table')))
table = texto.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[2]/table/tbody/tr").text

rows = len(driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[2]/div[2]/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[1]/th"))

test_list = []
for n in range(2, rows+1):
	for b in range(1, cols+1):
		try:
			dato = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[2]/table/tbody/tr["+str(n)+"]/td["+str(b)+"]").text

			test_list.append(dato)
			#print(dato, end='	')
		except Exception as e:
				pass
	#print()

time.sleep(3)

driver.close()

delays_count = test_list.count('Delayed') + test_list.count('Departed Late')
print (f'Number of delays: {delays_count}')

res = []
for ele in test_list:
	if ele.strip():
		res.append(ele)

print(str(res))

n = 8
final = [res[i * n:(i + 1) * n] for i in range((len(res) + n - 1) // n )]
print(final)

final.pop()
final.pop()
with open('List_of_departures.csv', 'w') as f:
	write = csv.writer(f)
	for item in final:
		write.writerow([item[0], item[1], item[2],item[3], item[4], item[5], item[6], item[7]])
