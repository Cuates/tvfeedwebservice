##
#        File: tvfeedtitleshortactionstatusclass.py
#     Created: 11/10/2020
#     Updated: 11/14/2020
#  Programmer: Cuates
#  Updated By: Cuates
#     Purpose: TV feed title short action status web service
#     Version: 0.0.1 Python3
##

# Import modules
import tvfeedwebserviceclass # tv feed web service class
from flask import Flask, request, jsonify # Flask, request, jsonify
from flask_restful import Resource #Api # flask_restful, api, resource
import json # json

# Class
class TVFeedTitleShortActionStatusClass(Resource):
  # Constructor
  def __init__(self):
    pass

  # Get method
  def get(self):
    # Initialize list, dictionary, and variables
    resultDict = {}
    returnDict = {}
    codeVal = 200

    # Create object of tv feed web service class
    tfwsclass = tvfeedwebserviceclass.TVFeedWebServiceClass()

    # try to execute the command(s)
    try:
      # Store headers
      wsHead = dict(request.headers)

      # Set variable
      #reqPath = request.path

      # Check if headers were provided
      webserviceHeaderResponse = tfwsclass._checkHeaders(wsHead)

      # Check if element exists
      if webserviceHeaderResponse.get('Status') != None:
        # Check if status is success
        if webserviceHeaderResponse['Status'] == 'Success':
          # Set list
          mandatoryParams = []

          # Check payload
          payloadResponse = tfwsclass._checkPayload(request.method, request.args, mandatoryParams)

          # Check if element exists
          if payloadResponse.get('Status') != None:
            # Check if status is success
            if payloadResponse['Status'] == 'Success':
              # Initialize list
              possibleParams = ['titlelong', 'titleshort', 'actionnumber', 'limit', 'sort']

              # Extract tv feed
              #resultDict = tfwsclass._extractTVFeed('MariaDBSQLTV', 'extracting', 'dbo.extractMediaFeed', 'extractTVFeed', possibleParams, payloadResponse['Result'])
              #resultDict = tfwsclass._extractTVFeed('PGSQLTV', 'extracting', 'dbo.extractMediaFeed', 'extractTVFeed', possibleParams, payloadResponse['Result'])
              #resultDict = tfwsclass._extractTVFeed('MSSQLLTV', 'extracting', 'dbo.extractMediaFeed', 'extractTVFeed', possibleParams, payloadResponse['Result'])
              resultDict = tfwsclass._extractTVFeed('MSSQLWTV', 'extracting', 'dbo.extractMediaFeed', 'extractTVFeed', possibleParams, payloadResponse['Result'])

              # Check if there is data
              if resultDict:
                # Loop through sub elements
                for systemEntries in resultDict:
                  # Check if elements exists
                  if systemEntries.get('SError') == None:
                      # Store Message
                      returnDict = {'Status': 'Success', 'Message': 'Processed request', 'Count': len(resultDict), 'Result': resultDict}
                  else:
                    # Store Message
                    returnDict = {'Status': systemEntries['SError'], 'Message': systemEntries['SMessage'], 'Count': 0, 'Result': []}

                    # Set code
                    codeVal = 500

                    # Break out of loop
                    break
              else:
                # Store Message
                returnDict = {'Status': 'Success', 'Message': 'Processed request', 'Count': 0, 'Result': []}
            else:
              # Store Message
              returnDict = {'Status': payloadResponse['Status'], 'Message': payloadResponse['Message'], 'Count': 0, 'Result': []}

              # Store code
              codeVal = 400
          else:
            # Store Message
            returnDict = {'Status': 'Error', 'Message': 'Issue with payload check', 'Count': 0, 'Result': []}

            # Store code
            codeVal = 400
        else:
          # Store Message
          returnDict = {'Status': webserviceHeaderResponse['Status'], 'Message': webserviceHeaderResponse['Message'], 'Count': 0, 'Result': []}

          # Store code
          codeVal = 400
      else:
        # Store Message
        returnDict = {'Status': 'Error', 'Message': 'Issue with header check', 'Count': 0, 'Result': []}

        # Store code
        codeVal = 400
    # Catch exceptions
    except Exception as e:
      # Store Message
      returnDict = {'Status': 'Error', 'Message': 'GET not implemented properly', 'Count': 0, 'Result': []}

      # Log message
      tfwsclass._setLogger('GET ' + str(e))

    # Return dictionary with code
    return returnDict, codeVal

  # Post method
  def post(self):
    # Initialize list, dictionary, and variables
    resultDict = {}
    returnDict = {}
    codeVal = 200

    # Create object of tv feed web service class
    tfwsclass = tvfeedwebserviceclass.TVFeedWebServiceClass()

    # try to execute the command(s)
    try:
      # Store headers
      wsHead = dict(request.headers)

      # Set variable
      #reqPath = request.path

      # Check if headers were provided
      webserviceHeaderResponse = tfwsclass._checkHeaders(wsHead)

      # Check if element exists
      if webserviceHeaderResponse.get('Status') != None:
        # Check if status is success
        if webserviceHeaderResponse['Status'] == 'Success':
          # Set list
          mandatoryParams = ['titlelong', 'titleshort', 'publishdate', 'actionstatus']

          # Check payload
          payloadResponse = tfwsclass._checkPayload(request.method, request.data, mandatoryParams)

          # Check if element exists
          if payloadResponse.get('Status') != None:
            # Check if status is success
            if payloadResponse['Status'] == 'Success':
              # Initailize list
              possibleParams = ['titlelong', 'titleshort', 'publishdate', 'actionstatus']

              # Insert tv feed
              #resultDict = tfwsclass._insertupdatedeleteTVFeed('MariaDBSQLTV', 'inserting', 'insertupdatedeletemediafeed', 'insertTVFeed', possibleParams, payloadResponse['Result'])
              #resultDict = tfwsclass._insertupdatedeleteTVFeed('PGSQLTV', 'inserting', 'insertupdatedeletemediafeed', 'insertTVFeed', possibleParams, payloadResponse['Result'])
              #resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLLTV', 'inserting', 'dbo.insertupdatedeleteMediaFeed', 'insertTVFeed', possibleParams, payloadResponse['Result'])
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLWTV', 'inserting', 'dbo.insertupdatedeleteMediaFeed', 'insertTVFeed', possibleParams, payloadResponse['Result'])

              # Loop through sub elements
              for systemEntries in resultDict:
                # Check if elements exists
                if systemEntries.get('SError') == None:
                  # Store Message
                  returnDict = {'Status': 'Success', 'Message': 'Processed request)', 'Count': len(resultDict), 'Result': resultDict}
                else:
                  # Store Message
                  returnDict = {'Status': systemEntries['SError'], 'Message': systemEntries['SMessage'], 'Count': 0, 'Result': []}

                  # Break out of loop
                  break
            else:
              # Store Message
              returnDict = {'Status': payloadResponse['Status'], 'Message': payloadResponse['Message'], 'Count': 0, 'Result': []}

              # Store code
              codeVal = 400
          else:
            # Store Message
            returnDict = {'Status': 'Error', 'Message': 'Issue with payload check', 'Count': 0, 'Result': []}

            # Store code
            codeVal = 400
        else:
          # Store Message
          returnDict = {'Status': webserviceHeaderResponse['Status'], 'Message': webserviceHeaderResponse['Message'], 'Count': 0, 'Result': []}
      else:
        # Store Message
        returnDict = {'Status': 'Error', 'Message': 'Issue with header check', 'Count': 0, 'Result': []}
    # Catch exceptions
    except Exception as e:
      # Store Message
      returnDict = {'Status': 'Error', 'Message': 'POST not implemented properly', 'Count': 0, 'Result': []}

      # Set code
      codeVal = 500

      # Log message
      tfwsclass._setLogger('POST ' + str(e))

    # Return dictionary with code
    return returnDict, codeVal

  # Put method
  def put(self):
    # Initialize list, dictionary, and variables
    resultDict = {}
    returnDict = {}
    codeVal = 200

    # Create object of tv feed web service class
    tfwsclass = tvfeedwebserviceclass.TVFeedWebServiceClass()

    # try to execute the command(s)
    try:
      # Store headers
      wsHead = dict(request.headers)

      ## Set variable
      #reqPath = request.path

      # Check if headers were provided
      webserviceHeaderResponse = tfwsclass._checkHeaders(wsHead)

      # Check if element exists
      if webserviceHeaderResponse.get('Status') != None:
        # Check if status is success
        if webserviceHeaderResponse['Status'] == 'Success':
          # Set list
          mandatoryParams = ['titleshort', 'actionstatus']

          # Check payload
          payloadResponse = tfwsclass._checkPayload(request.method, request.data, mandatoryParams)

          # Check if element exists
          if payloadResponse.get('Status') != None:
            # Check if status is success
            if payloadResponse['Status'] == 'Success':
              # Initailize list
              possibleParams = ['titleshort', 'actionstatus']

              # Update tv feed
              #resultDict = tfwsclass._insertupdatedeleteTVFeed('MariaDBSQLTV', 'updating', 'insertupdatedeletemediafeed', 'updateTVFeedTitleShortActionStatus', possibleParams, payloadResponse['Result'])
              #resultDict = tfwsclass._insertupdatedeleteTVFeed('PGSQLTV', 'updating', 'insertupdatedeletemediafeed', 'updateTVFeedTitleShortActionStatus', possibleParams, payloadResponse['Result'])
              #resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLLTV', 'updating', 'dbo.insertupdatedeleteMediaFeed', 'updateTVFeedTitleShortActionStatus', possibleParams, payloadResponse['Result'])
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLWTV', 'updating', 'dbo.insertupdatedeleteMediaFeed', 'updateTVFeedTitleShortActionStatus', possibleParams, payloadResponse['Result'])

              # Loop through sub elements
              for systemEntries in resultDict:
                # Check if elements exists
                if systemEntries.get('SError') == None:
                  # Store Message
                  returnDict = {'Status': 'Success', 'Message': 'Processed request', 'Count': len(resultDict), 'Result': resultDict}
                else:
                  # Store Message
                  returnDict = {'Status': systemEntries['SError'], 'Message': systemEntries['SMessage'], 'Count': 0, 'Result': []}

                  # Break out of loop
                  break
            else:
              # Store Message
              returnDict = {'Status': payloadResponse['Status'], 'Message': payloadResponse['Message'], 'Count': 0, 'Result': []}

              # Store code
              codeVal = 400
          else:
            # Store Message
            returnDict = {'Status': 'Error', 'Message': 'Issue with payload check', 'Count': 0, 'Result': []}

            # Store code
            codeVal = 400
        else:
          # Store Message
          returnDict = {'Status': webserviceHeaderResponse['Status'], 'Message': webserviceHeaderResponse['Message'], 'Count': 0, 'Result': []}
      else:
        # Store Message
        returnDict = {'Status': 'Error', 'Message': 'Issue with header check', 'Count': 0, 'Result': []}
    # Catch exceptions
    except Exception as e:
      # Store Message
      returnDict = {'Status': 'Error', 'Message': 'PUT not implemented properly', 'Count': 0, 'Result': []}

      # Set code
      codeVal = 500

      # Log message
      tfwsclass._setLogger('PUT ' + str(e))

    # Return dictionary with code
    return returnDict, codeVal

  # Delete method
  def delete(self):
    # Initialize list, dictionary, and variables
    resultDict = {}
    returnDict = {}
    codeVal = 200

    # Create object of tv feed web service class
    tfwsclass = tvfeedwebserviceclass.TVFeedWebServiceClass()

    # try to execute the command(s)
    try:
      # Store headers
      wsHead = dict(request.headers)

      ## Set variable
      #reqPath = request.path

      # Check if headers were provided
      webserviceHeaderResponse = tfwsclass._checkHeaders(wsHead)

      # Check if element exists
      if webserviceHeaderResponse.get('Status') != None:
        # Check if status is success
        if webserviceHeaderResponse['Status'] == 'Success':
          # Set list
          mandatoryParams = ['titleshort']

          # Check payload
          payloadResponse = tfwsclass._checkPayload(request.method, request.data, mandatoryParams)

          # Check if element exists
          if payloadResponse.get('Status') != None:
            # Check if status is success
            if payloadResponse['Status'] == 'Success':
              # Initailize list
              possibleParams = ['titleshort']

              # Delete tv feed
              #resultDict = tfwsclass._insertupdatedeleteTVFeed('MariaDBSQLTV', 'deleting', 'insertupdatedeletemediafeed', 'updateTVFeedTitleShort', possibleParams, payloadResponse['Result'])
              #resultDict = tfwsclass._insertupdatedeleteTVFeed('PGSQLTV', 'deleting', 'insertupdatedeletemediafeed', 'updateTVFeedTitleShort', possibleParams, payloadResponse['Result'])
              #resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLLTV', 'deleting', 'dbo.insertupdatedeleteMediaFeed', 'updateTVFeedTitleShort', possibleParams, payloadResponse['Result'])
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLWTV', 'deleting', 'dbo.insertupdatedeleteMediaFeed', 'updateTVFeedTitleShort', possibleParams, payloadResponse['Result'])

              # Loop through sub elements
              for systemEntries in resultDict:
                # Check if elements exists
                if systemEntries.get('SError') == None:
                  # Store Message
                  returnDict = {'Status': 'Success', 'Message': 'Processed request', 'Count': len(resultDict), 'Result': resultDict}
                else:
                  # Store Message
                  returnDict = {'Status': systemEntries['SError'], 'Message': systemEntries['SMessage'], 'Count': 0, 'Result': []}

                  # Break out of loop
                  break
            else:
              # Store Message
              returnDict = {'Status': payloadResponse['Status'], 'Message': payloadResponse['Message'], 'Count': 0, 'Result': []}

              # Store code
              codeVal = 400
          else:
            # Store Message
            returnDict = {'Status': 'Error', 'Message': 'Issue with payload check', 'Count': 0, 'Result': []}

            # Store code
            codeVal = 400
        else:
          # Store Message
          returnDict = {'Status': webserviceHeaderResponse['Status'], 'Message': webserviceHeaderResponse['Message'], 'Count': 0, 'Result': []}
      else:
        # Store Message
        returnDict = {'Status': 'Error', 'Message': 'Issue with header check', 'Count': 0, 'Result': []}
    # Catch exceptions
    except Exception as e:
      # Store Message
      returnDict = {'Status': 'Error', 'Message': 'DELETE not implemented properly', 'Count': 0, 'Result': []}

      # Set code
      codeVal = 500

      # Log message
      tfwsclass._setLogger('DELETE ' + str(e))

    # Return dictionary with code
    return returnDict, codeVal