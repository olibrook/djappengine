from setuptools import setup, find_packages

setup(
    name="djappengine",
    version="0.1",
    packages=find_packages(),
    scripts=['memcache.py'],
    description="",
    install_requires=[
        'google-api-python-client>=1.2'
    ],
    entry_points={
        'console_scripts': [
            'get_refresh_token=djappengine.tools.get_refresh_token:main',
            'sandbox_shell=djappengine.tools.sandbox_shell:main',
        ],
    }
)
