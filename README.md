<!--- Heading --->
<div align="center">
  <h1>ak_cache</h1>
  <p>
    Cache any data for your python projects
  </p>
</div>
<br />

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/rpakishore/ak_cache)
![GitHub last commit](https://img.shields.io/github/last-commit/rpakishore/ak_cache)
<!-- Table of Contents -->
<h2>Table of Contents</h2>

- [1. About the Project](#1-about-the-project)
  - [1.1. Features](#11-features)
- [2. Getting Started](#2-getting-started)
  - [2.1. Installation](#21-installation)
- [3. Usage](#3-usage)
- [4. Roadmap](#4-roadmap)
- [5. License](#5-license)
- [6. Contact](#6-contact)

<!-- About the Project -->
## 1. About the Project

<!-- Features -->
### 1.1. Features

- Read and write data to a Cached Pickle File

<!-- Getting Started -->
## 2. Getting Started

<!-- Installation -->
### 2.1. Installation

```bash
pip install ak_cache
```

Alternatively

```bash
git install ak_cache@git+https://github.com/rpakishore/ak_cache.git
```

<!-- Usage -->
## 3. Usage

Use this space to tell a little more about your project and how it can be used. Show additional screenshots, code samples, demos or link to other resources.

```python
from ak_cache import Cache
cache_file = Cache(r'Path\to\Cache\file.pkl')
cache_file.write('This is a text')
cache_file.read()
```

Encrypt your pickle file as below

```python
cache_file = Cache(r'Path\to\Cache\encr_file.pkl', password="Strong_Password")

cache_file.write('This is an encrypted text')
cache_file.read()
```
<!-- Roadmap -->
## 4. Roadmap

- [x] Add encryption option to the cache file

<!-- License -->
## 5. License

See [LICENSE](./LICENSE) for more information.

<!-- Contact -->
## 6. Contact

Arun Kishore - [@rpakishore](mailto:ak_cache@rpakishore.co.in)

Project Link: [https://github.com/rpakishore/ak_cache](https://github.com/rpakishore/ak_cache)
