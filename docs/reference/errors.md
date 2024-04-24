---
description: Error classes to find errors more accurately.
---

# Errors

## _class Error(_[_<mark style="color:blue;">Exception</mark>_](https://docs.python.org/3/library/exceptions.html#Exception)_)_

Generic error.

```python
def __init__(self,
    error_type: str = "",
    message: str = ""
) -> None
```

### _class HTTPError(_[_<mark style="color:blue;">Error</mark>_](errors.md#class-error)_)_

The API call returned an error.

```python
def __init__(self,
    dic: dict # The caught HTTP error will often be returned as a dict
) -> None
```

## _class ImageError(_[_<mark style="color:blue;">Exception</mark>_](https://docs.python.org/3/library/exceptions.html#Exception)_)_

Generic error in terms of the avatar image.

```python
def __init__(self,
    message: str = None
) -> None
```

### _class ImageValueError(_[_<mark style="color:blue;">ImageError</mark>_](errors.md#class-imageerror-exception)_)_

The avatar image has a value error.

```python
def __init__(self,
    file_name: str = None
) -> None
```

### _class ImageOSError(_[_<mark style="color:blue;">ImageError</mark>_](errors.md#class-imageerror-exception)_)_

The image cannot be written to your device.

```python
def __init__(self,
    message: str = None
) -> None
```

### _class PILError(_[_<mark style="color:blue;">ImageError</mark>_](errors.md#class-imageerror-exception)_)_

`PIL` is not installed or a DAvatar method that uses `PIL` raised an unexpected error.

```python
def __init__(self,
    message: str = "To use this function you need to install Pillow."
) -> None
```

## _class IncorrectColor(_[_<mark style="color:blue;">Exception</mark>_](https://docs.python.org/3/library/exceptions.html#Exception)_)_

The color you provided is not in hex format.

```python
def __init__(self,
    wrong_color: str = None
) -> None
```

## _class InvalidOption(_[_<mark style="color:blue;">Exception</mark>_](https://docs.python.org/3/library/exceptions.html#Exception)_)_

The option you provided is not a valid option.

```python
def __init__(self,
    wrong_option: str = None
) -> None
```

## _def log\_error()_

Manually log an error either printing the error or raising it.

```python
def log_error(
    exception: Union[Exception, str],
    raise_error: bool = False
) -> None
```

> Raises: The given `exception` if `raise_error` is set to `True`
