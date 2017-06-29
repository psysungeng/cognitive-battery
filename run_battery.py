import os
import sys

from PyQt5 import QtWidgets
from interface import project_window


if __name__ == '__main__':
    # Get application directory
    base_dir = os.path.dirname(os.path.realpath(__file__))

    # Check if settings file exists. If not, this is a first run
    first_run = not os.path.isfile(os.path.join(base_dir, "settings.ini"))

    # Create main app window
    app = QtWidgets.QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()

    project_manager = project_window.ProjectWindow(base_dir,
                                                   first_run,
                                                   screen_resolution.width(),
                                                   screen_resolution.height())
    project_manager.show()

    sys.exit(app.exec_())
