from flask import Flask, request, jsonify
from .lib import daterange, InMemoryDateStatCache, get_data_from_cache

app = Flask(__name__)


cache = InMemoryDateStatCache()

@app.route('/')
def entrypoint():
    start_date = request.args.get('start_date', '2018-10-12')
    end_date = request.args.get('end_date', '2018-11-12')

    result = get_data_from_cache(cache, start_date, end_date)

    return jsonify(result)
