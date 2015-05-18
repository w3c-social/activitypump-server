# Copyright (C) 2015 Christopher Allan Webber <cwebber@dustycloud.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name="minipump",
    version="0.0.1.dev",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "flask",
        # Technically only needed to make docs
        "sphinx",
        ],
    test_suite='nose.collector',
    license="Apache License 2.0",
    description="Bare minimum demo implementation of the ActivityPump spec",
    author='Minipump contributors',
    author_email='cwebber@dustycloud.org')
