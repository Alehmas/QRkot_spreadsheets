import types
try:
    from app.core import google_client
except (NameError, ImportError):
    raise AssertionError(
        'File `google_client` not found. '
        'Check and fix: it should be available in the `app.core` module.',
    )


def test_scopes():
    assert hasattr(google_client, 'SCOPES'), (
        'The variable `SCOPES` was not found in the file `google_client`'
    )
    assert len(google_client.SCOPES) == 2, (
        'Make sure the number of objects in `google_client.SCOPES` is two.'
    )
    for scope in google_client.SCOPES:
        assert any(s in scope for s in ['drive', 'spreadsheets']), (
            'The required access level was not found in `google_client.SCOPES`'
        )


def test_info():
    assert hasattr(google_client, 'INFO'), (
        'No `INFO` variable found in file `google_client`'
    )
    info = google_client.INFO
    need_info_keys = [
        'type',
        'project_id',
        'private_key_id',
        'private_key',
        'client_email',
        'client_id',
        'auth_uri',
        'token_uri',
        'auth_provider_x509_cert_url',
        'client_x509_cert_url',
    ]

    for info_key in need_info_keys:
        assert info_key in info, (
            f'No key `{info_key}` found in object `google_client.INFO`'
        )


def test_connect():
    assert hasattr(google_client, 'get_service'), (
        'No `get_service` function found in file `google_client`'
    )
    service = google_client.get_service()
    assert isinstance(service, types.AsyncGeneratorType), (
        'The `google_client.get_service` function must return an asynchronous generator.'
    )
