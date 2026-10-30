import unittest
from agent import build_interview_plan


class InterviewTests(unittest.TestCase):
    def test_each_competency_has_a_question(self):
        result = build_interview_plan({"title": "Engineer", "competencies": ["debugging", "communication"]})
        self.assertEqual(len(result["questions"]), 2)
        self.assertTrue(result["protected_topics_prohibited"])


if __name__ == "__main__":
    unittest.main()
