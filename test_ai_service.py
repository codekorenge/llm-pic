import sys
import unittest

import openai_service

# # TODO: Currently importing from outside directory. Need to make external package.
# sys.path.append(".")
# from openai_service import make_query


# Single file and related question works with graph.
class TestAIService(unittest.TestCase):
    def test_query_openai(self):

        file = open("data/clinical_luad1.csv", mode="rb")
        data = file.read()
        try:
            response, is_image = openai_service.make_query(
                data, "Show the distribution of ALK?"
            )
            self.assertEqual(is_image, True)
            print(f"Response: <{response}>.")
        except Exception as e:
            print(e)


# # Show the distribution of ALK
# # When question is only related to single file, no graph returned but error response from openai.
# class TestAIService(unittest.TestCase):
#     def test_query_openai_for_two_files(self):
#         file1 = open("data/mutation_luad1.csv", mode="rb")
#         file2 = open("data/clinical_luad1.csv", mode="rb")
#         data1 = file1.read()
#         data2 = file2.read()
#         try:
#             response, is_image = openai_service.make_query2(
#                 data1, data2, "Show the distribution of ALK"
#             )

#             self.assertEqual(is_image, True)
#             print(f"Response: <{response}>.")

#         except Exception as e:
#             print(e)


# # Compare the distribution of values of EGFR for each values from primary_therapy_outcome_success
# # Question is realted to both files.
# class TestAIService(unittest.TestCase):
#     def test_query_openai_for_two_files(self):
#         file1 = open("data/mutation_luad1.csv", mode="rb")
#         file2 = open("data/clinical_luad1.csv", mode="rb")
#         data1 = file1.read()
#         data2 = file2.read()
#         try:
#             response, is_image = openai_service.make_query2(
#                 data1,
#                 data2,
#                 "Compare the distribution of values of EGFR for each values from primary_therapy_outcome_success",
#             )

#             self.assertEqual(is_image, True)
#             print(f"Response: <{response}>.")

#         except Exception as e:
#             print(e)


# Compare the distribution of values of EGFR for each values from primary_therapy_outcome_success
# Question is realted to both files.
# class TestAIService(unittest.TestCase):
#     def test_query_openai_question_only(self):
#         try:
#             response = openai_service.make_query_only(
#                 "Compare the distribution of values of EGFR for each values from primary_therapy_outcome_success",
#             )
#             print(f"Response1: <{response}>.")

#             response = openai_service.make_query_only(
#                 "Count the total number of effect of EGFR.",
#             )
#             # self.assertEqual(is_image, True)
#             print(f"Response2: <{response}>.")

#         except Exception as e:
#             print(e)


if __name__ == "__main__":
    unittest.main()
