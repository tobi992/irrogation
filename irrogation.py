from irrogation import irrogation_system
# from irrogation import raspberry
import logging
import time

# from telegrambot import botrunner

print "starting irrogation control app"

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

irrogation_system.run_irrogation_system()
