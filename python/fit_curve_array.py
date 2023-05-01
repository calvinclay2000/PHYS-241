import numpy as np


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):
    """

    :param
    :return:
    """
    if max_x<min_x:
        raise ArithmeticError
    try:
        x_values = np.linspace(min_x, max_x, number_of_points)
        y_values = np.polyval(quadratic_coefficients, x_values)
        return [x_values, y_values]
    except IndexError as error:
        print(f'{error}')
    except ArithmeticError as error:
        print(f'{error}')


if __name__ == "__main__":
    test_coefficients = [1,0,0]
    print(fit_curve_array(test_coefficients, -2, 2, number_of_points=5))