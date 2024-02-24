import sys
import unittest

from openai_service import make_query

# # TODO: Currently importing from outside directory. Need to make external package.
# sys.path.append(".")
# from openai_service import make_query


class TestAIService(unittest.TestCase):
    def test_query_openai(self):

        file = open("data/clinical_luad1.csv", mode="rb")
        data = file.read()
        try:
            response, is_image = make_query(data, "Show the distribution of ALK?")

            self.assertEqual(is_image, True)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
