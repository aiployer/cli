from setuptools import setup

setup(
    name='aiployer',
    version='0.1.0',
    py_modules=['aiployer'],
    install_requires=[
        'Click',
        'jupyter_kernel_gateway'
    ],
    entry_points={
        'console_scripts': [
            'aiployer = command:cli',
        ],
    },
)

if __name__ == '__main__':
    print("setting up")
