from abc import ABC
from pathlib import Path
from urllib.parse import urlparse

import httpx

from clappia_api_tools.client.base_client import (
    BaseAPIKeyClient,
    BaseAuthTokenClient,
    BaseClappiaClient,
)
from clappia_api_tools.utils import FileUtils


class FileManagementClient(BaseClappiaClient, ABC):
    """Client for managing Clappia file management."""

    async def upload_file(
        self,
        app_id: str,
        file_bytes: bytes,
        filename: str,
        mime_type: str,
        upload_category: str,
    ) -> tuple[str, str]:
        payload: dict[str, str] = {
            "appId": app_id,
            "fileName": filename,
            "mimeType": mime_type,
            "uploadCategory": upload_category,
        }

        success, error_message, response_data = await self.api_utils.make_request(
            method="POST",
            endpoint="/generateFileUploadUrl",
            data=payload,
        )

        if not success:
            raise Exception(error_message)

        if response_data is None or not isinstance(response_data, dict):
            raise Exception("Invalid response data from API")

        file_upload_url = response_data["fileUploadUrl"]
        file_id = response_data["fileId"]
        public_file_url = response_data.get("publicFileUrl")

        if not file_upload_url or not file_id:
            raise Exception(f"Failed to generate {filename} file upload URL")

        async with httpx.AsyncClient() as client:
            response = await client.put(file_upload_url, content=file_bytes)
            if response.status_code != 200:
                raise Exception(f"Failed to upload {filename} file")

        return file_id, public_file_url

    async def upload_html_file(
        self,
        app_id: str,
        html_content: str,
        filename: str,
        upload_category: str = "printtemplate",
    ) -> tuple[Path, str, str]:
        file_path, detected_mime_type = FileUtils.save_text_file(
            text_content=html_content, filename=filename, mime_type="text/html"
        )

        file_id, public_file_url = await self.upload_file(
            app_id=app_id,
            file_bytes=file_path.read_bytes(),
            filename=filename,
            mime_type=detected_mime_type,
            upload_category=upload_category,
        )

        return file_path, file_id, public_file_url

    async def upload_file_from_url(
        self,
        app_id: str,
        file_url: str,
        filename: str | None = None,
        upload_category: str = "appicon",
    ) -> tuple[str, str]:
        async with httpx.AsyncClient() as client:
            response = await client.get(file_url)
            if response.status_code != 200:
                raise Exception(
                    f"Failed to download file from URL: {response.status_code}"
                )

            file_bytes = response.content
            content_type = response.headers.get(
                "Content-Type", "application/octet-stream"
            )

        if not filename:
            parsed_url = urlparse(file_url)
            filename = parsed_url.path.split("/")[-1] or "file"
            if "." not in filename:
                filename = "file"

        file_id, public_file_url = await self.upload_file(
            app_id=app_id,
            file_bytes=file_bytes,
            filename=filename,
            mime_type=content_type,
            upload_category=upload_category,
        )

        return file_id, public_file_url


class FileManagementAPIKeyClient(BaseAPIKeyClient, FileManagementClient):
    """Client for managing Clappia file management with API key authentication."""

    def __init__(
        self,
        api_key: str,
        base_url: str,
        timeout: int = 30,
    ):
        """Initialize file management client with API key.

        Args:
            api_key: Clappia API key.
            base_url: API base URL.
            timeout: Request timeout in seconds.
        """
        BaseAPIKeyClient.__init__(self, api_key, base_url, timeout)


class FileManagementAuthTokenClient(BaseAuthTokenClient, FileManagementClient):

    def __init__(
        self,
        auth_token: str,
        workplace_id: str,
        base_url: str,
        timeout: int = 30,
    ):
        """Initialize file management client with auth token.

        Args:
            auth_token: Clappia Auth token.
            workplace_id: Clappia Workplace ID.
            base_url: API base URL.
            timeout: Request timeout in seconds.
        """
        BaseAuthTokenClient.__init__(self, auth_token, workplace_id, base_url, timeout)
