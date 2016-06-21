"""Create, test, and modify the default configuration."""

from pathlib import Path


class ConfigurationHandler(object):
    def __init__(self, appname='', apptoken=''):
        """Initialize the configuration folder name and token file"""
        if (not appname) | (not apptoken):
            raise ValueError(
                'Need both name and token for configuration folder: ',
                appname, apptoken)

        self.configurationfolder = Path.home().joinpath(appname)
        self.application_token = self.configurationfolder.joinpath(apptoken)

    def checkconfigurationfolder(self):
        """Confirm that the application folder and token file exist

        The token serve to prove that an existing folder with the name of
        the application is in fact for that application and not a
        coincidentialy name folder that should not be over written."""

        assert(self.configurationfolder != self.application_token)

        if self.configurationfolder.exists() & \
                self.application_token.exists():
            return(True)
        else:
            return(False)
