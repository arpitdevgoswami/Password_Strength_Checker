def calculate_score(results):
    score = 0

    score += results['common_password']
    score += results['length']
    score += results['uppercase']
    score += results['lowercase']
    score += results['digit']
    score += results['special_char']
    score += results['repeated_char']
    score += results['sequential']

   
    # Score should never goes below ZERO...
    score = max(score, 1)
    return score

def get_strength_label(score):
    if score >= 8:
        return "🔵 Highly Secure"
    elif score >= 6:
        return "🟢 Very Strong"
    elif score >= 5:
        return "🟡 Strong"
    elif score >= 3:
        return "🟠 Fair"
    else:
        return "🔴 Weak"

def evaluate (results):
    score = calculate_score(results)
    label = get_strength_label(score)
    return score, label


if __name__ == "__main__":
    from checker import analyze_password

    passwords = ["hi", "Hello123", "Hello@123", "X#9kL!mQ2@wZ", "X#9kL!mQ2@wZpQrT!yUo"]

    for p in passwords:
        results = analyze_password(p)
        score, label = evaluate(results)
        print(f"Password: {p:25} Score: {score}  →  {label}")
