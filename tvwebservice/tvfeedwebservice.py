##
#        File: tvfeedwebservice.py
#     Created: 11/10/2020
#     Updated: 11/18/2020
#  Programmer: Cuates
#  Updated By: Cuates
#     Purpose: TV feed web service
#     Version: 0.0.1 Python3
##

# Import modules
from flask import Flask, request, jsonify # Flask, request, jsonify
from flask_restful import Api # flask_restful, api
import json # json
import tvfeedwebserviceclass # tv feed web service class
from tvfeedclass import TVFeedClass # tv feed web service class
from tvfeedtitleshortclass import TVFeedTitleShortClass # tv feed title short web service class
from tvfeedtitleshortactionstatusclass import TVFeedTitleShortActionStatusClass # tv feed title short action status web service class

# Create objects
app = Flask(__name__)
api = Api(app)

# Set object
tfwsclass = tvfeedwebserviceclass.TVFeedWebServiceClass()

# try to execute the command(s)
try:
  # Error handler
  @app.errorhandler(Exception)
  def errorHandling(eh):
    # Initialize variables
    messageVal = ''
    codeVal = 500

    # try to execute the command(s)
    try:
      # Set message
      messageVal = str(eh.code) + ' ' + str(eh.name) + ' ' + str(eh.description)

      # Set code
      codeVal = eh.code
    # Catch exceptions
    except Exception as e:
      # Set message
      messageVal = 'ErrorHandler'

      # Log message
      tfwsclass._setLogger('ErrorHandler ' + str(e))

    # Return message
    return {'Status': 'Error', 'Message': messageVal, 'Count': 0, 'Result': []}, codeVal

  # Store possible methods
  validMethods = ['GET', 'POST', 'PUT', 'DELETE']

  # Before request
  @app.before_request
  def before_request_func():
    # Check if request method is in the list
    if request.method not in validMethods:
      # Return message
      return {'Status': 'Error', 'Message': 'Method invalid or not implemented', 'Count': 0, 'Result': []}, 501

  # Add resource for api web service call tv feed
  api.add_resource(TVFeedClass, '/api/tvfeed', methods = validMethods)

  # Add resource for additional api web service call tv feed title short
  api.add_resource(TVFeedTitleShortClass, '/api/tvfeed/titleshort', methods = ['PUT', 'DELETE'])

  # Add resource for additional api web service call tv feed title short action status
  api.add_resource(TVFeedTitleShortActionStatusClass, '/api/tvfeed/titleshortactionstatus', methods = ['PUT'])
# Catch exceptions
except Exception as e:
  # Log message
  tfwsclass._setLogger('Issue executing main PY file ' + str(e))

# Run program
if __name__ == '__main__':
  # Run app
  app.run(host='127.0.0.1', port=4817, debug=True, threaded=True)