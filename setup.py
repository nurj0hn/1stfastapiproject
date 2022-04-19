from setuptools import setup

setup(
    name='fast-api-app',
    version='0.0.1',
    author='Nurjon',
    description='FastAPI app',
    install_requires=[
        'fastapi==0.75.1',
        'uvicorn==0.15.0',
        'SQLAlchemy==1.4.35',
        'pytest==7.1.1',
        'requests==2.27.1',
        'alembic==1.7.7'
    ],
    scripts=['app/main.py', 'scripts/craete_db.py']
)