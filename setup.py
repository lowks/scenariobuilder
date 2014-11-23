from setuptools import setup

setup(
    name='scenariobuilder',
    version='0.1.16',
    description='Instantiates scenarios described by the scenario_node_terminus data model on an Openstack cloud',
    packages=['scenariobuilder'],
    license='Apache',
    url='https://github.com/CiscoSystems/scenariobuilder',
    install_requires=['python-novaclient', 'python-neutronclient', 'PyYaml', 'Jinja2'],
    scripts=['bin/sb'],
    include_package_data=True
)


