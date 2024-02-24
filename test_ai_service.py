import sys
import unittest

import openai_service

# # TODO: Currently importing from outside directory. Need to make external package.
# sys.path.append(".")
# from openai_service import make_query


# Single file and related question works with graph.
# class TestAIService(unittest.TestCase):
#     def test_query_openai(self):

#         file = open("data/clinical_luad1.csv", mode="rb")
#         data = file.read()
#         try:
#             response, is_image = openai_service.make_query(
#                 data, "Show the distribution of ALK?"
#             )
#             self.assertEqual(is_image, True)
#             print(f"Response: <{response}>.")
#         except Exception as e:
#             print(e)


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
# Question is related to both files.
class TestAIService(unittest.TestCase):
    def test_query_openai_question_only(self):
        try:
            response, has_image = openai_service.make_query_only(
                "Count the sample_id for each values of pathologic_stage",
            )
            print(f"Response1: <{response}>.")
            # print(f"Response1: <{type(response.to_string)}>.")
            print(f"Response1:(has-image): <{has_image}>.")

            # response, has_image = openai_service.make_query_only(
            #     "Distribution of TP53 gene for each values of gender",
            # )
            # # # self.assertEqual(is_image, True)
            # print(f"Response2: <{response}>.")
            # print(f"Response2:(has-image): <{has_image}>.")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
