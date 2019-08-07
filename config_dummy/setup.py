from setuptools import setup
setup(name='PythonBehave',
      version='1.0',
      description='Python Behave Examples',
      author='Berna Gökçe',
      author_email='bernagokce92@gmail.com',
      url='https://www.meetup.com/tr-TR/TestHive/',
      packages=[
            'BDDCommon',
            'BDDCommon.CommonFuncs',
            'BDDCommon.CommonSteps',
            'BDDCommon.CommonConfigs'
      ],
     )

     #~/Desktop/behave-selenium-example/practical_example
     #python setup.py install
     #for each time you need to use it its annoying
     #python setup.py develop
     #development modu çalıştırdı ve create it ti ve her değişikliğin setup oluyor.
     #after to run it it downloaded build, dist and egg.info file automatically