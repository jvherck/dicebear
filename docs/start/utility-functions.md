---
description: >-
  You can find some functions here that can help with quickly creating avatars
  or getting useful information.
---

# 🛠️ Utility Functions

### _def create\_avatar()_

Create a DAvatar object and return it.

```python
def create_avatar(
    style: DStyle,
    seed: str,
    options: DOptions | None = None,
    customisations: dict | None = None
) -> DAvatar
```

> Returns: a new [`DAvatar`](../reference/avatar.md#class-davatar) object

<table><thead><tr><th width="197.80536912751677">Parameter</th><th width="110">Type</th><th width="191">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>style</code></td><td><a href="../reference/models.md#class-dstyle">DStyle</a></td><td><code>DStyle.random()</code></td><td>The style of avatar you want to create (<a data-mention href="customization.md#styles">#styles</a>)</td></tr><tr><td><code>seed</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#str">str</a></td><td><code>None</code></td><td>Base string to determine the avatar.</td></tr><tr><td><code>options</code></td><td><a href="../reference/models.md#class-doptions">DOptions</a></td><td><code>DOptions.empty</code></td><td>General options for the avatar.</td></tr><tr><td><code>customisations</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></td><td><code>None</code></td><td>Customisations (for the chosen style)</td></tr></tbody></table>

&#x20;

### _def create\_random()_

Create a random DAvatar object and return it.

```python
def create_random(
    randomOptions: bool = False
) -> DAvatar
```

> Returns: a new [`DAvatar`](../reference/avatar.md#class-davatar) object

<table><thead><tr><th width="197.80536912751677">Parameter</th><th width="110">Type</th><th width="191">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>randomOptions</code></td><td><a href="https://docs.python.org/3/library/functions.html#bool">bool</a></td><td><code>False</code></td><td>Whether to use random (background) options for this avatar or not</td></tr></tbody></table>



### _def bulk\_create()_

Create a list of [`DAvatar`](utility-functions.md#class-davatar) objects (with random seeds).

```python
def bulk_create(
    style: DStyle = DStyle.random(),
    amount: int = 2,
    *,
    options: DOptions = DOptions.default,
    custom: dict = None
) -> list[DAvatar]
```

> Returns: [`list[DAvatar]`](https://docs.python.org/3/library/stdtypes.html?highlight=list#list): a list of [`DAvatar`](../reference/avatar.md) objects

<table><thead><tr><th width="137.80536912751677">Parameter</th><th width="150">Type</th><th width="195">Default</th><th>Description</th></tr></thead><tbody><tr><td><code>style</code></td><td><a href="../reference/models.md#class-dstyle">DStyle</a></td><td><code>DStyle.random()</code></td><td>The style you want to create (<a data-mention href="customization.md#styles">#styles</a>)</td></tr><tr><td><code>amount</code></td><td><a href="https://docs.python.org/3/library/functions.html#int">int</a></td><td><code>2</code></td><td>The amount of DAvatar objects you want to create.</td></tr><tr><td><code>options</code></td><td><a href="../reference/models.md#class-doptions">DOptions</a></td><td><code>DOptions.empty</code></td><td>General options for the avatars.</td></tr><tr><td><code>custom</code></td><td><a href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></td><td><code>None</code></td><td>Customisations (for the chosen style)</td></tr></tbody></table>



