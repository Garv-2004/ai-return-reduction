def recommend_size(previous_returns):
    if previous_returns > 2:
        return "Recommend one size smaller"
    else:
        return "Current size looks fine"

print(recommend_size(3))