"""
Salt runner module providing CI tools and utilities.
"""

import logging

import salt.config
import salt.loader
import salt.pillar

log = logging.getLogger(__name__)


def get_pillar_for_env(minion_id, pillarenv):
    """
    Get the pillar data for a minion in a specific environment.

    Args:
        minion_id (str): The minion ID.
        env (str): The environment.

    Returns:
        dict: The pillar data.
    """
    #opts = __opts__
    opts = salt.config.master_config('/etc/salt/master')

    opts["pillarenv"] = pillarenv
    grains = salt.loader.grains(opts)
    pillar = salt.pillar.Pillar(opts, grains, minion_id, pillarenv)
    pillar_data = pillar.compile_pillar()

    return pillar_data
