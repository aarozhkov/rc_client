import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rc_client",  # Replace with your own username
    version="0.0.1",
    author="Aleksandr Rozhkov",
    author_email="alexander.rozhkov@nordigy.ru",
    description="Ringcentral API wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.ringcentral.com/rcvdevops/rc_sdk.git",
    packages=setuptools.find_packages(),
    install_requires=['pubnub', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
