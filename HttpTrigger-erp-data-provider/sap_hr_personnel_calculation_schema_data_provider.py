#!/usr/bin/env python

import os
import sys
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/data/sap/hr/personnel_calculation_schema')
import data


class SapHrPersonnelCalculationSchemaDataProvider(object):
    def __init__(self) -> None:
        self.data = data.data

    def get_data_in_json(self, indent=None) -> str:
        return json.dumps(self.data, ensure_ascii=False, indent=indent)


if __name__ == '__main__':
    data_provider = SapHrPersonnelCalculationSchemaDataProvider()
    print(data_provider.get_data_in_json(indent=2))
