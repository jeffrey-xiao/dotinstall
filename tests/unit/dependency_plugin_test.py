import mock
import pytest

from dotinstall.plugins.dependency import Dependency


@pytest.mark.parametrize('update', [True, False])
def test_execute_update_false(update):
    pkg_manager = mock.Mock()
    Dependency().execute(
        options={
            'update': update,
        },
        data={
            'dependencies': ['ack', 'python'],
        },
        pkg_manager=pkg_manager,
    )
    if update:
        pkg_manager.install.assert_not_called()
    else:
        pkg_manager.install.assert_has_calls([mock.call('ack'), mock.call('python')])
