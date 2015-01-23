'''
CheckBox
========

.. versionadded:: 1.4.0

.. image:: images/checkbox.png
    :align: right

:class:`CheckBox` is a specific two-state button that can be either checked or
unchecked. If the CheckBox is in a Group, it becomes a Radio button.
As with the :class:`~kivy.uix.togglebutton.ToggleButton`, only one Radio button
at a time can be selected when the :attr:`CheckBox.group` is set.

An example usage::

    from kivy.uix.checkbox import CheckBox

    # ...

    def on_checkbox_active(checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active')
        else:
            print('The checkbox', checkbox, 'is inactive')

    checkbox = CheckBox()
    checkbox.bind(active=on_checkbox_active)
'''

__all__ = ('CheckBox', )

from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.behaviors import ToggleButtonBehavior


class CheckBox(ToggleButtonBehavior, Widget):
    '''CheckBox class, see module documentation for more information.
    '''

    active = BooleanProperty(False)
    '''Indicates if the switch is active or inactive.

    :attr:`active` is a :class:`~kivy.properties.BooleanProperty` and defaults
    to False.
    '''

    background_checkbox_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_off')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is not active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_off'.
    '''

    background_checkbox_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_on')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_on'.
    '''

    background_checkbox_disabled_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_disabled_off')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is disabled and not active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_disabled_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_disabled_off'.
    '''

    background_checkbox_disabled_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_disabled_on')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is disabled and active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_disabled_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_disabled_on'.
    '''

    background_radio_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_off')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is not active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_off'.
    '''

    background_radio_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_on')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_on'.
    '''

    background_radio_disabled_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_disabled_off')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is disabled and not active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_disabled_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_disabled_off'.
    '''

    background_radio_disabled_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_disabled_on')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is disabled and active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_disabled_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_disabled_on'.
    '''

    def on_state(self, instance, value):
        if value == 'down':
            self.active = True
        else:
            self.active = False

    def _toggle_active(self):
        self._do_press()

    def on_active(self, instance, value):
        self.state = 'down' if value else 'normal'
