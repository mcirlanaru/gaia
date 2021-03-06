# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette import Wait
from marionette.by import By
from marionette import expected

from gaiatest.apps.base import Base


class AttachmentOptions(Base):

    _attachment_options_locator = (By.CSS_SELECTOR, '#attachment-options[data-type="action"]')
    _view_button_locator = (By.ID, 'attachment-options-view')
    _header_locator = (By.CSS_SELECTOR, '.current gaia-header')
    _cancel_button_locator = (By.ID, 'attachment-options-cancel')

    def __init__(self, marionette):
        Base.__init__(self, marionette)
        Wait(self.marionette).until(lambda m:
                                    m.find_element(*self._attachment_options_locator).location['y'] == 0)

    def tap_cancel(self):
        self.marionette.find_element(*self._cancel_button_locator).tap()
        Wait(self.marionette).until(expected.element_not_displayed(
            Wait(self.marionette).until(expected.element_present(*self._attachment_options_locator))))

    def tap_view_button(self):
        self.marionette.find_element(*self._view_button_locator).tap()
        from gaiatest.apps.gallery.regions.view_image import ViewImage
        return ViewImage(self.marionette)
