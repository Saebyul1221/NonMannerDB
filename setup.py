from setuptools import setup, find_packages


setup(
    name='NonMannerDB',
    version='1.0.1',
    description='우마공DB 전용 라이브러리',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='WhiteKJ',
    author_email='whitekj1221@gmail.com',
    url='https://github.com/CwhiteKJ/NonMannerDB',
    install_requires=['aiohttp'],
    python_requires='>=3',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)
