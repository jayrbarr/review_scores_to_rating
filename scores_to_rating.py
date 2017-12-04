def convert_to_numeric(score):
    """
    Take an input score that might be a string, float or int and
    converts to a float value.
    
    score: string, float, int
    converted_score: float
    """
    if isinstance(score, float):
        return score
    else:
        return float(score)
        
def sum_of_middle_three(a,b,c,d,e):
    """
    Takes the input of five float values and returns the sum of the middle three
    values (i.e., throws out the min and max values and calculates sum of remaining).
    
    inputs a,b,c,d,e: floats
    return: float
    """
    sum_of_all_five = a + b + c + d + e
    return sum_of_all_five - min(a,b,c,d,e) - max(a,b,c,d,e)
    
def score_to_rating_string(score):
    """
    From an input float score, match to range of values that corresponds
    to a returned string rating.
    
    input score: float
    return rating: string
    """
    if 0 <= score < 1:
        return "Terrible"
    elif 1 <= score < 2:
        return "Bad"
    elif 2 <= score < 3:
        return "OK"
    elif 3 <= score < 4:
        return "Good"
    elif 4 <= score <= 5:
        return "Excellent"
    return "Error: Score not in range of 0 through 5"
    
def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating
    
print(scores_to_rating(1,2,3,4,5))