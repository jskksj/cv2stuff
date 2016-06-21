"""Create, test, and modify the default configuration."""

from pathlib import Path


class ConfigurationHandler(object):
    def __init__(self, appname='', apptoken=''):
        """Initialize the configuration folder name and token file"""
        if (not appname) | (not apptoken):
            raise ValueError(
                'Need both name and token for configuration folder: ',
                appname, apptoken)

        self.configuration_folder = Path.home().joinpath(appname)
        self.application_token = self.configuration_folder.joinpath(apptoken)

    def check_configuration_folder(self):
        """Confirm that the application folder and token file exist

        The token serve to prove that an existing folder with the name of
        the application is in fact for that application and not a
        coincidentialy name folder that should not be over written."""

        assert(self.configuration_folder != self.application_token)

        if self.configuration_folder.exists() & \
                self.application_token.exists():
            return(True)
        else:
            return(False)
