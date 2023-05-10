from setuptools import setup
setup(
    name='app-example',
    version='0.0.1',
    author='kent',
    description='Fastapi_Docker_test',
    install_requires=[
        'fastapi==0.70.0',
        'uvicorn==0.15.0',
        'SQLAlchemy==1.4.26',
        'pytest==6.2.5',
        'requests==2.26.0',
        'starlette~=0.16.0',
        'pydantic~=1.10.7'
    ],
    scripts=['app/main.py']
)