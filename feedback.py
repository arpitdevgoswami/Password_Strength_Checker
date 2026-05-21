def generate_feedback(results, score, password):
    feedback = []

    if results['common_password'] == -2:
        feedback.append("🚨 This is a very common password! Avoid it completely.")
    if results['length'] == 0:
        feedback.append("❌ Password is too short. Use at least 8 characters.")
    elif results['length'] == 1:
        feedback.append("⚠️  Try making your password 12+ characters for better strength.")
    elif results['length'] == 2:
        feedback.append("⚠️  Consider using 16+ characters for very strong protection.")
    elif results['length'] == 3:
        feedback.append("⚠️  Go for 20+ characters to reach Highly secured level!")

    if results['uppercase'] == 0:
        feedback.append("❌ Add at least one uppercase letter (A-Z).")

    if results['lowercase'] == 0:
        feedback.append("❌ Add at least one lowercase letter (a-z).")

    if results['digit'] == 0:
        feedback.append("❌ Add at least one number (0-9).")

    if results['special_char'] == 0:
        feedback.append("❌ Add at least one special character (!@#$%^&*).")

    if results['repeated_char'] == -1:
        feedback.append("⚠️  Avoid repeating the same character 3+ times (e.g. 'aaa', '111').")

    if results['sequential'] == -1:
        feedback.append("⚠️  Avoid sequential patterns like 'abc' or '123'.")
    
    

    if score >= 8:
        feedback.append("✅ Excellent password! Extremely hard to crack.")
    elif score >= 6:
        feedback.append("✅ Very strong password! Just a few tweaks can make it perfect.")

    return feedback


if __name__ == "__main__":
    from checker import analyze_password
    from scorer import evaluate

    passwords = ["hi", "Hello123", "X#9kL!mQ2@wZpQrT!yUo"]

    for p in passwords:
        print(f"\nPassword: {p}")
        print("-" * 40)
        results = analyze_password(p)
        score, label = evaluate(results)
        print(f"Score: {score}  →  {label}")
        tips = generate_feedback(results, score, p)
        for tip in tips:
            print(tip)