import os, sys
from platform import system

# detects the OS for the clear command
if system() == 'Windows':
    clear = 'cls'
else:
    clear = 'clear'

os.system(clear)

global _1, _2, _3, _4, _5, _6, _7, _8, _9, _10
# 1st ball, 2nd ball, total
_1 = [' ', ' ', '   ']
_2 = [' ', ' ', '   ']
_3 = [' ', ' ', '   ']
_4 = [' ', ' ', '   ']
_5 = [' ', ' ', '   ']
_6 = [' ', ' ', '   ']
_7 = [' ', ' ', '   ']
_8 = [' ', ' ', '   ']
_9 = [' ', ' ', '   ']
# 1st ball, 2nd ball, fill ball, total
_10 = [' ', ' ', ' ', '   ']

def main():
    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    strike_bonus_counters = {0: 0, 0: 0, 0: 0}
    spare_bonus_counter = {0: 0}

    #########################################################

    strike_bonus_counters, spare_bonus_counter, strike1 = frame1shot1(_1, strike_bonus_counters, spare_bonus_counter)
    if strike1:
        pass
    else:
        strike_bonus_counters, spare_bonus_counter = frame1shot2(_1, strike_bonus_counters, spare_bonus_counter)

    strike_bonus_counters, spare_bonus_counter, strike2 = frame2shot1(_2, strike_bonus_counters, spare_bonus_counter)
    if strike2:
        pass
    else:
        strike_bonus_counters, spare_bonus_counter = frame2shot2(_1, _2, strike_bonus_counters, spare_bonus_counter)

    strike_bonus_counters, spare_bonus_counter, strike3 = frame3shot1(_3, strike_bonus_counters, spare_bonus_counter)
    if strike3:
        pass
    else:
        strike_bonus_counters, spare_bonus_counter = frame3shot2(_2, _3, strike_bonus_counters, spare_bonus_counter)

    strike_bonus_counters, spare_bonus_counter, strike4 = frame4shot1(_4, strike_bonus_counters, spare_bonus_counter)
    if strike4:
        pass
    else:
        strike_bonus_counters, spare_bonus_counter = frame4shot2(_3, _4, strike_bonus_counters, spare_bonus_counter)

    strike_bonus_counters, spare_bonus_counter, strike5 = frame5shot1(_5, strike_bonus_counters, spare_bonus_counter)
    if strike5:
        pass
    else:
        strike_bonus_counters, spare_bonus_counter = frame5shot2(_4, _5, strike_bonus_counters, spare_bonus_counter)

    strike_bonus_counters, spare_bonus_counter, strike6 = frame6shot1(_6, strike_bonus_counters, spare_bonus_counter)
    if strike6:
        pass
    else:
        strike_bonus_counters, spare_bonus_counter = frame6shot2(_5, _6, strike_bonus_counters, spare_bonus_counter)

    strike_bonus_counters, spare_bonus_counter, strike7 = frame7shot1(_7, strike_bonus_counters, spare_bonus_counter)
    if strike7:
        pass
    else:
        strike_bonus_counters, spare_bonus_counter = frame7shot2(_6, _7, strike_bonus_counters, spare_bonus_counter)

    strike_bonus_counters, spare_bonus_counter, strike8 = frame8shot1(_8, strike_bonus_counters, spare_bonus_counter)
    if strike8:
        pass
    else:
        strike_bonus_counters, spare_bonus_counter = frame8shot2(_7, _8, strike_bonus_counters, spare_bonus_counter)

    strike_bonus_counters, spare_bonus_counter, strike9 = frame9shot1(_9, strike_bonus_counters, spare_bonus_counter)
    if strike9:
        pass
    else:
        strike_bonus_counters, spare_bonus_counter = frame9shot2(_8, _9, strike_bonus_counters, spare_bonus_counter)

    # frame 10
    strike_bonus_counters, spare_bonus_counter, strike10, shot1_fixer = frame10shot1(_10, strike_bonus_counters, spare_bonus_counter)
    if strike10:
        strike_bonus_counters, spare_bonus_counter, strike10_2, shot2_fixer = frame10shot2_strike_opp(_10, strike_bonus_counters, spare_bonus_counter)
        if strike10_2:
            strike_bonus_counters, spare_bonus_counter = frame10shot3_strike_opp(_10, strike_bonus_counters, spare_bonus_counter, shot1_fixer)
        else:
            strike_bonus_counters, spare_bonus_counter = frame10shot3_spare_opp(_9, _10, strike_bonus_counters, spare_bonus_counter, shot2_fixer)
    else:
        strike_bonus_counters, spare_bonus_counter, spare10 = frame10shot2(_9, _10, strike_bonus_counters, spare_bonus_counter)
        if spare10:
            strike_bonus_counters, spare_bonus_counter = frame10shot3_strike_opp(_10, strike_bonus_counters, spare_bonus_counter, shot1_fixer)


def frame1shot1(_1, strike_bonus_counters, spare_bonus_counter):
    strike1 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame1shot1(_1, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame1shot1(_1, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike1 = True
        shot = 'X'
        _1[0] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 1, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 1, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 1, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike1

    # if execution reaches here, there was no strike
    os.system(clear)
    _1[0] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 1, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 1, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 1, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike1


def frame1shot2(_1, strike_bonus_counters, spare_bonus_counter):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _1[0] + shot > 9:
            return frame1shot2(_1, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame1shot2(_1, strike_bonus_counters, spare_bonus_counter)
        # spare detection
        os.system(clear)
        shot = '/'
        _1[1] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 1, False)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 1, True)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, '/', 1, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no spare
    os.system(clear)
    _1[1] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 1, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 1, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 1, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter


def frame2shot1(_2, strike_bonus_counters, spare_bonus_counter):
    strike2 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame2shot1(_2, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame2shot1(_2, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike2 = True
        shot = 'X'
        _2[0] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 2, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 2, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 2, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike2

    # if execution reaches here, there was no strike
    os.system(clear)
    _2[0] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 2, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 2, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 2, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike2


def frame2shot2(_1, _2, strike_bonus_counters, spare_bonus_counter):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _2[0] + shot > 9:
            return frame2shot2(_1, _2, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame2shot2(_1, _2, strike_bonus_counters, spare_bonus_counter)
        # spare detection
        os.system(clear)
        shot = '/'
        _2[1] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 2, False)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 2, True)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, '/', 2, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no spare
    os.system(clear)
    _2[1] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 2, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 2, False)

    # detects X followed by open
    if _1[0] == 'X' and _2[0] != 'X' and _2[1] != '/':
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 2, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, True)
    else:
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 2, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter


def frame3shot1(_3, strike_bonus_counters, spare_bonus_counter):
    strike3 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame3shot1(_3, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame3shot1(_3, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike3 = True
        shot = 'X'
        _3[0] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 3, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 3, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 3, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike3

    # if execution reaches here, there was no strike
    os.system(clear)
    _3[0] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 3, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 3, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 3, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike3


def frame3shot2(_2, _3, strike_bonus_counters, spare_bonus_counter):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _3[0] + shot > 9:
            return frame3shot2(_2, _3, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame3shot2(_2, _3, strike_bonus_counters, spare_bonus_counter)
        # spare detection
        os.system(clear)
        shot = '/'
        _3[1] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 3, False)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 3, True)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, '/', 3, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no spare
    os.system(clear)
    _3[1] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 3, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 3, False)

    # detects X followed by open
    if _2[0] == 'X' and _3[0] != 'X' and _3[1] != '/':
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 3, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, True)
    else:
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 3, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter


def frame4shot1(_4, strike_bonus_counters, spare_bonus_counter):
    strike4 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame4shot1(_4, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame4shot1(_4, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike4 = True
        shot = 'X'
        _4[0] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 4, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 4, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 4, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike4

    # if execution reaches here, there was no strike
    os.system(clear)
    _4[0] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 4, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 4, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 4, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike4


def frame4shot2(_3, _4, strike_bonus_counters, spare_bonus_counter):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _4[0] + shot > 9:
            return frame4shot2(_3, _4, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame4shot2(_3, _4, strike_bonus_counters, spare_bonus_counter)
        # spare detection
        os.system(clear)
        shot = '/'
        _4[1] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 4, False)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 4, True)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, '/', 4, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no spare
    os.system(clear)
    _4[1] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 4, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 4, False)

    # detects X followed by open
    if _3[0] == 'X' and _4[0] != 'X' and _4[1] != '/':
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 4, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, True)
    else:
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 4, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter


def frame5shot1(_5, strike_bonus_counters, spare_bonus_counter):
    strike5 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame5shot1(_5, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame5shot1(_5, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike5 = True
        shot = 'X'
        _5[0] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 5, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 5, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 5, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike5

    # if execution reaches here, there was no strike
    os.system(clear)
    _5[0] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 5, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 5, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 5, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike5


def frame5shot2(_4, _5, strike_bonus_counters, spare_bonus_counter):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _5[0] + shot > 9:
            return frame5shot2(_4, _5, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame5shot2(_4, _5, strike_bonus_counters, spare_bonus_counter)
        # spare detection
        os.system(clear)
        shot = '/'
        _5[1] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 5, False)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 5, True)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, '/', 5, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no spare
    os.system(clear)
    _5[1] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 5, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 5, False)

    # detects X followed by open
    if _4[0] == 'X' and _5[0] != 'X' and _5[1] != '/':
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 5, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, True)
    else:
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 5, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter


def frame6shot1(_6, strike_bonus_counters, spare_bonus_counter):
    strike6 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame6shot1(_6, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame6shot1(_6, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike6 = True
        shot = 'X'
        _6[0] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 6, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 6, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 6, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike6

    # if execution reaches here, there was no strike
    os.system(clear)
    _6[0] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 6, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 6, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 6, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike6


def frame6shot2(_5, _6, strike_bonus_counters, spare_bonus_counter):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _6[0] + shot > 9:
            return frame6shot2(_5, _6, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame6shot2(_5, _6, strike_bonus_counters, spare_bonus_counter)
        # spare detection
        os.system(clear)
        shot = '/'
        _6[1] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 6, False)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 6, True)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, '/', 6, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no spare
    os.system(clear)
    _6[1] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 6, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 6, False)

    # detects X followed by open
    if _5[0] == 'X' and _6[0] != 'X' and _6[1] != '/':
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 6, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, True)
    else:
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 6, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter


def frame7shot1(_7, strike_bonus_counters, spare_bonus_counter):
    strike7 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame7shot1(_7, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame7shot1(_7, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike7 = True
        shot = 'X'
        _7[0] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 7, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 7, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 7, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike7

    # if execution reaches here, there was no strike
    os.system(clear)
    _7[0] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 7, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 7, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 7, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike7


def frame7shot2(_6, _7, strike_bonus_counters, spare_bonus_counter):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _7[0] + shot > 9:
            return frame7shot2(_6, _7, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame7shot2(_6, _7, strike_bonus_counters, spare_bonus_counter)
        # spare detection
        os.system(clear)
        shot = '/'
        _7[1] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 7, False)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 7, True)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, '/', 7, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no spare
    os.system(clear)
    _7[1] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 7, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 7, False)

    # detects X followed by open
    if _6[0] == 'X' and _7[0] != 'X' and _7[1] != '/':
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 7, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, True)
    else:
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 7, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter


def frame8shot1(_8, strike_bonus_counters, spare_bonus_counter):
    strike8 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame8shot1(_8, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame8shot1(_8, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike8 = True
        shot = 'X'
        _8[0] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 8, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 8, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 8, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike8

    # if execution reaches here, there was no strike
    os.system(clear)
    _8[0] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 8, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 8, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 8, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike8


def frame8shot2(_7, _8, strike_bonus_counters, spare_bonus_counter):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _8[0] + shot > 9:
            return frame8shot2(_7, _8, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame8shot2(_7, _8, strike_bonus_counters, spare_bonus_counter)
        # spare detection
        os.system(clear)
        shot = '/'
        _8[1] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 8, False)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 8, True)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, '/', 8, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no spare
    os.system(clear)
    _8[1] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 8, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 8, False)

    # detects X followed by open
    if _7[0] == 'X' and _8[0] != 'X' and _8[1] != '/':
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 8, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, True)
    else:
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 8, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter


def frame9shot1(_9, strike_bonus_counters, spare_bonus_counter):
    strike9 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame9shot1(_9, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame9shot1(_9, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike9 = True
        shot = 'X'
        _9[0] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 9, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 9, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 9, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike9

    # if execution reaches here, there was no strike
    os.system(clear)
    _9[0] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 9, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 9, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 9, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike9


def frame9shot2(_8, _9, strike_bonus_counters, spare_bonus_counter):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _9[0] + shot > 9:
            return frame9shot2(_8, _9, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame9shot2(_8, _9, strike_bonus_counters, spare_bonus_counter)
        # spare detection
        os.system(clear)
        shot = '/'
        _9[1] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 9, False)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 9, True)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, '/', 9, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no spare
    os.system(clear)
    _9[1] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 9, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 9, False)

    # detects X followed by open
    if _8[0] == 'X' and _9[0] != 'X' and _9[1] != '/':
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 9, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, True)
    else:
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 9, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter


def frame10shot1(_10, strike_bonus_counters, spare_bonus_counter):
    strike10 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame10shot1(_10, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame10shot1(_10, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike10 = True
        shot = 'X'
        _10[0] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 10, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 10, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike10, shot

    # if execution reaches here, there was no strike
    os.system(clear)
    _10[0] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 10, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 10, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike10, shot


def frame10shot2(_9, _10, strike_bonus_counters, spare_bonus_counter):
    spare10 = False
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _10[0] + shot > 9:
            return frame10shot2(_9, _10, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame10shot2(_9, _10, strike_bonus_counters, spare_bonus_counter)
        # spare detection
        os.system(clear)
        spare10 = True
        shot = '/'
        _10[1] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 10, False)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 10, True)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, '/', 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, spare10

    # if execution reaches here, there was no spare
    os.system(clear)
    _10[1] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 10, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 10, False)

    # detects X followed by open
    if _9[0] == 'X' and _10[0] != 'X' and _10[1] != '/':
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, True)
    else:
                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(2, shot, 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, spare10


# These are some more functions for the tenth frame
def frame10shot2_strike_opp(_10, strike_bonus_counters, spare_bonus_counter):
    strike10_2 = False
    shot_fixer = 0
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame10shot2_strike_opp(_10, strike_bonus_counters, spare_bonus_counter)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame10shot2_strike_opp(_10, strike_bonus_counters, spare_bonus_counter)
        # strike detection
        os.system(clear)
        strike10_2 = True
        shot = 'X'
        _10[1] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 10, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 10, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter, strike10_2, shot_fixer

    # if execution reaches here, there was no strike
    os.system(clear)
    _10[1] = shot
    shot_fixer = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 10, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 10, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter, strike10_2, shot_fixer


def frame10shot3_strike_opp(_10, strike_bonus_counters, spare_bonus_counter, shot_fixer):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or shot > 9:
            return frame10shot3_strike_opp(_10, strike_bonus_counters, spare_bonus_counter, shot_fixer)
    except ValueError:
        if shot.upper().strip() != 'X':
            return frame10shot3_strike_opp(_10, strike_bonus_counters, spare_bonus_counter, shot_fixer)
        # strike detection
        os.system(clear)
        shot = 'X'
        _10[2] = 'X'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 10, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 10, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, 'X', 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False, tenth_bonus_ball=True)
        # fixes some issues in the tenth frame
        if _10[0] == 'X':
            _10[0] = 10
        if _10[1] == 10 - _10[0]:
            _10[1] = '/'
        if _10[0] == 10:
            _10[0] = 'X'

        if _10[0] == 'X' and _10[1] == '/' and _10[2] == '/':
            _10[1] = 'X'
            _10[2] = 'X'

        if _10[0] != 'X' and _10[1] == ' ':
            _10[1] = '/'

        if _10[0] == 0 and _10[1] == 'X' and _10[2] == 'X':
            _10[1] = '/'

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no strike
    os.system(clear)
    _10[2] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 10, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 10, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False, tenth_bonus_ball=True)
    # fixes some issues in the tenth frame
    if _10[1] == 0:
        _10[1] = 'X'
    if _10[0] != 'X' and _10[1] == 'X':
        _10[1] = '/'
    _10[0] = 10
    if _10[1] == 10 - _10[0]:
        _10[1] = '/'
    _10[0] = 'X'

    if _10[0] == shot_fixer:
        pass
    else:
        _10[0] = shot_fixer
        _10[1] = '/'

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter
    


def frame10shot3_spare_opp(_9, _10, strike_bonus_counters, spare_bonus_counter, shot_fixer):
    try:
        shot = input()
    except EOFError:
        sys.exit('-EXIT-')
    try:
        shot = int(shot)
        if shot < 0 or _10[1] + shot > 9:
            return frame10shot3_spare_opp(_9, _10, strike_bonus_counters, spare_bonus_counter, shot_fixer)
    except ValueError:
        if shot.upper().strip() != '/':
            return frame10shot3_spare_opp(_9, _10, strike_bonus_counters, spare_bonus_counter, shot_fixer)
        # spare detection
        os.system(clear)
        shot = '/'
        _10[2] = '/'
        # updates the strike bonus penders
        strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 10, True)
        # updates the spare bonus pender
        spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 10, False)

                                                    # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, '/', 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False)
        # fixes an issue in the second tenth frame ball
        _10[1] = shot_fixer
        if _10[1] != 0:
            missing_number = 10 - _10[2]
            _10[1] = missing_number
        _10[2] = '/'

        print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
        return strike_bonus_counters, spare_bonus_counter

    # if execution reaches here, there was no strike
    os.system(clear)
    _10[2] = shot
    # updates the strike bonus penders
    strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true = do_strike_sequence(strike_bonus_counters, 10, False)
    # updates the spare bonus pender
    spare_bonus_counter, frame_to_do_bonus_on_spare, bonus_is_true_spare = do_spare_sequence(spare_bonus_counter, 10, False)

                                                # ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open, 10th frame bonus ball, tenth shot 3 spare opportunity
    _1, _2, _3, _4, _5, _6, _7, _8, _9, _10 = do_totals(1, shot, 10, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, False, tenth_bonus_ball=True, tenth_shot3_spare_opp=True)
    # fixes an issue in the tenth frame
    _10[1] = shot_fixer

    print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10)
    return strike_bonus_counters, spare_bonus_counter
#############################################


def do_strike_sequence(strike_bonus_counters, frame_number, _bool):
    frame_to_do_bonus_on = 0
    bonus_is_true = False

    # isolates the keys into their own list
    keys = []
    for k in strike_bonus_counters:
        keys.append(k)

    # isolates the values into their own list
    values = []
    for v in strike_bonus_counters.values():
        values.append(v)

    # adds extra indices to avoid index out of range
    for _ in range(3):
        keys.append(0)
        values.append(0)

    # decrements each value by 1
    for i in range(3):
        try:
            if values[i] > 0:
                values[i] -= 1
                # if values[0] reaches zero, frame to do bonus on becomes keys[0], and the keys and values to the right shift to the left by one
                if values[0] == 0:
                    frame_to_do_bonus_on = keys[0]
                    bonus_is_true = True
                    keys[0] = keys[1]
                    keys[1] = keys[2]
                    keys[2] = 0
                    values[0] = values[1]
                    values[1] = values[2]
                    values[2] = 0
                    for j in range(2):
                        if values[j] > 0:
                            values[j] -= 1
            else:
                break
        except IndexError:
            pass

    # detects if a strike was just received (will count down from 2 since a strike takes the 10 from the current strike PLUS the next TWO shots)
    if _bool and keys[0] != 10:
        for i in range(len(values)):
            if keys[i] == 0 and values[i] == 0:
                keys[i] = frame_number
                values[i] = 2
                break
    else:
        pass

    # compiles the keys and values back into a dictionary
    strike_bonus_counters = {keys[0]: values[0], keys[1]: values[1], keys[2]: values[2]}
    return strike_bonus_counters, frame_to_do_bonus_on, bonus_is_true


def do_spare_sequence(spare_bonus_counter, frame_number, _bool):
    frame_to_do_bonus_on = 0
    bonus_is_true = False

    # isolates the keys into their own list
    key = []
    for k in spare_bonus_counter:
        key.append(k)

    # isolates the values into their own list
    value = []
    for v in spare_bonus_counter.values():
        value.append(v)

    # decrements the value by 1
    if value[0] > 0:
        value[0] -= 1
        # if value reaches zero, frame to do bonus on becomes key
        if value[0] == 0:
            frame_to_do_bonus_on = key[0]
            bonus_is_true = True
            key[0] = 0

    # detects if a spare was just received (will count down from 1 since a spare takes the 10 from the current spare PLUS the next shot)
    if _bool:
        key[0] = frame_number
        value[0] = 1

    # compiles the key and value back into a dictionary
    spare_bonus_counter = {key[0]: value[0]}
    return spare_bonus_counter, frame_to_do_bonus_on, bonus_is_true


def do_totals(ball, shot, frame, frame_to_do_bonus_on, bonus_is_true, frame_to_do_bonus_on_spare, bonus_is_true_spare, x_open, tenth_bonus_ball=False, tenth_shot3_spare_opp=False):
    # convert strikes to 10s
    if _1[0] == 'X':
        _1[0] = 10
    if _2[0] == 'X':
        _2[0] = 10
    if _3[0] == 'X':
        _3[0] = 10
    if _4[0] == 'X':
        _4[0] = 10
    if _5[0] == 'X':
        _5[0] = 10
    if _6[0] == 'X':
        _6[0] = 10
    if _7[0] == 'X':
        _7[0] = 10
    if _8[0] == 'X':
        _8[0] = 10
    if _9[0] == 'X':
        _9[0] = 10
    if _10[0] == 'X':
        _10[0] = 10
    if _10[1] == 'X':
        _10[1] = 10
    if _10[2] == 'X':
        _10[2] = 10

    # convert spares to 10 minus previous shot
    if _1[1] == '/':
        _1[1] = 10 - _1[0]
    if _2[1] == '/':
        _2[1] = 10 - _2[0]
    if _3[1] == '/':
        _3[1] = 10 - _3[0]
    if _4[1] == '/':
        _4[1] = 10 - _4[0]
    if _5[1] == '/':
        _5[1] = 10 - _5[0]
    if _6[1] == '/':
        _6[1] = 10 - _6[0]
    if _7[1] == '/':
        _7[1] = 10 - _7[0]
    if _8[1] == '/':
        _8[1] = 10 - _8[0]
    if _9[1] == '/':
        _9[1] = 10 - _9[0]
    if _10[1] == '/':
        _10[1] = 10 - _10[0]
    if _10[2] == '/':
        _10[2] = 10 - _10[1]

    # strike bonus
    if bonus_is_true:
        if frame_to_do_bonus_on == 1:
            # if the next frame's second ball is empty, it is implied that the next frame is a strike
            if _2[1] == ' ':
                _1[2] = 0 + _1[0] + _2[0] + _3[0]
            else:
                _1[2] = 0 + _1[0] + _2[0] + _2[1]
        elif frame_to_do_bonus_on == 2:
            # if the next frame's second ball is empty, it is implied that the next frame is a strike
            if _3[1] == ' ':
                _2[2] = _1[2] + _2[0] + _3[0] + _4[0]
            else:
                _2[2] = _1[2] + _2[0] + _3[0] + _3[1]
        elif frame_to_do_bonus_on == 3:
            # if the next frame's second ball is empty, it is implied that the next frame is a strike
            if _4[1] == ' ':
                _3[2] = _2[2] + _3[0] + _4[0] + _5[0]
            else:
                _3[2] = _2[2] + _3[0] + _4[0] + _4[1]
        elif frame_to_do_bonus_on == 4:
            # if the next frame's second ball is empty, it is implied that the next frame is a strike
            if _5[1] == ' ':
                _4[2] = _3[2] + _4[0] + _5[0] + _6[0]
            else:
                _4[2] = _3[2] + _4[0] + _5[0] + _5[1]
        elif frame_to_do_bonus_on == 5:
            # if the next frame's second ball is empty, it is implied that the next frame is a strike
            if _6[1] == ' ':
                _5[2] = _4[2] + _5[0] + _6[0] + _7[0]
            else:
                _5[2] = _4[2] + _5[0] + _6[0] + _6[1]
        elif frame_to_do_bonus_on == 6:
            # if the next frame's second ball is empty, it is implied that the next frame is a strike
            if _7[1] == ' ':
                _6[2] = _5[2] + _6[0] + _7[0] + _8[0]
            else:
                _6[2] = _5[2] + _6[0] + _7[0] + _7[1]
        elif frame_to_do_bonus_on == 7:
            # if the next frame's second ball is empty, it is implied that the next frame is a strike
            if _8[1] == ' ':
                _7[2] = _6[2] + _7[0] + _8[0] + _9[0]
            else:
                _7[2] = _6[2] + _7[0] + _8[0] + _8[1]
        elif frame_to_do_bonus_on == 8:
            # if the next frame's second ball is empty, it is implied that the next frame is a strike
            if _9[1] == ' ':
                _8[2] = _7[2] + _8[0] + _9[0] + _10[0]
            else:
                _8[2] = _7[2] + _8[0] + _9[0] + _9[1]
        elif frame_to_do_bonus_on == 9:
            _9[2] = _8[2] + _9[0] + _10[0] + _10[1]
        elif frame_to_do_bonus_on == 10:
            _10[3] = _9[2] + _10[0] + _10[1] + _10[2]

        # if the previous frame was a strike and the current frame is an open, the current frame total gets added up
        if ball == 2 and x_open:
            if frame == 1:
                _1[2] = 0 + _1[0] + _1[1]
            elif frame == 2:
                _2[2] = _1[2] + _2[0] + _2[1]
            elif frame == 3:
                _3[2] = _2[2] + _3[0] + _3[1]
            elif frame == 4:
                _4[2] = _3[2] + _4[0] + _4[1]
            elif frame == 5:
                _5[2] = _4[2] + _5[0] + _5[1]
            elif frame == 6:
                _6[2] = _5[2] + _6[0] + _6[1]
            elif frame == 7:
                _7[2] = _6[2] + _7[0] + _7[1]
            elif frame == 8:
                _8[2] = _7[2] + _8[0] + _8[1]
            elif frame == 9:
                _9[2] = _8[2] + _9[0] + _9[1]
            elif frame == 10:
                _10[3] = _9[2] + _10[0] + _10[1]

        # convert back to /'s
        if _1[1] != ' ':
            if _1[0] + _1[1] == 10:
                _1[1] = '/'
        if _2[1] != ' ':
            if _2[0] + _2[1] == 10:
                _2[1] = '/'
        if _3[1] != ' ':
            if _3[0] + _3[1] == 10:
                _3[1] = '/'
        if _4[1] != ' ':
            if _4[0] + _4[1] == 10:
                _4[1] = '/'
        if _5[1] != ' ':
            if _5[0] + _5[1] == 10:
                _5[1] = '/'
        if _6[1] != ' ':
            if _6[0] + _6[1] == 10:
                _6[1] = '/'
        if _7[1] != ' ':
            if _7[0] + _7[1] == 10:
                _7[1] = '/'
        if _8[1] != ' ':
            if _8[0] + _8[1] == 10:
                _8[1] = '/'
        if _9[1] != ' ':
            if _9[0] + _9[1] == 10:
                _9[1] = '/'
        # tenth frame
        if _10[1] != 0:
            if _10[1] != ' ':
                if _10[0] + _10[1] == 10:
                    _10[1] = '/'
        # if second conditional wasn't here, a problem could occur
        if _10[2] != 0:
            if _10[2] != ' ':
                _10[1] = 10 - _10[0]
                if _10[1] + _10[2] == 10:
                    _10[2] = '/'

        # convert 10s to strikes
        if _1[0] == 10:
            _1[0] = 'X'
        if _2[0] == 10:
            _2[0] = 'X'
        if _3[0] == 10:
            _3[0] = 'X'
        if _4[0] == 10:
            _4[0] = 'X'
        if _5[0] == 10:
            _5[0] = 'X'
        if _6[0] == 10:
            _6[0] = 'X'
        if _7[0] == 10:
            _7[0] = 'X'
        if _8[0] == 10:
            _8[0] = 'X'
        if _9[0] == 10:
            _9[0] = 'X'
        if _10[0] == 10:
            _10[0] = 'X'
        if _10[1] == 10:
            _10[1] = 'X'
        if _10[2] == 10:
            _10[2] = 'X'
        #########################

        return _1, _2, _3, _4, _5, _6, _7, _8, _9, _10

    # spare bonus
    if bonus_is_true_spare:
        if frame_to_do_bonus_on_spare == 1:
            _1[2] = 0 + _1[0] + _1[1] + _2[0]
        elif frame_to_do_bonus_on_spare == 2:
            _2[2] = _1[2] + _2[0] + _2[1] + _3[0]
        elif frame_to_do_bonus_on_spare == 3:
            _3[2] = _2[2] + _3[0] + _3[1] + _4[0]
        elif frame_to_do_bonus_on_spare == 4:
            _4[2] = _3[2] + _4[0] + _4[1] + _5[0]
        elif frame_to_do_bonus_on_spare == 5:
            _5[2] = _4[2] + _5[0] + _5[1] + _6[0]
        elif frame_to_do_bonus_on_spare == 6:
            _6[2] = _5[2] + _6[0] + _6[1] + _7[0]
        elif frame_to_do_bonus_on_spare == 7:
            _7[2] = _6[2] + _7[0] + _7[1] + _8[0]
        elif frame_to_do_bonus_on_spare == 8:
            _8[2] = _7[2] + _8[0] + _8[1] + _9[0]
        elif frame_to_do_bonus_on_spare == 9:
            _9[2] = _8[2] + _9[0] + _9[1] + _10[0]
        elif frame_to_do_bonus_on_spare == 10:
            _10[3] = _9[2] + _10[0] + _10[1] + _10[2]

        # convert back to /'s
        if _1[1] != ' ':
            if _1[0] + _1[1] == 10:
                _1[1] = '/'
        if _2[1] != ' ':
            if _2[0] + _2[1] == 10:
                _2[1] = '/'
        if _3[1] != ' ':
            if _3[0] + _3[1] == 10:
                _3[1] = '/'
        if _4[1] != ' ':
            if _4[0] + _4[1] == 10:
                _4[1] = '/'
        if _5[1] != ' ':
            if _5[0] + _5[1] == 10:
                _5[1] = '/'
        if _6[1] != ' ':
            if _6[0] + _6[1] == 10:
                _6[1] = '/'
        if _7[1] != ' ':
            if _7[0] + _7[1] == 10:
                _7[1] = '/'
        if _8[1] != ' ':
            if _8[0] + _8[1] == 10:
                _8[1] = '/'
        if _9[1] != ' ':
            if _9[0] + _9[1] == 10:
                _9[1] = '/'
        # tenth frame
        if _10[1] != 0:
            if _9[1] == '/' and _10[1] == ' ':
                _10[1] = 0
                if _10[0] + _10[1] == 10:
                    _10[1] = '/'
                _10[1] = ' '
        # if second conditional wasn't here, a problem could occur
        if _10[2] != 0:
            if _10[0] != 10 and _10[1] == '/':
                _10[1] = 10 - _10[0]
                if _10[1] + _10[2] == 10:
                    _10[2] = '/'

        # convert 10s to strikes
        if _1[0] == 10:
            _1[0] = 'X'
        if _2[0] == 10:
            _2[0] = 'X'
        if _3[0] == 10:
            _3[0] = 'X'
        if _4[0] == 10:
            _4[0] = 'X'
        if _5[0] == 10:
            _5[0] = 'X'
        if _6[0] == 10:
            _6[0] = 'X'
        if _7[0] == 10:
            _7[0] = 'X'
        if _8[0] == 10:
            _8[0] = 'X'
        if _9[0] == 10:
            _9[0] = 'X'
        if _10[0] == 10:
            _10[0] = 'X'
        if _10[1] == 10:
            _10[1] = 'X'
        if _10[2] == 10:
            _10[2] = 'X'
        #########################

        return _1, _2, _3, _4, _5, _6, _7, _8, _9, _10
    
    # else
    if tenth_bonus_ball == False:
        if ball == 2:
            if shot != '/':
                if frame == 1:
                    _1[2] = 0 + _1[0] + _1[1]
                elif frame == 2:
                    _2[2] = _1[2] + _2[0] + _2[1]
                elif frame == 3:
                    _3[2] = _2[2] + _3[0] + _3[1]
                elif frame == 4:
                    _4[2] = _3[2] + _4[0] + _4[1]
                elif frame == 5:
                    _5[2] = _4[2] + _5[0] + _5[1]
                elif frame == 6:
                    _6[2] = _5[2] + _6[0] + _6[1]
                elif frame == 7:
                    _7[2] = _6[2] + _7[0] + _7[1]
                elif frame == 8:
                    _8[2] = _7[2] + _8[0] + _8[1]
                elif frame == 9:
                    _9[2] = _8[2] + _9[0] + _9[1]
                elif frame == 10:
                    _10[3] = _9[2] + _10[0] + _10[1]
    elif tenth_bonus_ball:
        if tenth_shot3_spare_opp:
            _10[3] = _9[2] + 10 + _10[1] + _10[2]
        else:
            _10[3] = _9[2] + 10 + _10[2]

    # convert back to /'s
    if _1[1] != ' ':
        if _1[0] + _1[1] == 10:
            _1[1] = '/'
    if _2[1] != ' ':
        if _2[0] + _2[1] == 10:
            _2[1] = '/'
    if _3[1] != ' ':
        if _3[0] + _3[1] == 10:
            _3[1] = '/'
    if _4[1] != ' ':
        if _4[0] + _4[1] == 10:
            _4[1] = '/'
    if _5[1] != ' ':
        if _5[0] + _5[1] == 10:
            _5[1] = '/'
    if _6[1] != ' ':
        if _6[0] + _6[1] == 10:
            _6[1] = '/'
    if _7[1] != ' ':
        if _7[0] + _7[1] == 10:
            _7[1] = '/'
    if _8[1] != ' ':
        if _8[0] + _8[1] == 10:
            _8[1] = '/'
    if _9[1] != ' ':
        if _9[0] + _9[1] == 10:
            _9[1] = '/'
    # in case of X followed by 0
    if _10[1] != 0:
        if _10[1] != ' ':
            if _10[0] + _10[1] == 10:
                _10[1] = '/'
    if _10[2] != 0:
        if _10[2] != ' ':
            if _10[1] + _10[2] == 10:
                _10[2] = '/'

    # convert 10s to strikes
    if _1[0] == 10:
        _1[0] = 'X'
    if _2[0] == 10:
        _2[0] = 'X'
    if _3[0] == 10:
        _3[0] = 'X'
    if _4[0] == 10:
        _4[0] = 'X'
    if _5[0] == 10:
        _5[0] = 'X'
    if _6[0] == 10:
        _6[0] = 'X'
    if _7[0] == 10:
        _7[0] = 'X'
    if _8[0] == 10:
        _8[0] = 'X'
    if _9[0] == 10:
        _9[0] = 'X'
    if _10[0] == 10:
        _10[0] = 'X'
    if _10[1] == 10:
        _10[1] = 'X'
    if _10[2] == 10:
        _10[2] = 'X'
    #########################

    return _1, _2, _3, _4, _5, _6, _7, _8, _9, _10


def print_scoreboard(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10):
    prefix1 = ''
    prefix2 = ''
    prefix3 = ''
    prefix4 = ''
    prefix5 = ''
    prefix6 = ''
    prefix7 = ''
    prefix8 = ''
    prefix9 = ''
    prefix10 = ''

    # adds prefixing spaces if necessary
    if len(str(_1[2])) == 1:
        prefix1 = '  '
    elif len(str(_1[2])) == 2:
        prefix1 = ' '

    if len(str(_2[2])) == 1:
        prefix2 = '  '
    elif len(str(_2[2])) == 2:
        prefix2 = ' '

    if len(str(_3[2])) == 1:
        prefix3 = '  '
    elif len(str(_3[2])) == 2:
        prefix3 = ' '

    if len(str(_4[2])) == 1:
        prefix4 = '  '
    elif len(str(_4[2])) == 2:
        prefix4 = ' '

    if len(str(_5[2])) == 1:
        prefix5 = '  '
    elif len(str(_5[2])) == 2:
        prefix5 = ' '

    if len(str(_6[2])) == 1:
        prefix6 = '  '
    elif len(str(_6[2])) == 2:
        prefix6 = ' '

    if len(str(_7[2])) == 1:
        prefix7 = '  '
    elif len(str(_7[2])) == 2:
        prefix7 = ' '

    if len(str(_8[2])) == 1:
        prefix8 = '  '
    elif len(str(_8[2])) == 2:
        prefix8 = ' '

    if len(str(_9[2])) == 1:
        prefix9 = '  '
    elif len(str(_9[2])) == 2:
        prefix9 = ' '

    if len(str(_10[3])) == 1:
        prefix10 = '  '
    elif len(str(_10[3])) == 2:
        prefix10 = ' '

    # prints the name and scoreboard
    print('\033[1m- 2-SCORE -\033[0m')
    print()
    print('   1     2     3     4     5     6     7     8     9      10')
    print(f'|  {_1[0]}|{_1[1]}|  {_2[0]}|{_2[1]}|  {_3[0]}|{_3[1]}|  {_4[0]}|{_4[1]}|  {_5[0]}|{_5[1]}|  {_6[0]}|{_6[1]}|  {_7[0]}|{_7[1]}|  {_8[0]}|{_8[1]}|  {_9[0]}|{_9[1]}|  {_10[0]}|{_10[1]}|{_10[2]}|')
    print(f'|  {prefix1}{_1[2]}|  {prefix2}{_2[2]}|  {prefix3}{_3[2]}|  {prefix4}{_4[2]}|  {prefix5}{_5[2]}|  {prefix6}{_6[2]}|  {prefix7}{_7[2]}|  {prefix8}{_8[2]}|  {prefix9}{_9[2]}|    {prefix10}{_10[3]}|')
    print()
    

main()
