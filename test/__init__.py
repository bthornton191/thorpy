TEST_INTEGERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 100, 101, 110, 115, 127, -1, -2, -3, -4]
TEST_EXPECTED_ORDINALS = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '100th', '101st', '110th', '115th', '127th', 'last', '1st to last', '2nd to last', '3rd to last']
TEST_DATA_STRING = '''A,B,C,D\n
11,12,13,14\n
21,22,23,24\n
31,32,33,34\n
41,42,43,44\n
'''

TEST_EXPECTED_DATA_DICT_WITH_HEADERS = [
    {'A': '11', 'B': '12', 'C': '13', 'D': '14'},
    {'A': '21', 'B': '22', 'C': '23', 'D': '24'},
    {'A': '31', 'B': '32', 'C': '33', 'D': '34'},
    {'A': '41', 'B': '42', 'C': '43', 'D': '44'}
]

TEST_EXPECTED_DATA_DICT_WITHOUT_HEADERS = [
    {'1': 'A', '2': 'B', '3': 'C', '4': 'D'},
    {'1': '11', '2': '12', '3': '13', '4': '14'},
    {'1': '21', '2': '22', '3': '23', '4': '24'},
    {'1': '31', '2': '32', '3': '33', '4': '34'},
    {'1': '41', '2': '42', '3': '43', '4': '44'}
]
