import os
import sys
import imp

class Framework(object):
    """
    CloeeMongo is the base framework class that loads the appropriate config
    module as a class attribute
    """
    def __init__(self, env, app=None):
        self.env = env
        self.app = app
        self._set_config_filename()
        self._load_global_config()
        self._load_app_config()

    def _set_config_filename(self):
        filename = self.env + ".py"
        if self.env == 'local':
            filename = 'base.py'

        self.config_filename = filename

    def _load_global_config(self):
        """
        load_config does the actual loading of config file
        """
        filepath = os.path.join(
                                os.path.dirname(__file__),
                                "../",
                                "config",
                                self.config_filename,
                                )

        config = imp.load_source("config", filepath)

        self.config = config

    def _load_app_config(self):
        """
        _load_app_config loads config for sepcific application and appends to
        self.config
        """
        if not self.app:
            return

        filepath = os.path.join(
                                os.path.dirname(__file__),
                                "../",
                                self.app,
                                "config",
                                self.config_filename
                                )
        config = imp.load_source("config", filepath)

        items = [item for item in dir(config) if not item.startswith("__")]

        for item in items:
            setattr(self.config, item[0], item[1])
