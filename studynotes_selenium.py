# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author  : zlbd


class DialogAddTagXXX(object):

    def __init__(self): 
        pass

    def get_grid_bodies(self, locator):
            """
            :param locator: tuple. eg: ("By.XPATH", r"//ag-grid-angular[@id='myGrid']" layer)
            :return bodies: list.
            """
            # step1:
            # Get locator.
            body_locator = (locator[0], locator[1] + r"//div[contains(@class, 'ag-center-cols-container')]/div")
            # step2:
            # Get body elements.
            elements = self.common.find_elements(body_locator)
            # step3:
            # Get bodies text.
            if len(elements) == 0:
                return []
            else:
                bodies = []
                for _line in elements:
                    _div_index = int(elements.index(_line)) + 1
                    _line_locator = (locator[0], body_locator[1] + "/../div[%s]/div" % _div_index)
                    _line_subelements = self.common.find_elements(_line_locator)
                    _line_items = [_ele.text for _ele in _line_subelements]
                    bodies.append(_line_items)
                return bodies

        def get_grid_datalist(self, locator):
            """
            :param locator: tuple. eg: ("By.XPATH", r"//ag-grid-angular[@id='myGrid']" layer)
            :return _datalist: list.
            """
            # step1:
            # Get grid headers.
            headers = self.get_grid_headers(locator)
            # step2:
            # Get grid bodies.
            bodies = self.get_grid_bodies(locator)
            # step3:
            # Get grid datalist.
            datalist = []
            for body in bodies:
                _dict = {}
                for head in headers:
                    _index = headers.index(head)
                    _dict[head] = body[_index]
                datalist.append(_dict)
            return datalist

        def select_row_by_index(self, locator, index):
            """
            Select row checkbox by index.
            :param locator: tuple. eg: ("By.XPATH", r"<span[@class='ag-selection-checkbox']> layer")
            :param index: int. start from 1.
            :return:
            """
            # step1:
            # Get locator.
            with_index_locator = (locator[0], locator[1] % index)
            status_locator = (with_index_locator[0], with_index_locator[1] + r'//input')
            # step2:
            # Select row checkbox.
            status = self.common.find_element(status_locator).is_selected()
            if not status:
                self.common.click_element(locator)

        def get_visible_bodies_from_tagXXX_grid(self):
            """
            Get visible bodies from 'tagXXX' grid.
            """
            # step1:
            # Get locator.
            _grid_tagXXX_locator = self.Dialog_AT_Pane.grid_tagXXX()
            # step2:
            # Get tags browsed.
            grid_bodies = self.GridActor.get_grid_bodies(_grid_tagXXX_locator)
            return grid_bodies
