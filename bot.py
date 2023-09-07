from tkinter import messagebox, HORIZONTAL
from tkinter.ttk import Progressbar
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import threading

from selenium.webdriver.support.wait import WebDriverWait


def create_driver():
    """returns a new chrome webdriver"""
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless")  # make it not visible, just comment if you like seeing opened browsers
    chromeOptions.add_argument("--no-sandbox")
    return webdriver.Chrome(options=chromeOptions)


counter = 0


class SlidoBot:
    def __init__(self, room_hash=None, xpath=None):
        if room_hash is None or xpath is None:
            raise "Invalid arg"
        self.room_hash = room_hash
        self.xpath = xpath

    def vote(self, webdriver=None):
        def voter(driver):
            global counter
            self.driver = driver
            self.driver.get("https://app.sli.do/event/" + self.room_hash + "/live/polls")
            try:
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.xpath)))
                click_elem = self.driver.find_element("xpath", self.xpath)
                click_elem.click()
                submit_btn = self.driver.find_element("id", "poll-submit-button")
                submit_btn.click()
                time.sleep(1)
            except TimeoutException:
                counter += 1
                print("Timed out waiting for page to load" + str(counter))
                if counter == 1:
                    messagebox.showerror("Error", "Can't find the Room Hash or the XPath, Please check them again")
                    exit()

        if webdriver:
            voter(webdriver)
        else:
            webdriver = create_driver()
            voter(webdriver)
            webdriver.quit()


def worker(HASH, XPATH):
    BOT = SlidoBot(HASH, XPATH)
    BOT.vote()


def btest():
    print(thAnim.is_alive())
    print(thWorker.is_alive())


class threads_controller:
    def __init__(self):
        self.event = None
        self.window = None
        self.thWorker = None
        self.Progress_Bar = None
        self.thAnim = None

    def thread_start(self, entry_1, entry_2, entry_3, window):
        global thAnim
        global thWorker
        self.window = window
        self.Progress_Bar = Progressbar(window, style="green.Horizontal.TProgressbar", orient=HORIZONTAL,
                                        length=400,
                                        mode='indeterminate')
        self.Progress_Bar.place(x=0, y=370)
        self.event = threading.Event()
        thAnim = threading.Thread(target=threads_controller.play_animation, args=(self, self.event,))
        thAnim.daemon = True
        thAnim.start()
        thWorker = threading.Thread(target=threads_controller.bot, args=(self, entry_1, entry_2, entry_3,))
        thWorker.daemon = True
        thWorker.start()

    def play_animation(self, event):
        while not event.is_set():
            self.Progress_Bar['value'] += 1
            self.window.update_idletasks()
            time.sleep(0.01)
        else:
            self.Progress_Bar.place_forget()
            self.window.update()

    def thread_stop(self):
        self.event.set()

    def bot(self, thread_amount_entry, xpath_entry, room_hash_entry):
        print("Have fun.")
        global counter
        counter = 0
        xpath = xpath_entry.get()
        room_hash = room_hash_entry.get()
        thread_amount = int(thread_amount_entry.get())
        start_time = time.time()
        threads = []

        for i in range(1, thread_amount + 1):
            th = threading.Thread(target=worker, args=(room_hash, xpath,))
            th.daemon = True
            th.start()
            threads.append(th)

        for th in threads:
            th.join()
        messagebox.showinfo("Success",
                            "All of the votes has been done in: " + str(int(time.time() - start_time)) + "sec")
        print("multiple threads took ", (time.time() - start_time), " seconds")
        threads_controller.thread_stop(self)
