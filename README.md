# moz-youtube

自前のYouTube操作ライブラリ。

## Function

- random_get_video
- get_video_match_today
- get_videos_within_x_day
- get_play_list
- upload
- add_to_play_list
- delete_from_play_list

## Usage

Environmental variables

`.env`ファイルに書いてproject rootに配置。

```txt
moz_youtube_client_secret_contents='{"installed":{"client_id":"....}'
moz_youtube_token_contents='{"access_token": "...}'
moz_youtube_new_token_contents='{"access_token": "...}'
```

Install

```sh
pip install git+https://github.com/mozkzki/moz-youtube
# upgrade
pip install --upgrade git+https://github.com/mozkzki/moz-youtube
# uninstall
pip uninstall moz-youtube
```

Coding

```python
>>> from moz_youtube import random_get_video
>>> random_get_video()
```

## Develop

base project: [mozkzki/moz-sample](https://github.com/mozkzki/moz-sample)

### Prepare

```sh
poetry install
poetry shell
```

### Run (Example)

```sh
python ./example/example.py
# or
make start
```

### Unit Test

test all.

```sh
pytest
pytest -v # verbose
pytest -s # show standard output (same --capture=no)
pytest -ra # show summary (exclude passed test)
pytest -rA # show summary (include passed test)
```

with filter.

```sh
pytest -k app
pytest -k test_app.py
pytest -k my
```

specified marker.

```sh
pytest -m 'slow'
pytest -m 'not slow'
```

make coverage report.

```sh
pytest -v --capture=no --cov-config .coveragerc --cov=src --cov-report=xml --cov-report=term-missing .
# or
make ut
```

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./src
# or
make lint
```

### Create API Document (Sphinx)

```sh
make doc
```
