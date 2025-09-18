import logging


class Logger:
    @staticmethod
    def log_generator():
        logging.basicConfig(filename='.\\logs\\nopcommerce.log',
                            format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
