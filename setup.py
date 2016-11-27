from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name              = 'vtechcoder_Video_Looper',
      version           = '1.0.0',
      author            = 'Tony DiCola and vishwaprabhakar',
      author_email      = 'vtechcoder@gmail.com',
      description       = 'Application to turn your Raspberry Pi into a dedicated looping video playback device, good for art installations, information displays, or just playing cat videos all day.',
      license           = 'GNU GPLv2',
      url               = 'https://github.com/vishwaprabhakar/pi_video_looper',
      install_requires  = ['pyudev'],
      packages          = find_packages())
