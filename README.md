
WIP

```
from colab_a11y_utils import set_sound_notification, tqdm

set_sound_notification()

import time
for epoch in tqdm(range(10)):
    time.sleep(1)
```

# For contributer

## Update PyPI

```
$ nosetests -vs
$ pip install twine # if necessary
$ cat ~/.pypirc  # if necessary
[distutils]
index-servers = pypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: YOUR_USERNAME
password: YOUR_PASSWORD
$ rm -rf colab_a11y_utils.egg-info dist # if necessary
$ python setup.py sdist
$ twine upload --repository pypi dist/*
$ pip --no-cache-dir install --upgrade colab-a11y-utils
```

https://pypi.org/project/colab-a11y-utils/

## Contributing

- Fork the repository on Github
- Create a named feature branch (like add_component_x)
- Write your change
- Write tests for your change (if applicable)
- Run the tests, ensuring they all pass
- Submit a Pull Request using Github

# License

MIT
