# PyQt5 Battery Percentage Widget Fix Size

I create this widget while making a GUI at work. I was trying to find any open-source battery widget but could not find one. Sharing this fix size widget won't help much but hope for someone was looking for a quick one like me.

![Imgae](https://github.com/Ktheara/pyqt5-widget-battery-percentage/blob/main/image/pyqt5-battery-widget.png)

## Setup

1. If you're using Qt Designer, promot your widget to `BatteryWidget`
2. Copy `batterywidget.py` to your main directory
3. To set the battery value use:
    ```python
    self.yourUIbatteryWidgetName.setValue(value) # between 0 - 100, percentage
    ```

# Note
- This widget is fix size, you can resize in `batterywidget.py`
- Feel free to update and republish it, maybe make it **responsive**.