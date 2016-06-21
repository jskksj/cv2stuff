"""Create, test, and modify the default configuration."""

from pathlib import Path


class ConfigurationHandler(object):
    def __init__(self, folder='', token=''):
        """Initialize the configuration folder name and token file"""
        if (not folder) | (not token):
            raise ValueError(
                'Need both name and token for configuration folder: ',
                folder, token)

        self.folder = Path.home().joinpath(folder)
        self.token = self.folder.joinpath(token)

    def check_configuration_folder(self):
        """Confirm that the application folder and token file exist

        The token serve to prove that an existing folder with the name of
        the application is in fact for that application and not a
        coincidentialy name folder that should not be over written."""

        assert(self.folder != self.token)

        if self.folder.exists() & self.token.exists():
            return(True)
        else:
            return(False)
