# -*- coding: utf-8 -*-
# プログラミング的思考
# TODO(deck)　トランプを作る：　得点を数えられるように数字
# TODO(deal) トランプを2枚配る： 絵札(J,Q,K)で表示させる
# TODO(hand) プレイヤーに配られたカードを記録する
# TODO(hit) ヒットの場合handを追加する
# TODO(game) 実際にプレーする
# TODO(total) プレイヤーの合計を求める
# TODO(result) 勝ち負けを表記する
# TODO(play_again) もう一度プレイするか確認する

import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4


def deal():
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = 'J'
        if card == 12:
            card = 'Q'
        if card == 13:
            card = 'K'
        if card == 1:
            card = 'A'
        hand.append(card)
    return hand


def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card = 'J'
    if card == 12:
        card = 'Q'
    if card == 13:
        card = 'K'
    if card == 1:
        card = 'A'
    hand.append(card)
    return hand


def total(hand):
    score = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            score = score + 10
        elif card == 'A':
            if score >= 11:
                score = score + 1
            else:
                score = score + 11
        else:
            score = score + card
    return score


this_is_my_first_game = True


def play_start():
    if this_is_my_first_game == True:
        print('\nブラックジャックをはじめます！')
        print('hirohiro')
        print(this_is_my_first_game)
        game()
    else:
        again = input('\n\n\nもう一度プレイしますか? (Y/N):')
        if again == 'y' or again == 'Y':
            game()
        else:
            print('お疲れ様でした！')
            exit()


def play_again():
    again = input("もう１度プレイしますか？ (Y/N): ")
    if again == "y" or again == "Y":
        game()
        return
    else:
        print("お疲れ様でした！")
        exit()


def result(dealer_hand, player_hand):
    if total(player_hand) > total(dealer_hand):
        print(f'\nディーラーの合計は{total(dealer_hand)} あなたの合計は{total(player_hand)}です。 YOU WIN!')
    elif total(player_hand) < total(dealer_hand):
        print(f'\nディーラーの合計は{total(dealer_hand)} あなたの合計は{total(player_hand)}です。 YOU LOSE...')


def game():
    # this_is_my_first_game = False
    # print('hirohiro2')
    # print(this_is_my_first_game)
    dealer_hand = deal()
    player_hand = deal()
    print(f'\nディーラーカードは{dealer_hand[0]}, * です。')
    print(f'プレイヤーカードは {player_hand}　合計が{total(player_hand)}です。')

    choice = 0

    while True:
        choice = input('ヒットしますか? スタンドしますか? (HIT/STAND)：').lower()
        if choice == 'hit':
            hit(player_hand)
            print(f'\nあなたに{player_hand}が配られ、カードは{player_hand}　合計は{total(player_hand)}です。')
            if total(player_hand) > 21:
                print('あなたは21を超えてしまいました。　YOU LOSE....')
                play_again()

        elif choice == 'stand':
            print(f'\nディーラーの２枚目のカードは{dealer_hand[1]} 合計は{total(dealer_hand)}です。')
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(f'ディーラーに{dealer_hand}が配られ、カードは{dealer_hand}　合計は{total(dealer_hand)}です。')
                if total(dealer_hand) > 21:
                    print('ディーラーは 21を超えてしまいました。 YOU WIN!')
                    play_again()

            if total(dealer_hand) <= 21:
                result(dealer_hand, player_hand)
                play_again()


play_start()
