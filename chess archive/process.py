# fucking handmatig die \t toevoegen in de eerste regel watisdiedan

s = """
 arbordivision (927)\t DucoChapelle (990)	0-1 (won)	5|0	28	8/24/13	 View
 incognit9 (945)	 DucoChapelle (983)	0-1 (won)	5|0	54	8/24/13	 View
 DucoChapelle (975)	 SSP73 (1149)	1-0 (won)	5|0	10	8/24/13	 View
 DucoChapelle (963)	 paulie_15in (995)	draw	5|0	51	8/24/13	 View
 Maissen (837)	 DucoChapelle (962)	0-1 (won)	5|0	28	8/24/13	 View
 DucoChapelle (957)	 Sevennotrump (993)	1-0 (won)	5|0	60	8/24/13	 View
 DucoChapelle (948)	 kon_tat (1027)	0-1 (lost)	5|0	55	8/24/13	 View
 DucoChapelle (955)	 BLOOD-EYE (1078)	1-0 (won)	5|0	46	8/24/13	 View
 rvidele (953)	 DucoChapelle (944)	0-1 (won)	5|0	26	8/24/13	 View
 KTB100 (1043)	 DucoChapelle (935)	1-0 (lost)	5|0	62	8/24/13	 View
 20364162 (1065)	 DucoChapelle (941)	1-0 (lost)	5|0	40	8/24/13	 View
 DucoChapelle (947)	 buzanga (1012)	0-1 (lost)	5|0	38	8/24/13	 View
 Blichd (856)	 DucoChapelle (954)	0-1 (won)	5|0	31	8/23/13	 View
 leedsforever (1139)	 DucoChapelle (948)	draw	5|0	48	8/23/13	 View
 DucoChapelle (944)	 Gjac (1150)	0-1 (lost)	5|0	30	8/23/13	 View
 DucoChapelle (948)	 Konstantin_k (988)	0-1 (lost)	5|0	34	8/22/13	 View
 xxxlll (972)	 DucoChapelle (955)	1-0 (lost)	5|0	29	8/22/13	 View
 DucoChapelle (963)	 Indyy (1124)	1-0 (won)	5|0	17	8/22/13	 View
 DucoChapelle (951)	 mich079 (1040)	0-1 (lost)	5|0	26	8/22/13	 View
 khaled774 (964)	 DucoChapelle (957)	0-1 (won)	5|0	20	8/22/13	 View
 Yulianman (1022)	 DucoChapelle (948)	1-0 (lost)	5|0	13	8/22/13	 View
 DucoChapelle (955)	 REDNAXELAYDARB14 (1034)	1-0 (won)	5|0	53	8/22/13	 View
 DucoChapelle (945)	 scroople (1137)	0-1 (lost)	5|0	14	8/22/13	 View
 rock4200 (903)	 DucoChapelle (949)	1-0 (lost)	5|0	24	8/22/13	 View
 daviti123 (961)	 DucoChapelle (958)	1-0 (lost)	5|0	45	8/22/13	 View
 DucoChapelle (966)	 rashin86 (1031)	draw	5|0	33	8/22/13	 View
 piko68 (1117)	 DucoChapelle (964)	1-0 (lost)	5|0	39	8/20/13	 View
 nyromeo666 (992)	 DucoChapelle (969)	1-0 (lost)	5|0	27	8/20/13	 View
 DucoChapelle (977)	 Muadib23 (910)	0-1 (lost)	5|0	39	8/20/13	 View
 DucoChapelle (987)	 tp119 (936)	1-0 (won)	5|0	12	8/4/13	 View
 DucoChapelle (980)	 woge48 (1096)	1-0 (won)	5|0	23	8/3/13	 View
 warnerdc (894)	 DucoChapelle (969)	0-1 (won)	5|0	17	7/31/13	 View
 DucoChapelle (962)	 ASanches73 (1154)	0-1 (lost)	5|0	48	7/31/13	 View
 mencius99 (1065)	 DucoChapelle (966)	0-1 (won)	5|0	17	7/30/13	 View
 DucoChapelle (955)	 daledmas (929)	1-0 (won)	5|0	34	7/29/13	 View
 daledmas (980)	 DucoChapelle (946)	0-1 (won)	5|0	36	7/29/13	 View
 mike_wiebe (917)	 DucoChapelle (936)	0-1 (won)	5|0	35	7/29/13	 View
 """

draw,won,lost = "draw", "won", "lost"

ss = [x.strip() for x in s.strip().split("\n")]
ss.reverse()
White = []
MyRating = []
OtherRating = []
Moves = []
Score = []
for sx in ss: 
    outcome = sx.split("\t")[2]
    if draw in outcome:
        Score.append(0.5)
    elif won in outcome:
        Score.append(1.0)
    elif lost in outcome:
        Score.append(0.0)
    Moves.append(sx.split("\t")[4])
    player_a = sx.split("\t")[0] 
    player_b = sx.split("\t")[1] 
    if player_a.startswith("Duco"): 
        White.append(1)
        duco = player_a 
        other = player_b
    else:
        White.append(0)
        duco = player_b
        other = player_a
    MyRating.append(duco.split("(")[1].split(")")[0]) 
    OtherRating.append(other.split("(")[1].split(")")[0]) 

print "MyRating, OtherRating, Score, Moves, White"
for x in range(len(Moves)): 
    print "{0},{1},{2},{3},{4}".format(MyRating[x],OtherRating[x],Score[x],Moves[x],White[x]) 
    