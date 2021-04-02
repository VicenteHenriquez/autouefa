from selenium import webdriver
import time

usr = "" #nombreusuario que en este caso corresponde al mail
pswd = "" #password actual
nameus = "" #nombre que usaste en la pagina para ingresar(ej. Jaime)
#menu
print("Eliga una opcion para la pagina uefa.com: 1.inicio de sesion 2.reestablecer pass 3. modificar pass")
el = int(input())
if el == 1:
    print("iniciando sesion")
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.uefa.com") #ingresamos a la pag
    time.sleep(5) #dejamos que cargue todos los elementos durante 5s
    linklogin = browser.find_element_by_link_text("Login")
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    username_box=browser.find_element_by_name("username")
    username_box.send_keys(usr)
    password_box=browser.find_element_by_name("password")
    password_box.send_keys(pswd)
    login_btn=browser.find_element_by_class_name("gigya-input-submit")
    login_btn.submit()
    print("sesion iniciada")

elif el == 2:
    print("Reestableciendo password")
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.uefa.com") #ingresamos a la pag
    time.sleep(5) #dejamos que cargue todos los elementos durante 5s
    linklogin = browser.find_element_by_link_text("Login")
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    time.sleep(3)
    resetpas = browser.find_element_by_link_text("I forgot my password") #olvidamos la pass
    resetpas.click()
    email_box=browser.find_element_by_name("username")
    email_box.send_keys(usr)#rellenamos con nuestro mail
    reset_btn=browser.find_element_by_class_name("gigya-input-submit")
    reset_btn.submit()
    print("Para terminar el proceso, ingrese al mail correspondiente")

elif el == 3:
    print("Escriba su nueva password(Min. 8 car , 1 mayuscula minimo, 1 minuscula minimo, 1 numero minimo y 1 caracter especial): ")
    nuepas = raw_input() #recibimos por terminal la nueva password
    browser = webdriver.Firefox()#teniendo geckodriver en usr/local/bin
    browser.maximize_window()
    browser.get("https://www.uefa.com")
    time.sleep(5)
    linklogin = browser.find_element_by_link_text("Login")
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    linklogin.click()
    browser.implicitly_wait(20)
    username_box=browser.find_element_by_name("username")
    username_box.send_keys(usr)
    password_box=browser.find_element_by_name("password")
    password_box.send_keys(pswd)
    login_btn=browser.find_element_by_class_name("gigya-input-submit")
    login_btn.submit() #inicio de sesion
    time.sleep(3)
    userin = browser.find_element_by_link_text(nameus)
    userin.click()
    userin2 = browser.find_element_by_link_text("Profile")
    userin2.click()
    time.sleep(2)
    changepas = browser.find_element_by_xpath('//div[contains(text(),"Change password")]')
    changepas.click()
    #time.sleep(2)
    password_box1=browser.find_element_by_xpath('//input[@id="gigya-password-password"]')
    password_box1.send_keys(pswd)
    Pasres = nuepas
    newpass= browser.find_element_by_xpath('//input[@id="gigya-password-newPassword"]')
    newpass.send_keys(Pasres) #ingresamos la nueva password
    repas= browser.find_element_by_xpath('//input[@id="gigya-password-passwordRetype"]')
    repas.send_keys(Pasres) #reingresamos
    confnp = browser.find_element_by_xpath('//input[@value="Submit"]')
    confnp.submit()
else:
    print("error")
