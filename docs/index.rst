*****
DiceBear Py Wrapper
*****
`dicebear <https://pypi.org/project/dicebear/>`_ is an API wrapper for https://dicebear.com. Using this wrapper you can get custom avatars for your program.
\
For an example go to `examples/dicebear.py <https://github.com/jvherck/dicebear/tree/main/examples>`_.

----


Useful links
#######
* PyPI: https://pypi.org/project/dicebear/
* GitHub: https://github.com/jvherck/dicebear
* Dicebear: https://dicebear.com

----


How to install
#######
| Run :code:`pip install dicebear`
| If that doesn't work try :code:`py -m pip install dicebear`

----


Usage
#######
.. literalinclude:: example.py
   :language: python
   :emphasize-lines: 12,15-18
   :linenos:

----

Styles
#######
All the possible avatar styles.
https://avatars.dicebear.com/styles

* :code:`adventurer`
* :code:`adventurer-neutral`
* :code:`avataaars`
* :code:`big-ears`
* :code:`big-ears-neutral`
* :code:`big-smile`
* :code:`bottts`
* :code:`croodles`
* :code:`croodles-neutral`
* :code:`identicon`
* :code:`initials`
* :code:`micah`
* :code:`miniavs`
* :code:`open-peeps`
* :code:`personas`
* :code:`pixel-art`
* :code:`pixel-art-neutral`


Base Options
**********************

All the possible options for the avatar. These options work for all the styles.

* :code:`seed` (type: :code:`str`) - the seed for the avatar generator (determine its basic looks)
* :code:`dataUri` (type: :code:`bool`) - whether to give the dataUri
* :code:`flip` (type: :code:`bool`) - flips the image vertically
* :code:`rotate` (type: :code:`int`) - rotates the avatar
* :code:`scale` (type: :code:`int`) - the scale of the avatar
* :code:`radius` (type: :code:`int`) - the radius of the avatar
* :code:`size` (type: :code:`int`) - the size of the avatar
* :code:`backgroundColor` (type: :code:`DColor( " #ffffff " )` ) - the background color of the avatar
* :code:`translateX` (type: :code:`int`) - move the avatar horizontally
* :code:`translateY` (type: :code:`int`) - move the avatar vertically


Specific Style Options
**********************

Specific options to get a more detailed avatar. This is different for every style.

* `adventurer <https://avatars.dicebear.com/styles/adventurer#style-options)>`_
* `adventurer-neutral <https://avatars.dicebear.com/styles/adventurer-neutral#style-options)>`_
* `avataaars <https://avatars.dicebear.com/styles/avataaars#style-options)>`_
* `big-ears <https://avatars.dicebear.com/styles/big-ears#style-options)>`_
* `big-ears-neutral <https://avatars.dicebear.com/styles/big-ears-neutral#style-options)>`_
* `big-smile <https://avatars.dicebear.com/styles/big-smile#style-options)>`_
* `bottts <https://avatars.dicebear.com/styles/bottts#style-options)>`_
* `croodles <https://avatars.dicebear.com/styles/croodles#style-options)>`_
* `croodles-neutral <https://avatars.dicebear.com/styles/croodles-neutral#style-options)>`_
* `identicon <https://avatars.dicebear.com/styles/identicon#style-options)>`_
* `initials <https://avatars.dicebear.com/styles/initials#style-options)>`_
* `micah <https://avatars.dicebear.com/styles/micah#style-options)>`_
* `miniavs <https://avatars.dicebear.com/styles/miniavs#style-options)>`_
* `open-peeps <https://avatars.dicebear.com/styles/open-peeps#style-options)>`_
* `personas <https://avatars.dicebear.com/styles/personas#style-options)>`_
* `pixel-art <https://avatars.dicebear.com/styles/pixel-art#style-options)>`_
* `pixel-art-neutral <https://avatars.dicebear.com/styles/pixel-art-neutral#style-options)>`_

----


Credits
#######
Special thanks to `DiceBear <https://github.com/dicebear>`_
(`Florian Körner <https://github.com/FlorianKoerner>`_)
for making this amazing API and to all artists that helped 
making avatars!


Licenses and privacy policy
#######
- Dicebear **Licenses**: https://avatars.dicebear.com/licenses
- Dicebear **Privacy Policy**: https://avatars.dicebear.com/legal/privacy-policy
- Dicebear Python API wrapper (this project): https://choosealicense.com/licenses/mit/