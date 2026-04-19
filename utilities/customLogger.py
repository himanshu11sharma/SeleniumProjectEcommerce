# import logging
# import os
#
# class LogGen():
#     @staticmethod
#     def loggen():
#         path = "C:\\Users\\LENOVO\\PycharmProjects\\OpencartV1\\logs\\automation.log"
#         logging.basicConfig(filename=path,
#                             format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%m/%d/%Y %I:%M:%S %p')
#
#         logger = logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#
#         return logger
#
#

import logging
import os

class LogGen():
    @staticmethod
    def loggen():
        path = r"C:\Users\LENOVO\PycharmProjects\OpencartV1\logs\automation.log"

        os.makedirs(os.path.dirname(path), exist_ok=True)

        logging.basicConfig(
            filename=path,
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.DEBUG,
            force=True   # ✅ VERY IMPORTANT (Python 3.8+)
        )

        logger = logging.getLogger()
        return logger
