from setuptools import setup, find_packages

tests_require = [
    'django',
    'mock',
]

setup(
    name='django-mnemonic',
    version='1.0',
    url='http://github.com/alexlovelltroy/django-mnemonic/',
    description=(
        'Serve up a random set of words from the menmonic encoding project.'
    ),
    author='Alex Lovell-Troy',
    author_email='alex@lovelltroy.org',
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    test_suite='django_mnemonic.runtests.runtests',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires = [],
    zip_safe=False,
)
