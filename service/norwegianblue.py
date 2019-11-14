import os

from flask import Flask, request, jsonify, Response, abort

from sesamutils import sesam_logger, VariablesConfig
from sesamutils.flask import serve

# required_env_vars = ["SUBDOMAIN"]
# optional_env_vars = ["DEBUG", "LOG_LEVEL", ["API_ROOT","/"]] # Default values can be given to optional environment variables by the use of tuples

app = Flask(__name__)

logger = sesam_logger('norwegianblue', app=app, timestamp=True)

@app.route('/<path:txt>', methods=['GET','PUT','POST','DELETE','PATCH','COPY'])
def get_generic(txt):
    returnList = []
    returnDict = {'Hello': f'Polly wants a cracker'}
    returnDict['path'] = txt
    returnList.append(returnDict)
    return jsonify(returnList) , 200, {"Content-Type": "application/json"}

if __name__ == "__main__":
    # config = VariablesConfig(required_env_vars, optional_env_vars=optional_env_vars)
    # if not config.validate():
    #     os.sys.exit(1)

    serve(app)