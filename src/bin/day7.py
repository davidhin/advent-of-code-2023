from functools import cmp_to_key
from collections import Counter


def hand_type(hand):
    if sorted(Counter(hand).values()) == [5]:
        return 7
    if sorted(Counter(hand).values()) == [1, 4]:
        return 6
    if sorted(Counter(hand).values()) == [2, 3]:
        return 5
    if sorted(Counter(hand).values()) == [1, 1, 3]:
        return 4
    if sorted(Counter(hand).values()) == [1, 2, 2]:
        return 3
    if sorted(Counter(hand).values()) == [1, 1, 1, 2]:
        return 2
    return 1


def compare_same_hand_type(hand1, hand2):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    letter_map = {item: index for index, item in enumerate(cards)}
    for i in range(0, len(hand1)):
        if letter_map[hand1[i]] > letter_map[hand2[i]]:
            return -1
        if letter_map[hand1[i]] < letter_map[hand2[i]]:
            return 1
    return 0


def compare(hand1, hand2):
    hand_type_num = hand_type(hand1) - hand_type(hand2)
    if hand_type_num == 0:
        return compare_same_hand_type(hand1, hand2)
    else:
        return hand_type_num


def explain_sorted(sorted_hands):
    names = {
        7: "Five of a kind",
        6: "Four of a kind",
        5: "Full house",
        4: "Three of a kind",
        3: "Two pair",
        2: "One pair",
        1: "High card",
    }
    for hand in sorted_hands:
        print(f"{hand} => {names[hand_type(hand)]}")


def parse_input(filepath):
    with open(filepath, "r") as file:
        content = file.read()
    content = content.splitlines()
    content = {i.split()[0]: int(i.split()[1]) for i in content}
    return content


hand_to_bets = parse_input("../../data/day7a.txt")

sorted_hands = sorted(hand_to_bets.keys(), key=cmp_to_key(compare))


intermediate = list(enumerate([hand_to_bets[i] for i in sorted_hands]))
multiplied_pairs = [(i[0] + 1) * i[1] for i in intermediate]
final_result = sum(multiplied_pairs)

print(final_result)
