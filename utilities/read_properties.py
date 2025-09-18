import configparser


config = configparser.RawConfigParser()
config.read('.\\config\\config.ini')


class ReadConfig:
    @staticmethod
    def get_valid_admin_username():
        valid_username = config.get('admin login info', 'valid_username')
        return valid_username

    @staticmethod
    def get_valid_admin_password():
        valid_password = config.get('admin login info', 'valid_password')
        return valid_password

    @staticmethod
    def get_invalid_admin_username():
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username

    @staticmethod
    def get_invalid_admin_password():
        invalid_password = config.get('admin login info', 'invalid_password')
        return invalid_password

    @staticmethod
    def get_admin_login_url():
        admin_login_url = config.get('urls', 'admin_login_url')
        return admin_login_url

    @staticmethod
    def get_store_home_url():
        store_home_url = config.get('urls', 'store_home_url')
        return store_home_url
