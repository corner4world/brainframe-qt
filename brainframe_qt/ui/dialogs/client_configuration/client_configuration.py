from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
from PyQt5.uic import loadUi

from brainframe.client.extensions import DialogActivity
from brainframe.client.ui.resources import settings
from brainframe.client.ui.resources.paths import qt_ui_paths


class ClientConfigActivity(DialogActivity):

    _built_in = True

    def open(self, *, parent: QWidget):
        RenderConfiguration.show_dialog(parent=parent)

    def window_title(self) -> str:
        return QApplication.translate("ClientConfigActivity",
                                      "Client Configuration")

    @staticmethod
    def icon() -> QIcon:
        return QIcon(":/icons/client_config")

    @staticmethod
    def short_name() -> str:
        return QApplication.translate("ClientConfigActivity", "Client")


class RenderConfiguration(QDialog):
    # Default settings
    draw_lines = True
    draw_regions = True
    draw_detections = True
    use_polygons = True
    show_detection_tracks = True,
    show_detection_confidence = True
    show_detection_labels = True
    show_attributes = True

    def __init__(self, parent=None):
        super().__init__(parent)

        loadUi(qt_ui_paths.client_configuration_ui, self)

        self.detections_checkbox.setChecked(
            settings.draw_detections.val())
        self.polygon_radio_button.setChecked(
            settings.use_polygons.val())
        self.bbox_radio_button.setChecked(
            not settings.use_polygons.val())
        self.detection_labels_checkbox.setChecked(
            settings.show_detection_labels.val())
        self.detection_attributes_checkbox.setChecked(
            settings.show_attributes.val())
        self.regions_checkbox.setChecked(
            settings.draw_regions.val())
        self.lines_checkbox.setChecked(
            settings.draw_lines.val())
        self.tracks_checkbox.setChecked(
            settings.show_detection_tracks.val())
        self.recognition_checkbox.setChecked(
            settings.show_recognition_labels.val())
        self.extra_data_checkbox.setChecked(
            settings.show_extra_data.val())

    @classmethod
    def show_dialog(cls, parent):
        ...

        dialog = cls(parent)

        result = dialog.exec_()
        if not result:
            return

        # Get new values from the UI
        _detection_display_type = dialog.detection_radio_group.checkedButton()
        use_polygons = _detection_display_type is dialog.polygon_radio_button

        # Change the settings
        settings.draw_regions.set(
            dialog.regions_checkbox.isChecked())
        settings.draw_lines.set(
            dialog.lines_checkbox.isChecked())
        settings.draw_detections.set(
            dialog.detections_checkbox.isChecked())
        settings.use_polygons.set(
            use_polygons)
        settings.show_detection_labels.set(
            dialog.detection_labels_checkbox.isChecked())
        settings.show_attributes.set(
            dialog.detection_attributes_checkbox.isChecked())
        settings.show_detection_tracks.set(
            dialog.tracks_checkbox.isChecked())
        settings.show_recognition_labels.set(
            dialog.recognition_checkbox.isChecked())
        settings.show_extra_data.set(
            dialog.extra_data_checkbox.isChecked())
