# Smart Classroom Quiz & Performance Analyzer

# Step 1: Input student IDs and generate unique value
id1 = int(input("Enter Student 1 ID: "))
id2 = int(input("Enter Student 2 ID: "))

last2_id1 = id1 % 100
last2_id2 = id2 % 100

unique_value = (last2_id1 + last2_id2) % 10
print("\nUnique Value Generated:", unique_value)

# Step 2: Store student names
students = {}

print("\nEnter student names (type 'exit' to stop):")

while True:
    name = input("Student name: ").strip()

    if name.lower() == "exit":
        break

    if name == "":
        print("⚠ Warning: Empty name skipped!")
        continue

    students[name] = 0  # initialize score

# Step 3: Display student names
print("\n--- Student List ---")
for name in students:
    print(name)

# Step 4: Quiz Function
def run_quiz(name):
    score = 0

    print(f"\nQuiz for {name}")

    q1 = unique_value + 2
    ans1 = int(input("Q1: unique_value + 2 = "))
    if ans1 == q1:
        score += 1

    q2 = unique_value * 3
    ans2 = int(input("Q2: unique_value × 3 = "))
    if ans2 == q2:
        score += 1

    q3 = unique_value + 5
    ans3 = int(input("Q3: unique_value + 5 = "))
    if ans3 == q3:
        score += 1

    return score

# Step 5: Performance analysis
for name in students:
    score = run_quiz(name)
    students[name] = score

    # Performance level
    if score == 3:
        level = "Excellent"
    elif score == 2:
        level = "Good"
    elif score == 1:
        level = "Average"
    else:
        level = "Poor"

    print("\nScore:", score)
    print("Performance Level:", level)

    # Certificate eligibility
    if score >= 2:
        print("Certificate: Eligible")
    else:
        print("Certificate: Not Eligible")

    # Star pattern
    print("Star Pattern:")
    if score > 0:
        
        print("*" * score)
    else:
        print("")

print("\n--- Final Results ---")
for name, score in students.items():
    print(f"{name}: {score} marks")