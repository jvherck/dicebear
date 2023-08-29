import unittest
from urllib.parse import quote
from dicebear_wrapper.dicebear import avatar
from dicebear_wrapper.dicebear import errors
from dicebear_wrapper.dicebear import models
from dicebear_wrapper.dicebear import utility


class TColor(unittest.TestCase):
    def testBase(self):
        c1 = models.DColor("transparent")
        c2 = models.DColor("#fff333")
        c3 = models.DColor("transparent, 000fff")
        c4 = models.DColor(["transparent", "000fff"])
        self.assertEqual(c1, "transparent")
        self.assertEqual(c2, "fff333")
        self.assertRaises(errors.IncorrectColor, models.DColor, html_code="za32da")
        self.assertRaises(errors.IncorrectColor, models.DColor, html_code="transparentt")
        self.assertEqual(c3, "transparent,000fff")
        self.assertEqual(c4, "transparent,000fff")


class TOptions(unittest.TestCase):
    options = models.DOptions(flip=True, scale=50, backgroundType="gradientLinear", translateX=5, randomizeIds=True)

    def testBase(self):
        self.assertEqual(self.options, {
            "flip": True,
            "scale": 50,
            "backgroundType": "gradientLinear",
            "translateX": 5,
            "randomizeIds": True
        })


class TFormat(unittest.TestCase):
    def testBase(self):
        allf = models.DFormat.all_formats
        png = models.DFormat.png
        json = models.DFormat.from_str("json")
        self.assertEqual(allf, ["svg", "png", "jpg", "json"])
        self.assertEqual(png, "png")
        self.assertEqual(json, "json")
        self.assertRaises(AttributeError, models.DFormat.from_str, format_str="jpeg")


class TStyle(unittest.TestCase):
    def testBase(self):
        alls = models.DStyle.all_styles
        bottts = models.DStyle.bottts
        avataaars = models.DStyle.from_str("avataaars")
        self.assertEqual(alls, models.styles)
        self.assertEqual(bottts, "bottts")
        self.assertEqual(avataaars, "avataaars")
        self.assertRaises(AttributeError, models.DStyle.from_str, style_str="something-wrong")
        self.assertIn(models.DStyle.random(), models.styles)
        schema = models.DStyle.get_schema(models.DStyle.rings)
        self.assertEqual("object", schema["type"])
        self.assertIn("properties", schema)
        self.assertIn("seed", schema["properties"])
        self.assertIn("type", schema["properties"]["seed"])
        self.assertEqual("string", schema["properties"]["seed"]["type"])
        self.assertIn("ringOne", schema["properties"])
        self.assertIn("ringTwo", schema["properties"])
        self.assertIn("ringThree", schema["properties"])
        self.assertIn("ringFour", schema["properties"])
        self.assertIn("ringFive", schema["properties"])


class TAvatar(unittest.TestCase):
    def testBase(self):
        style = models.DStyle.random()
        seed = "John Apple"
        options = models.DOptions(flip=True, rotate=90, backgroundType="gradientLinear")
        av = avatar.DAvatar(style, seed, options=options)
        self.assertEqual(
            av,
            avatar._x.format(quote(style), quote(seed)) + "flip=true&rotate=90&backgroundType=gradientLinear"
        )

    def test2(self):
        style = "John Apple"
        seed = "John Apple"
        options = models.DOptions(flip=True, rotate=90, backgroundType="gradientLinear")
        self.assertRaises(
            errors.Error,
            avatar.DAvatar,
            style=style, seed=seed, options=options
        )

    def testAdv(self):
        style = "bottts"
        seed = "John Apple"
        options = models.DOptions(flip=True)
        custom = {
            "eyes": "dizzy",
            "texture": "camo01",
            "somethingWrong": "doesNotMatter"
        }
        av = avatar.DAvatar(style, seed, options=options, custom=custom)
        self.assertEqual(
            av,
            avatar._x.format(quote(style), quote(seed)) + "flip=true&eyes=dizzy&texture=camo01&somethingWrong=doesNotMatter"
        )


class TUtil(unittest.TestCase):
    def testSingle(self):
        style = models.DStyle.random()
        seed = "John Apple"
        options = models.DOptions(rotate=90)
        custom = {"scale": "52"}
        av = utility.create_avatar(style, seed, options, custom)
        self.assertEqual(
            av,
            avatar._x.format(quote(style), quote(seed)) + "rotate=90&scale=52"
        )

    def testRandom(self):
        av = utility.create_random(True)
        _url_svg = av.url_svg
        self.assertEqual(av.url_svg, _url_svg)

    def testMulti(self):
        style = models.DStyle.thumbs
        options = models.DOptions(rotate=90)
        custom = {"faceOffsetX": 15}
        avs = utility.bulk_create(style, 3, options=options, custom=custom)
        self.assertEqual(len(avs), 3)
        for item in avs:
            self.assertEqual(
                item.url_svg.startswith("https://api.dicebear.com/") and item.url_svg.endswith("&rotate=90&faceOffsetX=15"),
                True
            )


if __name__ == '__main__':
    unittest.main()
