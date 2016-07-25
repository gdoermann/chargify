from setuptools import setup, find_packages


version = open('voicebase/VERSION', 'r').readline().strip()

setup(
    name='chargify',
    version=version,
    description="python chargify library",
    long_description="""This is a generic SDK for hooking up with the Chargify API""",
    author='Greg Doermann',
    author_email='greg@tell.bz',
    url='http://github.com/gdoermann/chargify',
    license='GNU General Public License',
    platforms=['any'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',],
    packages=find_packages(),
    include_package_data=True,
)
