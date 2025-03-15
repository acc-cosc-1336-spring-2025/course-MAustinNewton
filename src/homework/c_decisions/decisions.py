def get_options_ratio(option, total):
    """Returns the ratio of options divided by total."""
    if total == 0:
        return 0  # To prevent division by zero
    return option / total

def get_faculty_rating(ratio):
    """Returns faculty rating based on the given ratio."""
    if 0.9 <= ratio < 1:
        return "Excellent"
    elif ratio > 0.8:
        return "Very Good"
    elif ratio > 0.7:
        return "Good"
    elif ratio > 0.6:
        return "Needs Improvement"
    else:
        return "Unacceptable"
