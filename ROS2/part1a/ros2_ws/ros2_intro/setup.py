from setuptools import find_packages, setup

package_name = 'ros2_intro'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lavish',
    maintainer_email='lavishg@iitbhilai.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "pub_node = ros2_intro.publisher:main",
            "sub_node = ros2_intro.subscriber:main"
        ],
    },
)
