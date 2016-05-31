# -*- coding: utf-8 -*-

import logging
from typing import TypeVar, Generic

logger = logging.getLogger(__name__)

ConfigClass = TypeVar('ConfigClass')

config_options = {
    'default': 'Development',
}


def register_config(config_class: Generic[ConfigClass]) -> Generic[ConfigClass]:

    logger.debug('Registering the config class {!r}'.format(config_class.__name__))

    config_options.update({config_class.__name__.lower(): config_class})

    return config_class


class Config(object):

    DEBUG = True


@register_config
class Development(Config):

    DEBUG = True


@register_config
class Testing(Config):

    DEBUG = False
