from typing import Dict

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QListWidget
from PyQt5.uic import loadUi

from .plugin_list_item.plugin_list_item import PluginListItem
from brainframe.client.api import api
from brainframe.client.ui.resources.paths import qt_ui_paths


class PluginList(QListWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        loadUi(qt_ui_paths.plugin_list_ui, self)

        # Things that exist
        # print(self.plugin_container)

        # Query API for existing plugins

        # Populate plugin_container layout with those plugins
        # names = api.get_plugin_names()