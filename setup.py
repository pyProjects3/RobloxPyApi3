from setuptools import setup, find_packages
from RobloxPyApi3.Version import __Copyright__
Version = "2.02"

Description = "RobloxPyApi3 is a great Roblox API controller that offers a variety of features, such as API wrapping, multi accounts control, join game and Place Creation and more. More features are coming soon. Do not use it on illegal purposes, Im not responsible for this.  Thanks for using RobloxPyApi3!! -pyProjects3"

Long_Description = f"""
Welcome to the RobloxPyAPI3 package, created by pyProjects3. This package is designed to make Roblox game development possible in python, API Wrapper (Access Roblox API), Multi Account management and being able to join games and leave games.

One of the key features of this package is its support for Place creation. With our Place creation tools, you can now create your Roblox Places in python, whether you're working on a personal project or developing a game with a team. Our tools make it easy to upload new assets, manage permissions, and more.

In addition to Place creation, the RobloxPyAPI3 package includes an API Wrapper that provides easy access to the Roblox API. Our wrapper simplifies the process of sending and receiving data from the Roblox API, making it easier to build automated bots and other tools that interact with the Roblox platform.

Another key feature of our package is multi-account management. If you're working on multiple projects or need to manage multiple Roblox accounts for any reason, our package makes it easy to do so. You can easily switch between accounts, manage permissions, and more, all from within the same package.

Finally, we want to note that the RobloxPyAPI3 package is created by pyProjects3 and is protected by copyright. We take great pride in our work and hope that our package will help make your Roblox game development experience even better. More features are coming soon to the project.

Copyright (c) 2023 pyProjects3 creations. All Rights Reserved.
"""
setup(
    name="RobloxPyApi3",
    version=Version,
    author="pyProjects3 (github.com/pyProjects3)",
    description=Description,
    long_description_content_type="text/markdown",
    long_description=Long_Description,
    packages=find_packages(),
    license="MIT",

    package_data= {'Place':["*.py"]},
    include_package_data=True,
    install_requires=['requests','colorama','psutil','RobloxPyApi3Update'],
    keywords=["Roblox","Api",'wrapper',"Bot",'Client','Automated',"Account Management","rbx","Python3","Place automation","post requests","get requests","JSON","Authorization","Roblox Development"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
