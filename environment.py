from utils.logger import setup_custom_logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def before_all(context):
    context.logger = setup_custom_logger("automation-log")
    context.app_url = context.config.userdata.get("app_url")
    context.browser = context.config.userdata.get("browser")

    context.logger.info("*" * 60)
    context.logger.info("Starting execution of automation")
    context.logger.info(f"Running on: {context.browser}")
    context.logger.info(f"APP URL: {context.app_url}")
    context.logger.info("*" * 60)


def before_feature(context, feature):
    if context.browser == "chrome":
        context.driver = webdriver.Chrome(ChromeDriverManager().install())
    elif context.browser == "firefox":
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise Exception("Not a valid browser provided.")

    context.driver.maximize_window()
    context.driver.set_page_load_timeout(context.config.userdata.get("se_default_page_load_time"))
    context.driver.implicitly_wait(context.config.userdata.get("se_default_implicit_time"))


def after_feature(context, feature):
    context.driver.quit()
