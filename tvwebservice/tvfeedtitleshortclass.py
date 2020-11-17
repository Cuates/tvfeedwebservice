##
#        File: tvfeedtitleshortclass.py
#     Created: 11/10/2020
#     Updated: 11/17/2020
#  Programmer: Cuates
#  Updated By: Cuates
#     Purpose: TV feed title short web service
#     Version: 0.0.1 Python3
##

# Import modules
import tvfeedwebserviceclass # tv feed web service class
from flask import Flask, request, jsonify # Flask, request, jsonify
from flask_restful import Resource #Api # flask_restful, api, resource
import json # json

# Class
class TVFeedTitleShortClass(Resource):
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
              # Set variable
              statusVal = 'Success'
              messageVal = 'Processed request'
              selectColumn = 'select titlelongreturn as "Title Long", titleshortreturn as "Title Short", publishdatereturn as "Publish Date", actionstatusreturn as "Action Status"'

              # Initialize list
              possibleParams = ['titlelong', 'titleshort', 'actionstatus', 'limit', 'sort']

              # Extract tv feed
              resultDict = tfwsclass._extractTVFeed('MariaDBSQLTV', 'extracting', '', 'extractmediafeed', 'extractTVFeed', possibleParams, payloadResponse['Result'])
              resultDict = tfwsclass._extractTVFeed('PGSQLTV', 'extracting', selectColumn, 'extractmediafeed', 'extractTVFeed', possibleParams, payloadResponse['Result'])
              resultDict = tfwsclass._extractTVFeed('MSSQLLTV', 'extracting', '', 'dbo.extractMediaFeed', 'extractTVFeed', possibleParams, payloadResponse['Result'])
              resultDict = tfwsclass._extractTVFeed('MSSQLWTV', 'extracting', '', 'dbo.extractMediaFeed', 'extractTVFeed', possibleParams, payloadResponse['Result'])

              # Check if there is data
              if resultDict:
                # Loop through sub elements
                for systemEntries in resultDict:
                  # Check if elements exists
                  if systemEntries.get('SError') != None:
                    # Store status value
                    statusVal = systemEntries['SError']

                    # Store message value
                    messageVal = systemEntries['SMessage']

                    # Set code
                    codeVal = 500

                    # Break out of loop
                    break

                # Check if status value is success
                if statusVal == 'Success':
                  # Store Message
                  returnDict = {'Status': statusVal, 'Message': messageVal, 'Count': len(resultDict), 'Result': resultDict}
                else:
                  # Store Message
                  returnDict = {'Status': statusVal, 'Message': messageVal, 'Count': 0, 'Result': []}
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
              # Set variable
              statusVal = 'Success'
              messageVal = 'Processed request'

              # Initailize list
              possibleParams = ['titlelong', 'titleshort', 'titleshortold', 'publishdate', 'actionstatus']
              removeParams = ['titleshortold']

              # Insert tv feed
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MariaDBSQLTV', 'inserting', 'insertupdatedeletemediafeed', 'insertTVFeed', possibleParams, payloadResponse['Result'], removeParams)
              resultDict = tfwsclass._insertupdatedeleteTVFeed('PGSQLTV', 'inserting', 'insertupdatedeletemediafeed', 'insertTVFeed', possibleParams, payloadResponse['Result'], removeParams)
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLLTV', 'inserting', 'dbo.insertupdatedeleteMediaFeed', 'insertTVFeed', possibleParams, payloadResponse['Result'], removeParams)
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLWTV', 'inserting', 'dbo.insertupdatedeleteMediaFeed', 'insertTVFeed', possibleParams, payloadResponse['Result'], removeParams)

              # Loop through sub elements
              for systemEntries in resultDict:
                # Check if elements exists
                if systemEntries.get('SError') != None:
                  # Store status value
                  statusVal = systemEntries['SError']

                  # Store message value
                  messageVal = systemEntries['SMessage']

                  # Set code
                  codeVal = 500

                  # Break out of the loop
                  break

              if statusVal == 'Success':
                # Store Message
                returnDict = {'Status': statusVal, 'Message': messageVal, 'Count': len(resultDict), 'Result': resultDict}
              else:
                # Store Message
                returnDict = {'Status': statusVal, 'Message': messageVal, 'Count': 0, 'Result': []}
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
          mandatoryParams = ['titleshort', 'titleshortold']

          # Check payload
          payloadResponse = tfwsclass._checkPayload(request.method, request.data, mandatoryParams)

          # Check if element exists
          if payloadResponse.get('Status') != None:
            # Check if status is success
            if payloadResponse['Status'] == 'Success':
              # Set variable
              statusVal = 'Success'
              messageVal = 'Processed request'

              # Initailize list
              possibleParams = ['titlelong', 'titleshort', 'titleshortold', 'publishdate', 'actionstatus']
              removeParams = ['titlelong', 'publishdate', 'actionstatus']

              # Update tv feed
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MariaDBSQLTV', 'updating', 'insertupdatedeletemediafeed', 'updateTVFeedTitleShort', possibleParams, payloadResponse['Result'], removeParams)
              resultDict = tfwsclass._insertupdatedeleteTVFeed('PGSQLTV', 'updating', 'insertupdatedeletemediafeed', 'updateTVFeedTitleShort', possibleParams, payloadResponse['Result'], removeParams)
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLLTV', 'updating', 'dbo.insertupdatedeleteMediaFeed', 'updateTVFeedTitleShort', possibleParams, payloadResponse['Result'], removeParams)
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLWTV', 'updating', 'dbo.insertupdatedeleteMediaFeed', 'updateTVFeedTitleShort', possibleParams, payloadResponse['Result'], removeParams)

              # Loop through sub elements
              for systemEntries in resultDict:
                # Check if elements exists
                if systemEntries.get('SError') != None:
                  # Store status value
                  statusVal = systemEntries['SError']

                  # Store message value
                  messageVal = systemEntries['SMessage']

                  # Set code
                  codeVal = 500

                  # Break out of the loop
                  break

              if statusVal == 'Success':
                # Store Message
                returnDict = {'Status': statusVal, 'Message': messageVal, 'Count': len(resultDict), 'Result': resultDict}
              else:
                # Store Message
                returnDict = {'Status': statusVal, 'Message': messageVal, 'Count': 0, 'Result': []}
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
              # Set variable
              statusVal = 'Success'
              messageVal = 'Processed request'

              # Initailize list
              possibleParams = ['titlelong', 'titleshort', 'titleshortold', 'publishdate', 'actionstatus']
              removeParams = ['titlelong', 'titleshortold', 'publishdate', 'actionstatus']

              # Delete tv feed
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MariaDBSQLTV', 'deleting', 'insertupdatedeletemediafeed', 'deleteTVFeedTitleShort', possibleParams, payloadResponse['Result'], removeParams)
              resultDict = tfwsclass._insertupdatedeleteTVFeed('PGSQLTV', 'deleting', 'insertupdatedeletemediafeed', 'deleteTVFeedTitleShort', possibleParams, payloadResponse['Result'], removeParams)
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLLTV', 'deleting', 'dbo.insertupdatedeleteMediaFeed', 'deleteTVFeedTitleShort', possibleParams, payloadResponse['Result'], removeParams)
              resultDict = tfwsclass._insertupdatedeleteTVFeed('MSSQLWTV', 'deleting', 'dbo.insertupdatedeleteMediaFeed', 'deleteTVFeedTitleShort', possibleParams, payloadResponse['Result'], removeParams)

              # Loop through sub elements
              for systemEntries in resultDict:
                # Check if elements exists
                if systemEntries.get('SError') != None:
                  # Store status value
                  statusVal = systemEntries['SError']

                  # Store message value
                  messageVal = systemEntries['SMessage']

                  # Set code
                  codeVal = 500

                  # Break out of the loop
                  break

              if statusVal == 'Success':
                # Store Message
                returnDict = {'Status': statusVal, 'Message': messageVal, 'Count': len(resultDict), 'Result': resultDict}
              else:
                # Store Message
                returnDict = {'Status': statusVal, 'Message': messageVal, 'Count': 0, 'Result': []}
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