import os
from datetime import datetime

from flask import Flask, request, jsonify, Response, abort

from sesamutils import sesam_logger, VariablesConfig
from sesamutils.flask import serve

from collections import OrderedDict

required_env_vars = ["SUBDOMAIN"]
optional_env_vars = ["DEBUG", "LOG_LEVEL", ("API_ROOT","/")] # Default values can be given to optional environment variables by the use of tuples
config = VariablesConfig(required_env_vars, optional_env_vars=optional_env_vars)

app = Flask(__name__)

logger = sesam_logger('norwegianblue', app=app, timestamp=True)

@app.route('/<path:txt>', methods=['GET','PUT','POST','DELETE','PATCH','COPY'])
def get_generic(txt):
    returnList = []
    returnDict = OrderedDict()
    returnDict['Hello'] = f'Polly wants a cracker {datetime.now()}'
    returnDict['base_url']= request.base_url
    returnDict['http_method'] = request.method
    returnDict['path'] = txt
    returnDict['args'] = request.args
    # returnDict['header_keys'] = request.headers.keys()
    returnDict['DEBUG'] = config.DEBUG
    # returnDict['Authorization'] = request.headers.get('Authorization')
    if request.is_json:
        returnDict['payload'] = request.json
    else:
        returnDict['payload'] = [str(data) for data in request.data]
    returnList.append(returnDict)
    return jsonify(returnList) , 200, {"Content-Type": "application/json"}

if __name__ == "__main__":
    # 
    # if not config.validate():
    #     os.sys.exit(1)

    serve(app)