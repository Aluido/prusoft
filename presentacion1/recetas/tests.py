import os

from django.test import TestCase

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class RecetaSeleniumTest(TestCase):
    def setUp(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opts)

    def tearDown(self):
        self.driver.quit()

    def Test_create(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        create_button = driver.find_element(By.LINK_TEXT, "Crear")
        create_button.click()

        #New recipe page
        title_box = driver.find_element(By.ID, "id_titulo")
        detalle_box = driver.find_element(By.ID, "id_detalle")
        ingredientes_box = driver.find_element(By.ID, "id_ingredientes")
        imagen_box = driver.find_element(By.ID, "id_imagen")
        title_box.send_keys("Prueba Sel")
        detalle_box.send_keys("Esta es una prueba utilizando Selenium.\nLorem ipsum dolor sit amet.")
        ingredientes_box.send_keys("-Lorem\n-Ipsum\n-Dolor (250 gr.)\n-Sit\n-Amet (1 tbsp)")

        image_abs_path = os.path.abspath("./testImage.jpeg")        
        imagen_box.send_keys(image_abs_path)

        send_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary")
        send_button.click()

        driver.get("http://127.0.0.1:8000")
        try:
            recipe_title = driver.find_element(By.LINK_TEXT, "Prueba Sel")
        except:
            return False
        return True

    def Test_index(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        post_button = driver.find_element(By.LINK_TEXT, "Prueba Sel")
        post_button.click()

        #Selenium recipe page
        title_text = driver.find_element(By.CSS_SELECTOR, "h1").text
        content_objects = driver.find_elements(By.CSS_SELECTOR, "p")
        detalle_text = content_objects[1].text
        ingredientes_text = content_objects[0].text

        if title_text != "Prueba Sel" or "-Lorem" not in ingredientes_text or "Esta" not in detalle_text:
            return False
        return True

    def Test_edit(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        post_button = driver.find_elements(By.LINK_TEXT, "Editar")[-1]
        post_button.click()

        #Selenium edit page
        title_box = driver.find_element(By.ID, "id_titulo")
        detalle_box = driver.find_element(By.ID, "id_detalle")
        ingredientes_box = driver.find_element(By.ID, "id_ingredientes")
        imagen_box = driver.find_element(By.ID, "id_imagen")
        title_box.send_keys(" 2")
        detalle_box.send_keys("\nY esta es la continuacion de la prueba.")
        ingredientes_box.send_keys("\n-Prueba (14 ml)")

        send_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary")
        send_button.click()

        driver.get("http://127.0.0.1:8000")
        try:
            recipe_title = driver.find_element(By.LINK_TEXT, "Prueba Sel 2")
        except:
            return False
        return True

    def Test_delete(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000")
        post_button = driver.find_elements(By.LINK_TEXT, "Eliminar")[-1]
        post_button.click()

        #Selenium delete page
        delete_button = driver.find_element(By.CSS_SELECTOR, "button.fcc-btn")
        delete_button.click()

        if driver.current_url != "http://127.0.0.1:8000/":
            print(driver.current_url)
            return False
        try:
            recipe_title = driver.find_element(By.LINK_TEXT, "Prueba Sel 2")
        except:
            return True
        return False

    def test_all(self):
        ret_val = True
        create_status = "[SUCCESS]"
        index_status = "[SUCCESS]"
        edit_status = "[SUCCESS]"
        delete_status = "[SUCCESS]"
        if not self.Test_create():
            ret_val = False
            create_status = "[FAILED]"
            print("FAILED CREATION TEST")
        if not self.Test_index():
            ret_val = False
            index_status = "[FAILED]"
            print("FAILED INDEX TEST")
        if not self.Test_edit():
            ret_val = False
            edit_status = "[FAILED]"
            print("FAILED EDIT TEST")
        if not self.Test_delete():
            ret_val = False
            delete_status = "[FAILED]"
            print("FAILED DELETE TEST")
        print("CREATION TEST\t\t\t " + create_status)
        print("INDEX TEST\t\t\t " + index_status)
        print("EDIT TEST\t\t\t " + edit_status)
        print("DELETE TEST\t\t\t " + delete_status)
        return ret_val

if __name__ == "__main__":
    rst = RecetaSeleniumTest()
    rst.setUp()
    rst.test_all()
    rst.tearDown()
