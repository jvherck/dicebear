---
description: Base class for the avatar generator.
---

# Avatar

## _class DAvatar_

### Properties

* `style` ([DStyle](models.md#class-dstyle)): the **style** of the avatar
* `seed` ([str](https://docs.python.org/3/library/stdtypes.html#str)): the **seed** of the avatar
* `options` ([DOptions](models.md#class-doptions)): the **options** of the avatar
* `customisations` ([dict](https://docs.python.org/3/library/stdtypes.html#dict)): the **customisations** of the avatar (alias: `customs`)
* `url_svg` ([str](https://docs.python.org/3/library/stdtypes.html#str)): **svg** url for the avatar
* `url_png` ([str](https://docs.python.org/3/library/stdtypes.html#str)): **png** url for the avatar
* `url_jpg` ([str](https://docs.python.org/3/library/stdtypes.html#str)): **jpg** url for the avatar
* `url_json` ([str](https://docs.python.org/3/library/stdtypes.html#str)): **json** url for the avatar data
* `schema` ([dict](https://docs.python.org/3/library/stdtypes.html#dict)): the **dict schema** of the avatar style

&#x20;

### _def \_\_init\_\_()_

Create an avatar using this class. `str(DAvatar)` returns the svg url.

```python
def __init__(self,
    style: DStyle = DStyle.random(),
    seed: str = None,
    *,
    options: DOptions = DOptions.default,
    custom: dict = None
) -> None
```

> Returns: `None`: when called as string it will return the svg link

<table><thead><tr><th width="137.80536912751677">Parameter</th><th width="150">Type</th><th width="195">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>style</code></td><td><a href="models.md#class-dstyle">DStyle</a></td><td><code>DStyle.random()</code></td><td>The style of avatar you want to create (<a data-mention href="../start/customization.md#styles">#styles</a>)</td></tr><tr><td><code>seed</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#str">str</a></td><td><code>None</code></td><td>Base string to determine the avatar.</td></tr><tr><td><code>options</code></td><td><a href="models.md#class-doptions">DOptions</a></td><td><code>DOptions.empty</code></td><td>General options for the avatar.</td></tr><tr><td><code>custom</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></td><td><code>None</code></td><td>Customisations (for the chosen style)</td></tr></tbody></table>

&#x20;

### _def edit()_

Edit an already existing [`DAvatar`](avatar.md#class-davatar).

```python
def edit(self,
    *,
    style: DStyle = None,
    seed: str = None,
    extra_options: DOptions = None,
    blank_options: DOptions = None
) -> str # returns a string containing the svg link
```

> Returns: [`str`](https://docs.python.org/3/library/stdtypes.html#str): the svg link of the edited avatar

<table><thead><tr><th>Parameter</th><th width="150">Type</th><th width="195">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>style</code></td><td><a href="models.md#class-dstyle">DStyle</a></td><td><code>None</code></td><td>The new style of avatar you want to edit (<a data-mention href="../start/customization.md#styles">#styles</a>)</td></tr><tr><td><code>seed</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#str">str</a></td><td><code>None</code></td><td>Base string to determine the edited avatar.</td></tr><tr><td><code>extra_options</code></td><td><a href="models.md#class-doptions">DOptions</a></td><td><code>None</code></td><td>Edit the avatar's options (old options stay, these get added or overwrite if they already existed).</td></tr><tr><td><code>blank_options</code></td><td><a href="models.md#class-doptions">DOptions</a></td><td><code>None</code></td><td>Edit the avatar's options (all old options get deleted and these get added, replacing the old options).</td></tr></tbody></table>

&#x20;

### _def edit\_specific()_

_Deprecated_: removed since v2.2.3

**-> use** [**`DAvatar.customise()`**](avatar.md#def-customise) **instead**.

&#x20;

### _def customise()_

_Alias_: `customize()`

Customise the specific options for an already existing avatar. Specific options/customisations are different for every style, so make sure to check all the possibilities [here](../start/customization.md#specific-style-options).

```python
def customise(self,
    *,
    extra_options: dict = None,
    blank_options: dict = None
) -> str # returns a string containing the svg link
```

> Returns: [`str`](https://docs.python.org/3/library/stdtypes.html#str): the svg link of the edited avatar

<table><thead><tr><th>Parameter</th><th width="150">Type</th><th width="153.75023705670395">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>extra_options</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></td><td><code>None</code></td><td>Edit the avatar's options (old options stay, these get added or overwrite if they already existed).</td></tr><tr><td><code>blank_options</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></td><td><code>None</code></td><td>Edit the avatar's options (all old options get deleted and these get added, replacing the old options).</td></tr></tbody></table>

&#x20;

### _def save()_

Save the avatar to your device.

```python
def save(self,
    *,
    location: pathlib.Path | str = None,
    file_name: str = "dicebear_avatar",
    file_format: DFormat = DFormat.svg,
    overwrite: bool = False,
    open_after_save: bool = False
) -> str # the path where it has been saved if successful
```

> Returns: [`str`](https://docs.python.org/3/library/stdtypes.html#str): the path where the avatar has been saved if successful else `-1`
>
> Raises:
>
> * [`ImageValueError`](errors.md#class-imagevalueerror-imageerror): Image has a ValueError
> * [`ImageOSError`](errors.md#class-imageoserror-imageerror): Image cannot be written to your devide (OSError)
> * [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception): Unknown Exception

<table><thead><tr><th>Parameter</th><th width="150">Type</th><th width="195">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>location</code></td><td><a href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">pathlib.Path</a> | <a href="https://docs.python.org/3/library/stdtypes.html#str">str</a></td><td>current directory</td><td>Location to save the avatar file.</td></tr><tr><td><code>file_name</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#str">str</a></td><td><code>"dicebear_avatar"</code></td><td>Name to give the avatar file.</td></tr><tr><td><code>file_format</code></td><td><a href="models.md#class-dformat">DFormat</a></td><td>DFormat.svg</td><td>Which format to use.</td></tr><tr><td><code>overwrite</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#boolean-values">bool</a></td><td><code>False</code></td><td>Whether to overwrite already existing images with the given filename.</td></tr><tr><td><code>open_after_save</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#boolean-values">bool</a></td><td><code>False</code></td><td>Whether to open the image after saving.</td></tr></tbody></table>

&#x20;

### _def view()_

_Alias_: `open()`

Open and view a [`DAvatar`](avatar.md#class-davatar) object.

```python
def view(self
    *,
    format: DFormat = DFormat.svg,
    use_pil: bool = True
) -> None
```

> Returns: `None`

<table><thead><tr><th width="175">Parameter</th><th width="150">Type</th><th width="156.78523489932886">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>format</code></td><td><a href="models.md#class-dformat"><code>DFormat</code></a></td><td><code>DFormat.svg</code></td><td>What format to use when opening the avatar image.</td></tr><tr><td><code>use_pil</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#boolean-values"><code>bool</code></a></td><td><code>True</code></td><td>Whether to use PIL module or something else to open the avatar.</td></tr></tbody></table>

&#x20;

### _def pillow()_

Convert a [`DAvatar`](avatar.md#class-davatar) instance to a [`PIL.Image.Image`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image) object.

```python
@pilcheck
def pillow(self
) -> PIL.Image.Image
```

> Returns: [`PIL.Image.Image`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image): the Image object to edit using the Pillow module
>
> Raises: [`PILError`](errors.md#class-pilerror-imageerror): if Pillow module is not found on your device

&#x20;

### _def text()_

Returns the avatar's full text/file in `str` format. (only useful for `svg` and `json`)

```python
def text(self,
    format: DFormat = DFormat.svg
) -> str
```

> Returns: `str`: the text of the image

<table><thead><tr><th width="175">Parameter</th><th width="150">Type</th><th width="156.78523489932886">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>format</code></td><td><a href="models.md#class-dformat"><code>DFormat</code></a></td><td><code>DFormat.svg</code></td><td>What format to use.</td></tr></tbody></table>

&#x20;

### _def bytes()_

Returns the avatar's bytes in `io.BytesIO` format (only useful for `png` and `jpg`).

Use `io.BytesIO.read()` to convert it to actual bytes when necessary.

```python
def bytes(self,
    format: DFormat = DFormat.png
) -> io.BytesIO
```

> Returns: `io.BytesIO`: the bytes of the image

<table><thead><tr><th width="175">Parameter</th><th width="150">Type</th><th width="156.78523489932886">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>format</code></td><td><a href="models.md#class-dformat"><code>DFormat</code></a></td><td><code>DFormat.png</code></td><td>What format to use.</td></tr></tbody></table>

&#x20;
