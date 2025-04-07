from setuptools import setup, find_packages

setup(
    name='textsmith',
    version='0.1',
    packages=find_packages(),
    description='A modular text-based game engine for building interactive text-based games.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your-email@example.com',
    url='https://github.com/xqill275/Textsmith',  # Replace with the actual GitHub URL
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)