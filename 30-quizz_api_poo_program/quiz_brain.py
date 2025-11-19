import html


class QuizBrain:

    def __init__(self, q_list):
        # Store list of Question objects
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Return True if there are remaining questions."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Move to the next question and return its text."""
        # Get current question object
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        # Decode HTML entities from API (e.g., &quot;)
        q_text = html.unescape(self.current_question.text)

        # Return formatted question
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """Check if the user's answer matches the correct one."""
        correct_answer = self.current_question.answer

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
