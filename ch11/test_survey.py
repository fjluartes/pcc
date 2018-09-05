#!/usr/bin/env python
# test_survey.py: test cases for AnonymousSurvey
# 5 Sep 2018 | fjgl
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""
    def test_store_single_response(self):
        """Test that a sigle response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

unittest.main()
