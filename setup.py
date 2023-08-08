from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hotel_booking/__init__.py
from hotel_booking import __version__ as version

setup(
	name="hotel_booking",
	version=version,
	description="A Custom appliaction created for make Hotel booking seamless.",
	author="Prabhu Verma",
	author_email="prabhuvermaaa@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
