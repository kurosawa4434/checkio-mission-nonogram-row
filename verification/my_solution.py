from re import findall


UNKNOWN = '?'
FILLED = 'O'
EMPTY = 'X'


def nonogram_row(row_string, clue_numbers):

    results = []
    answer = ''

    def search(rest_clues, rest_string, result_row=''):

        if not rest_clues:
            result_row += row_string[len(result_row):]

            if list(map(len, findall(f'{FILLED}+', result_row))) == clue_numbers:
                results.append(result_row)

            return

        tgt_clue = rest_clues[0]

        for i in range(len(rest_string) - tgt_clue + 1):
            if EMPTY not in rest_string[i: i + tgt_clue]:
                nx = len(result_row + rest_string[:i]) + tgt_clue
                search(rest_clues[1:],
                       rest_string[i + tgt_clue + 1:],
                       result_row + rest_string[:i] + FILLED*tgt_clue + row_string[nx: nx+1])

    # step 1: get all possibilities
    search(clue_numbers, row_string)

    if not results:
        return None

    # step 2: summarize the possibilities
    for i in range(len(row_string)):
        if len(set([row[i] for row in results])) == 1:
            tgt_chr = results[0][i]
            answer += EMPTY if tgt_chr == UNKNOWN else tgt_chr
        else:
            answer += UNKNOWN

    # print(answer)
    return answer
