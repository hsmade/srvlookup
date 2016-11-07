import setuptools

setuptools.setup(
    name='srvlookup',
    version='1.0.0',
    description='Service lookup using DNS SRV records',
    long_description=open('README.rst').read(),
    author='Gavin M. Roy',
    author_email='gavinr@aweber.com',
    url='https://github.com/gmr/srvlookup',
    py_modules=['srvlookup'],
    package_data={'': ['LICENSE', 'README.rst']},
    include_package_data=True,
    install_requires=['dnspython>=1.15.0'],
    tests_require=['nose', 'mock', 'coverage'],
    test_suite='nose.collector',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True)
