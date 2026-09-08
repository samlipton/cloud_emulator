import time

import requests

API_URL = "http://localhost:8000"
POLL_TIMEOUT_SECONDS = 30
POLL_INTERVAL_SECONDS = 1


def test_health():
    response = requests.get(f"{API_URL}/health", timeout=5)
    assert response.status_code == 200


def test_upload_flow_processes_metadata():
    content = b"hello from the integration test\n"

    upload_response = requests.post(
        f"{API_URL}/upload",
        files={"file": ("hello.txt", content, "text/plain")},
        timeout=10,
    )
    assert upload_response.status_code == 200
    file_id = upload_response.json()["file_id"]

    deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
    metadata = None
    while time.monotonic() < deadline:
        response = requests.get(f"{API_URL}/files/{file_id}", timeout=5)
        if response.status_code == 200:
            metadata = response.json()
            break
        time.sleep(POLL_INTERVAL_SECONDS)

    assert metadata is not None, "worker did not process the upload in time"
    assert metadata["size"] == len(content)
    assert metadata["content_type"] == "text/plain"
