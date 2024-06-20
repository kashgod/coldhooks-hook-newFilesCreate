from cloudevents.http import CloudEvent
import functions_framework
from google.events.cloud import firestore

@functions_framework.cloud_event
def hello_firestore(cloud_event: CloudEvent) -> None:
    """Triggered by a creation of a Firestore document in the files subcollection.
    Args:
        cloud_event: Cloud event with information on the Firestore event trigger.
    """
    firestore_payload = firestore.DocumentEventData()
    firestore_payload._pb.ParseFromString(cloud_event.data)

    print(f"Function triggered by change to: {cloud_event['source']}")

    # Extracting the new value from the payload
    new_value = firestore_payload.value.fields

    # Check if 'input_file' or 'output_file' fields exist in the new document
    if 'input_file' in new_value or 'output_file' in new_value:
        print("\nTrigger condition met. New value:")
        print(new_value)
        # Your custom logic here
    else:
        print("\nTrigger condition not met. Ignoring the change.")
