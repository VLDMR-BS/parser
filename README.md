# Site parser

This repository to parse some information from sites

## Setup project

Dependency management is performed via [Poetry](https://python-poetry.org/docs/). So file
`pyproject.toml` stores initial dependencies and `poetry.lock` stores actual versions of
all packages.

Poetry provides a [installer](https://python-poetry.org/docs/#installation) that will
install poetry isolated from the rest of your system by vendorizing its dependencies. This
is the recommended way of installing poetry. Update PATH manually if it wasn't during
installation: `export PATH="$HOME/.poetry/bin:$PATH"`

Despite `poetry` is able to create virtualenvs itself, we use `conda` as an environment
provider because of `conda forge` builds it provides (nowadays simple Data Science project
dependencies can be installed from regular `pip` but we are for reliability). So it is
recommended to [install `miniconda`](https://docs.conda.io/en/latest/miniconda.html) and
create separate environment for `evonets` there.

Your `conda` environment have to have `python` version compatible with this project (see
`pyproject.toml` for actual value):

To create new environment with specific `python` version run\
`conda env create -f linux-env.yml`\
 YAML file contains env name, python version and required env variables

To install project dependencies to currently active environment run `poetry install`

## Example

To run parse information in termunal you need to activate conda env abd run file
`commands.py`. Run example:
`python commands.py run_parse https://leetcode.com/problemset/all/ /tmp/info_1.csv`

## Add your decoder

Create a class inheritance of BaseDecoder
(`from site_packages.decoders import BaseDecoder`) and create your decoder. After add they
import to **init**.py in decoders and add they to `decoder_lists`

## Build to wheel

To build this package to wheel you need to setup project and after that run commnad
`poetry build`.
