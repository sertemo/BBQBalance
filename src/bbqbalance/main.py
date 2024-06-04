# Copyright 2024 Sergio Tejedor Moreno

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Script principal"""

import flet as ft


class BBQApp(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        pass


def main(page: ft.Page):
    """Entrypoint

    Parameters
    ----------
    page : ft.Page
        _description_
    """

    page.title = "BBQ Balance"
    page.padding = 0
    page.theme = ft.Theme(font_family="Nunito")
    page.theme.page_transitions.windows = "cupertino"
    page.bgcolor = ft.colors.BLUE_GREY_200
    app = BBQApp()
    page.add(app)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
