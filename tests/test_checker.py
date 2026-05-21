import unittest
import sys
import os

# So Python can find our modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from checker import (check_length, check_uppercase, check_lowercase,
                     check_digit, check_special_char, check_repeated_char,
                     check_sequential, analyze_password)
from scorer import calculate_score, get_strength_label, evaluate
from feedback import generate_feedback


class TestChecker(unittest.TestCase):

    # ── Length Tests ──
    def test_length_too_short(self):
        self.assertEqual(check_length("hi"), 0)

    def test_length_acceptable(self):
        self.assertEqual(check_length("Hello123"), 1)

    def test_length_strong(self):
        self.assertEqual(check_length("Hello123World"), 2)

    def test_length_very_strong(self):
        self.assertEqual(check_length("Hello123WorldExtra"), 3)

    def test_length_excellent(self):
        self.assertEqual(check_length("Hello123WorldExtraBig"), 4)

    # ── Uppercase Tests ──
    def test_has_uppercase(self):
        self.assertEqual(check_uppercase("Hello"), 1)

    def test_no_uppercase(self):
        self.assertEqual(check_uppercase("hello"), 0)

    # ── Lowercase Tests ──
    def test_has_lowercase(self):
        self.assertEqual(check_lowercase("Hello"), 1)

    def test_no_lowercase(self):
        self.assertEqual(check_lowercase("HELLO"), 0)

    # ── Digit Tests ──
    def test_has_digit(self):
        self.assertEqual(check_digit("Hello1"), 1)

    def test_no_digit(self):
        self.assertEqual(check_digit("Hello"), 0)

    # ── Special Char Tests ──
    def test_has_special_char(self):
        self.assertEqual(check_special_char("Hello@"), 1)

    def test_no_special_char(self):
        self.assertEqual(check_special_char("Hello123"), 0)

    # ── Repeated Char Tests ──
    def test_repeated_chars(self):
        self.assertEqual(check_repeated_char("aaa123"), -1)

    def test_no_repeated_chars(self):
        self.assertEqual(check_repeated_char("Hello123"), 0)

    # ── Sequential Tests ──
    def test_sequential(self):
        self.assertEqual(check_sequential("abc123"), -1)

    def test_no_sequential(self):
        self.assertEqual(check_sequential("Hello@999"), 0)


class TestScorer(unittest.TestCase):

    def test_weak_password(self):
        results = analyze_password("hi")
        score, label = evaluate(results)
        self.assertEqual(label, "🔴 Weak")

    def test_fair_password(self):
        results = analyze_password("Hello123")
        score, label = evaluate(results)
        self.assertEqual(label, "🟠 Fair")

    def test_excellent_password(self):
        results = analyze_password("X#9kL!mQ2@wZpQrT!yUo")
        score, label = evaluate(results)
        self.assertEqual(label, "🔵 Highly Secure")


class TestFeedback(unittest.TestCase):

    def test_feedback_common_password(self):
        results = analyze_password("123456")
        score, label = evaluate(results)
        tips = generate_feedback(results, score, "123456")
        self.assertIn("🚨 This is a very common password! Avoid it completely.", tips)

    def test_feedback_no_special_char(self):
        results = analyze_password("Hello123")
        score, label = evaluate(results)
        tips = generate_feedback(results, score, "Hello123")
        self.assertIn("❌ Add at least one special character (!@#$%^&*).", tips)

    def test_feedback_excellent(self):
        results = analyze_password("X#9kL!mQ2@wZpQrT!yUo")
        score, label = evaluate(results)
        tips = generate_feedback(results, score, "X#9kL!mQ2@wZpQrT!yUo")
        self.assertIn("✅ Excellent password! Extremely hard to crack.", tips)


if __name__ == "__main__":
    unittest.main()