import logging
import os
if os:
    try:
        os.remove("launcher.log")
    except:
        pass

import sys
if sys:
    logging.basicConfig(filename="launcher.log", level=logging.INFO)


from versa_webapp.wp_csvdata_input import wp_csvdata_input
from versa_webapp.wp_csv_schema_metadata import wp_csv_schema_metadata

import justpy as jp
from addict import Dict
from tracker import _hcs as stubStore, refBoard, session_dict

from versa_webapp.model_backend_actions import CSV_URL_INPUT

#app = jp.app
#jp.justpy(wp_csvdata_input, start_server=False)
# wp = wp_csvdata_input(None)

# # print(stubStore.inputctx.form)
# msg = Dict()
# msg.page = wp
# wp.model = Dict(track_changes=True)
# stubStore.inputctx.csvurl.target.setValue(
#     'https://query.data.world/s/rgz7coxjf2iutihqhbc2xybqkuhcxf')

# stubStore.inputctx.csvurl.target.setValue(
#     'http://192.168.0.183:9000/airport_to_counties.csv')
# stubStore.inputctx.form.target.on_submit(msg)

# to prepare for csv metadata page

CSV_URL_INPUT(session_dict.model, Dict({'url': 'http://192.168.0.183:9000/airport_to_counties.csv'})
              )

#wp = wp_csv_schema_metadata(None)

app = jp.app
jp.justpy(wp_csv_schema_metadata, start_server=False)
