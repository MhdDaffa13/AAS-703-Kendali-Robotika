from setuptools import setup

package_name = 'bt_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='erik',
    maintainer_email='erik@todo.todo',
    description='BT Robot Controller',
    license='TODO',
    entry_points={
        'console_scripts': [
            'bt_node = bt_robot.bt_node:main',
        ],
    },
)

