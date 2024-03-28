
def cond_prob(sensitivity, specificity, prevalence):

    # Getting probabilites
    probInf = prevalence / 100              # Prior probability of infection
    probPosTest_gInf = sensitivity / 100
    probNegTest_gNotInf = specificity / 100
    probPosTest = (probPosTest_gInf * probInf) + ((1 - probNegTest_gNotInf) * (1 - probInf))

    # Handlind division by zero
    if probPosTest == 0:
        raise ValueError("The denominator is zero.\nSensivity and specificity values may be invalid")

    # Calculating the conditional probability of being infected given a positive test
    probInf_gPosTest = (probPosTest_gInf * probInf) / probPosTest

    return probInf_gPosTest

def get_input_within_range(var_factor, min_value, max_value):
    while True:
        try:
            user_input = float(input(f"Enter {var_factor} value between {min_value} and {max_value}: "))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print("Input value is not within specified range. Please try again\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value\n")


if __name__ == '__main__':
    prev = get_input_within_range("prevalence", 0.001, 50)
    spec = get_input_within_range("specificity", 0, 100)
    sens = get_input_within_range("sensitivity", 0, 100)

    chanceVal = cond_prob(sens, spec, prev)
    print(f"\nThe probability of being truly infected is {chanceVal:.2f}")


