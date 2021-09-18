import pytest
from moz_youtube import upload, UploadOption


class TestYoutubeUploader:
    @pytest.mark.slow
    def test_upload(self):
        options = UploadOption(
            {
                "file": "./tests/resources/test.mp4",
                "title": "hogehoge",
                "description": "これは説明です。",
                "keywords": "hoge,foo,bar",
            }
        )
        upload(options)
