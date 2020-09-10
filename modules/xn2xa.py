"""
New Unit
"""
x_xa_matrix = ['A', 'B', 'C', 'D', 'E', 'F', 'K', 'L', 'M',
               'N', 'P', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z',
               '1', '2', '3', '4', '5', '6', '7', '8', '9']

x_xa_m_size = len(x_xa_matrix)


def conv_xn_xa(xn: int, xw: int) -> str:
    """
    Converts number to custom alpha repr according to xa matrix
    xn = xNumbers
    xa = xAlphas
    :param xw: Desired width
    :param xn: Input Number
    :return:
    """

    # Calculating power of matrix length for input number
    x_xa_s_size = 0
    x_curr_valu = xn
    while True:
        x_curr_valu = x_curr_valu / x_xa_m_size
        if x_curr_valu < 1:
            break
        x_xa_s_size += 1

    # Calculating Actual xAlpha
    x_prep_alpha = ''
    x_curr_valu = xn
    for x_curr_posi in range(x_xa_s_size, 0, -1):  # +1 for Range function specific counting
        x_curr_powr = (x_xa_m_size ** x_curr_posi)  # Current power of matrix size
        x_curr_rmdr = x_curr_valu // x_curr_powr  # Current remainder and index for Alpha
        x_curr_valu = x_curr_valu - (x_curr_rmdr * (x_xa_m_size ** x_curr_posi))
        x_prep_alpha += x_xa_matrix[x_curr_rmdr]
        # print(x_curr_posi, x_curr_rmdr,  x_curr_valu)

    # Last character is the remainder
    x_xa_s_size += 1
    x_prep_alpha += x_xa_matrix[x_curr_valu]

    # Filling empty spaces with 0
    if len(x_prep_alpha) < xw:
        x_full_alpha = ('0' * (xw - len(x_prep_alpha))) + x_prep_alpha
    else:
        x_full_alpha = x_prep_alpha

    return x_full_alpha


def conv_xa_xn(xa: str) -> int:
    x_temp_alfa = xa.strip('0')
    x_xa_length = len(x_temp_alfa)

    x_full_nums = 0

    # Iterating in the string
    for x_curr_alfa in x_temp_alfa:
        x_full_nums += x_xa_matrix.index(x_curr_alfa) * (x_xa_m_size ** (x_xa_length - 1))
        x_xa_length -= 1

    return x_full_nums


def main():
    x = 100000
    print(conv_xn_xa(x, 5))
    print(conv_xa_xn(conv_xn_xa(x, 4)))


if __name__ == '__main__':
    main()
