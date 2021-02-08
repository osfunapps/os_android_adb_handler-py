from distutils.core import setup

setup(
    name='os_android_adb_handler',
    packages=['os_android_adb_handler'],
    version='1.00',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='This module aims to provide functional and simple ADB commands to control an Android device from code (externally).',
    author='Oz Shabat',  # Type in your name
    author_email='admin@os-apps.com',  # Type in your E-Mail
    url='https://github.com/osfunapps/os_android_adb_handler-py',  # Provide either the link to your github or to your website
    keywords=['python', 'osfunapps', 'adb', 'android', 'osapps', 'automation'],  # Keywords that define your package best
    install_requires=['os_tools'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',  # Again, pick a license

        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9'
    ],
)

