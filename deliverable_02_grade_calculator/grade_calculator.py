def get_score(label):
    while True:
        score_text = input(f"{label} score: ").strip()

        try:
            score = float(score_text)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= score <= 100:
            return score

        print("Score must be between 0 and 100.")


def calculate_grade():
    test_score = get_score("Test")
    assignment_score = get_score("Assignment")
    exam_score = get_score("Exam")

    total_score = test_score + assignment_score + exam_score
    average_score = total_score / 3

    passed = average_score >= 50 and exam_score >= 40
    qualifies_for_award = average_score >= 80 and test_score >= 70 and assignment_score >= 70 and exam_score >= 70

    print("\nStudent Grade Result")
    print("-" * 30)
    print(f"Test score: {test_score:.2f}")
    print(f"Assignment score: {assignment_score:.2f}")
    print(f"Exam score: {exam_score:.2f}")
    print(f"Total score: {total_score:.2f}")
    print(f"Average score: {average_score:.2f}")

    if passed:
        print("Status: Passed")
    else:
        print("Status: Failed")

    if qualifies_for_award:
        print("Award: Qualified for academic excellence award")
    else:
        print("Award: Not qualified")


def main():
    print("Smart Student Grade Calculator")
    calculate_grade()


if __name__ == "__main__":
    main()
