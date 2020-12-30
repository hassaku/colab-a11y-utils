# colab-a11y-util

This library provides the following functions in Google Colab
- Notification by sound at the time of cell execution
  - One beep sound when executed
  - Two beep sounds when normal completion
  - Two buzzer sounds when abnormal completion
- Sound notification of progress bar by tqdm
- Simple audio output function that can be used instead of print

See the following example.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hassaku/colab-a11y-utils/blob/master/colab_a11y_util_example.ipynb)

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
