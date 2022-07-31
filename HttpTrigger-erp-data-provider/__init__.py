import logging

import azure.functions as func

import json

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from sap_hr_personnel_calculation_schema_data_provider import SapHrPersonnelCalculationSchemaDataProvider

from time import perf_counter_ns


def main(req: func.HttpRequest) -> func.HttpResponse:
    start_time = perf_counter_ns()
    logging.info('Python HTTP trigger function processed a request.')

    data_provider = SapHrPersonnelCalculationSchemaDataProvider()

    end_time = perf_counter_ns()

    res = {
        "elapsed_time": (end_time - start_time) / 1000000000,
        "request": {
            "method": req.method,
            "url": req.url,
            "headers": {k: v for k, v in req.headers.items()},
            "params": {k: v for k, v in req.params.items()},
            "route_params": {k: v for k, v in req.route_params.items()},
        },
        "data": data_provider.data
    }

    if req.method in ['POST', 'PUT', 'PATCH']:
        res['request']['body'] = req.get_json()

    if data_provider.data:
        return func.HttpResponse(json.dumps(res), status_code=200, mimetype='application/json', charset='utf-8', headers={'Content-Type': 'application/json'})
    else:
        return func.HttpResponse(json.dumps(res), status_code=500, mimetype='application/json', charset='utf-8', headers={'Content-Type': 'application/json'})
