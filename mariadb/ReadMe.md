# MariaDB Function, Index, Stored Procedure, Table, and or View
> MariaDB database schema for this project

## Table of Contents
* [Important Note](#important-note)
* [Stored Procedure Usage](#stored-procedure-usage)

### **Important Note**
* This project was written with MariaDB 10 methods

### Stored Procedure Usage
* `call extractmediafeed ('extractActionStatus', 'actionNumberValue', 'actionDescription', '', '', '', '', '', '', '', '', '', 'limitValue', 'sortValue')`
* `call extractmediafeed ('extractMediaAudioEncode', '', '', 'audioEncodeValue', '', '', '', '', '', '', '', '', 'limitValue', 'sortValue')`
* `call extractmediafeed ('extractMediaDynamicRange', '', '', '', 'dynamicRangeValue', '', '', '', '', '', '', '', 'limitValue', 'sortValue')`
* `call extractmediafeed ('extractMediaResolution', '', '', '', '', 'resolutionValue', '', '', '', '', '', '', 'limitValue', 'sortValue')`
* `call extractmediafeed ('extractMediaStreamSource', '', '', '', '', '', 'streamSourceValue', 'streamDescriptionValue', '', '', '', '', 'limitValue', 'sortValue')`
* `call extractmediafeed ('extractMediaVideoEncode', '', '', '', '', '', '', '', 'videoEncodeValue', '', '', '', 'limitValue', 'sortValue')`
* `call extractmediafeed ('extractMovieFeed', '', '', '', '', '', '', '', '', 'titleLongValue', 'titleShortValue', 'actionStatusValue', '', 'limitValue', 'sortValue')`
* `call extractmediafeed ('extractTVFeed', '', '', '', '', '', '', '', '', 'titleLongValue', 'titleShortValue', 'actionStatusValue', '', 'limitValue', 'sortValue')`
* `call insertupdatedeletemediafeed ('deleteActionStatus', 'actionNumberValue', '', '', '', '', '', '', '', '', '', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('deleteMediaAudioEncode', '', '', 'audioEncodeValue', '', '', '', '', '', '', '', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('deleteMediaDynamicRange', '', '', '', 'dynamicRangeValue', '', '', '', '', '', '', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('deleteMediaResolution', '', '', '', '', 'resolutionValue', '', '', '', '', '', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('deleteMediaStreamSource', '', '', '', '', '', 'streamSourceValue', '', '', '', '', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('deleteMediaVideoEncode', '', '', '', '', '', '', '', 'videoEncode', '', '', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('deleteMovieFeed', '', '', '', '', '', '', '', '', 'titleLongValue', '', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('deleteMovieFeedTitleShort', '', '', '', '', '', '', '', '', '', 'titleShortValue', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('deleteTVFeed', '', '', '', '', '', '', '', '', 'titleLongValue', '', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('deleteTVFeedTitleShort', '', '', '', '', '', '', '', '', '', 'titleShortValue', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('insertActionStatus', 'actionNumberValue', 'actionDescriptionValue', '', '', '', '', '', '', '', '', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('insertMediaAudioEncode', '', '', 'audioEncodeValue', '', '', '', '', '', '', '', '', '', '', 'movieIncludeValue', 'tvIncludeValue')`
* `call insertupdatedeletemediafeed ('insertMediaDynamicRange', '', '', '', 'dynamicRangeValue', '', '', '', '', '', '', '', '', '', 'movieIncludeValue', 'tvIncludeValue')`
* `call insertupdatedeletemediafeed ('insertMediaResolution', '', '', '', '', '', 'resolutionValue', '', '', '', '', '', '', '', '', 'movieIncludeValue', 'tvIncludeValue')`
* `call insertupdatedeletemediafeed ('insertMediaStreamSource', '', '', '', '', '', '', 'streamSourceValue', 'streamDescriptionValue', '', '', '', '', '', 'movieIncludeValue', 'tvIncludeValue')`
* `call insertupdatedeletemediafeed ('insertMediaVideoEncode', '', '', '', '', '', '', '', '', 'videoEncodeValue', '', '', '', '', 'movieIncludeValue', 'tvIncludeValue')`
* `call insertupdatedeletemediafeed ('insertMovieFeed', '', '', '', '', '', '', '', 'titleLongValue', 'titleShortValue', '', 'publishDateValue', 'actionStatusValue', '', '', '')`
* `call insertupdatedeletemediafeed ('insertTVFeed', '', '', '', '', '', '', '', 'titleLongValue', 'titleShortValue', '', 'publishDateValue', 'actionStatusValue', '', '', '')`
* `call insertupdatedeletemediafeed ('updateActionStatus', 'actionNumberValue', 'actionDescriptionValue', '', '', '', '', '', '', '', '', '', '', '', '', '')`
* `call insertupdatedeletemediafeed ('updateMediaAudioEncode', '', '', 'audioEncodeValue', '', '', '', '', '', '', '', '', '', '', 'movieIncludeValue', 'tvIncludeValue')`
* `call insertupdatedeletemediafeed ('updateMediaDynamicRange', '', '', '', 'dynamicRangeValue', '', '', '', '', '', '', '', '', '', 'movieIncludeValue', 'tvIncludeValue')`
* `call insertupdatedeletemediafeed ('updateMediaResolution', '', '', '', '', 'resolutionValue', '', '', '', '', '', '', '', '', 'movieIncludeValue', 'tvIncludeValue')`
* `call insertupdatedeletemediafeed ('updateMediaResolution', '', '', '', '', '', 'streamSourceValue', 'streamDescriptionValue', '', '', '', '', '', '', 'movieIncludeValue', 'tvIncludeValue')`
* `call insertupdatedeletemediafeed ('updateMediaVideoEncode', '', '', '', '', '', '', '', 'videoEncodeValue', '', '', '', '', '', 'movieIncludeValue', 'tvIncludeValue')`
* `call insertupdatedeletemediafeed ('updateMovieFeed', '', '', '', '', '', '', '', '', 'titleLongValue', 'titleShortValue', '', 'publishDateValue', 'actionStatusValue', '', '')`
* `call insertupdatedeletemediafeed ('updateMovieFeedTitleShort', '', '', '', '', '', '', '', '', '', 'titleShortValue', 'titleShortOldValue', '', '', '', '')`
* `call insertupdatedeletemediafeed ('updateMovieFeedTitleShortActionStatus', '', '', '', '', '', '', '', '', '', 'titleShortValue', '', '', 'actionStatusValue', '', '')`
* `call insertupdatedeletemediafeed ('updateTVFeed', '', '', '', '', '', '', '', '', 'titleLongValue', 'titleShortValue', '', 'publishDateValue', 'actionStatusValue', '', '')`
* `call insertupdatedeletemediafeed ('updateTVFeedTitleShort', '', '', '', '', '', '', '', '', '', 'titleShortValue', 'titleShortOldValue', '', '', '', '')`
* `call insertupdatedeletemediafeed ('updateTVFeedTitleShortActionStatus', '', '', '', '', '', '', '', '', '', 'titleShortValue', '', '', 'actionStatusValue', '', '')`
