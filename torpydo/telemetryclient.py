import logging

from opencensus.ext.azure.log_exporter import AzureEventHandler

logger = logging.getLogger(__name__)

class TelemetryClient(object):
    def init():
        logger.addHandler(AzureEventHandler(connection_string='InstrumentationKey=c764f176-19a5-4949-825d-9f30db2f14e8;IngestionEndpoint=https://germanywestcentral-1.in.applicationinsights.azure.com/'))
        logger.setLevel(logging.INFO)

    def trackEvent(eventName: str, properties: object):
        logger.info(eventName, extra=properties)        

