import azure.functions as func
import datetime
import json
import logging
import uuid

app = func.FunctionApp()


@app.function_name("gps-trigger")
@app.event_hub_message_trigger(
    arg_name="event",
    event_hub_name="gps-trigger",
    connection="IOT_HUB_CONNECTION_STRING",
)
@app.blob_output(
    arg_name="outputBlob",
    path="gps-data/{rand-guid}.json",
    connection="STORAGE_CONNECTION_STRING",
)
def main(event: func.EventHubEvent, outputBlob: func.Out[str]):
    logging.info(
        "Python EventHub trigger processed an event: %s",
        event.get_body().decode("utf-8"),
    )

    device_id = event.iothub_metadata["connection-device-id"]
    blob_name = f"{device_id}/{str(uuid.uuid1())}.json"

    event_body = json.loads(event.get_body().decode("utf-8"))
    blob_body = {
        "device_id": device_id,
        "timestamp": event.iothub_metadata["enqueuedtime"],
        "gps": event_body["gps"],
    }

    logging.info(f"Writing to blob: {blob_name} - {blob_body}")

    outputBlob.set(json.dumps(blob_body))
