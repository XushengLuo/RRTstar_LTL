"""
__author__ = chrislaw
__project__ = RRT*_LTL
__date__ = 8/30/18
"""

from shapely.geometry import Point, Polygon


class problemFormulation(object):
    def __init__(self):
        # +----------------------------------------------+
        # |                                              |
        # |                 Problem 1                    |
        # |                                              |
        # +----------------------------------------------+


        # +-----+-----+-----+
        # |  l1 |     | l2  |
        # |     +-----+     |
        # |       l4        |
        # |             l3  |
        # |    +-------+    |
        # | l5 |       |    |
        # +----+-------+----+
        # l1: (0.2, 0.8)
        # l2: (0.8, 0.8)
        # l3: (0.8, 0.4)
        # l4: (0.4, 0.4)
        # l5: (0.1, 0.2)

        self.workspace = (1, 1)
        # !! no whitespace in atomic proposation      b:ball s:square
        r = 0.2
        self.ap = {'l1', 'l2', 'l3', 'l4', 'l5', 'l6'}

        # describe regions using shapely library
        # self.regions = {'l1': Point(0.2, 0.8).buffer(r),
        #                 'l2': Point(0.8, 0.8).buffer(r),
        #                 'l3': Point(0.8, 0.4).buffer(r),
        #                 'l4': Point(0.4, 0.4).buffer(r),
        #                 'l5': Point(0.1, 0.2).buffer(r),
        #                 # 'l6': Point(0.1, 0.5).buffer(r)
        #                 }
        center = [(0.2, 0.8), (0.8, 0.8), (0.8, 0.4), (0.4, 0.4), (0.1, 0.2), (0.1, 0.5)]
        # self.regions = {'l1': Polygon([(center[0][0] - r, center[0][1] - r), (center[0][0] + r, center[0][1] - r),
        #                                (center[0][0] + r, center[0][1] + r), (center[0][0] - r, center[0][1] + r)]),
        #                 'l2': Polygon([(center[1][0] - r, center[1][1] - r), (center[1][0] + r, center[1][1] - r),
        #                                (center[1][0] + r, center[1][1] + r), (center[1][0] - r, center[1][1] + r)]),
        #                 'l3': Polygon([(center[2][0] - r, center[2][1] - r), (center[2][0] + r, center[2][1] - r),
        #                                (center[2][0] + r, center[2][1] + r), (center[2][0] - r, center[2][1] + r)]),
        #                 'l4': Polygon([(center[3][0] - r, center[3][1] - r), (center[3][0] + r, center[3][1] - r),
        #                                (center[3][0] + r, center[3][1] + r), (center[3][0] - r, center[3][1] + r)]),
        #                 'l5': Polygon([(center[4][0] - r, center[4][1] - r), (center[4][0] + r, center[4][1] - r),
        #                                (center[4][0] + r, center[4][1] + r), (center[4][0] - r, center[4][1] + r)]),
        #                 'l6': Polygon([(center[5][0] - r, center[5][1] - r), (center[5][0] + r, center[5][1] - r),
        #                                (center[5][0] + r, center[5][1] + r), (center[5][0] - r, center[5][1] + r)])
        #                 }
        center = [(0.1, 0.7), (0.7, 0.7), (0.7, 0.3), (0.3, 0.3), (0, 0.1), (0, 0.4)]

        self.regions = {'l1': Polygon([(center[0][0], center[0][1]), (center[0][0] + r, center[0][1]),
                                       (center[0][0], center[0][1] + r)]),
                        'l2': Polygon([(center[1][0], center[1][1]), (center[1][0] + r, center[1][1]),
                                       (center[1][0], center[1][1] + r)]),
                        'l3': Polygon([(center[2][0], center[2][1]), (center[2][0] + r, center[2][1]),
                                       (center[2][0], center[2][1] + r)]),
                        'l4': Polygon([(center[3][0], center[3][1]), (center[3][0] + r, center[3][1]),
                                       (center[3][0], center[3][1] + r)]),
                        'l5': Polygon([(center[4][0], center[4][1]), (center[4][0] + r, center[4][1]),
                                       (center[4][0], center[4][1] + r)]),
                        'l6': Polygon([(center[5][0], center[5][1]), (center[5][0] + r, center[5][1]),
                                       (center[5][0], center[5][1] + r)]),
                        }

        self.obs = {'o1': Polygon([(0.3, 0.0), (0.7, 0.0), (0.7, 0.2), (0.3, 0.2)]),
                    'o2': Polygon([(0.4, 0.7), (0.6, 0.7), (0.6, 1.0), (0.4, 1.0)])}

        init_state = []
        for i in range(1):
            init_state.append((0.8, 0.1))
        self.init_state = tuple(init_state)
        # self.init_state = ((0.8, 0.1),(0.8, 0.1),(0.8, 0.1),(0.8, 0.1),(0.8, 0.1),(0.8, 0.1),(0.8, 0.1),(0.8, 0.1))
        # self.init_state = ((0.8, 0.1),(0.8, 0.1),(0.8, 0.1),(0.8, 0.1),(0.8, 0.1),(0.8, 0.1))
        # self.init_state = ((0.8, 0.1),(0.8, 0.1),(0.8, 0.1),(0.8, 0.1))
        # self.init_state = ((0.8, 0.1), (0.9, 0.1))
        # self.init_state = ((0.8, 0.1), )
        self.uni_cost = 0.1

        # #----------------------------------------------#
        # |                                              |
        # |                 Problem 2                    |
        # |                                              |
        # #----------------------------------------------#

        # +-----+-----+-----+
        # | r4,b|r5,rb| r6  |
        # +-----+-----+-----+
        # | c1  | c2  | c3  |
        # +-----+-----+-----+
        # | r1  | r2,b|r3,gb|
        # +-----+-----+-----+

        # self.ap = {'l1', 'l2', 'l3', 'l4', 'l5'}
        # self.workspace = (1, 1)
        # # !! no whitespace in atomic proposation      b:ball s:square
        # self.regions = {('l1', 'b'): (0.2, 0.8, 0.1),
        #                 ('l2', 'b'): (0.8, 0.8, 0.1),
        #                 ('l3', 'b'): (0.8, 0.4, 0.1),
        #                 ('l4', 'b'): (0.4, 0.4, 0.1),
        #                 ('l5', 'b'): (0.1, 0.2, 0.1)}
        # # self.obs = {('o1', 'p'): ((0, 1, -1), (1, 0, -0.6), (0, -1, 0.7), (-1, 0, 0.4)),  # coefficient <=0
        # #             ('o2', 'p'): ((0, 1, -0.2), (1, 0, -0.7), (0, -1, 0), (-1, 0, 0.3)),
        # #             ('o3', 'p'): ((1, 1, -1), (-1, 1, 0.2), (0, -1, 0.2)),
        # #             ('o4', 'b'): (0.3, 0.6, 0.1)
        # #             }
        # self.obs = {}
        # self.init_state = (0.8, 0.1)
        # self.uni_cost = 0.1


        """
        +----------------------------+
        |   Propositonal Symbols:    |
        |        true, false         |
        |	    any lowercase string |
        |                            |
        |   Boolean operators:       |
        |       !   (negation)       |
        |       ->  (implication)    |
        |	    <-> (equivalence)    |
        |       &&  (and)            |
        |       ||  (or)             |
        |                            |
        |   Temporal operators:      |
        |       []  (always)         |
        |       <>  (eventually)     |
        |       U   (until)          |
        |       V   (release)        |
        |       X   (next)           |
        +----------------------------+
        """

        # self.formula = '<>(l3 && []<>l4)'
        # self.formula = '<> (l11) &&   [](<> ( l21 && <> (l31 && <> l41 ) ) )'
        # ---------------------------- case 1 --------------------------------
        # self.formula = '<> l4_1 && []<> (l3_1 && <> l1_1) && (!l1_1 U l2_1)  && []!l5_1'
        self.formula = '<> e1 && []<> (e2  && <> e3) && (!e3 U e4)  && []!e5'

        self.formula_comp = {1: '(l4_1)',
                             2: '(l3_1)',
                             3: '(l1_1)',
                             4: '(l2_1)',
                             5: '(l5_1)',
                             }
        self.exclusion = [('e1','e2'), ('e1','e3'),('e1','e3'),('e1','e4'),('e1','e5'),('e2','e3'),('e2','e4'),('e2','e5'),('e3','e4'),('e3','e5'),('e4','e5')]
        self.no = ['l5_1','l1_1']
        # #---------------------------- case 2 --------------------------------
        # self.formula = '[]<>l1_1 && [](l1_1 -> X(!l1_1 U l2_2))'
        # self.formula = '[]<> e1 && []<> e2 && []<> (e3 && <> e4)'
        # self.formula_comp = {1: '(l1_1)',
        #                      2: '(l2_2)',
        #                      3: '(l4_1)',
        #                      4: '(l4_2)'}
        #
        # self.exclusion = []
        # self.no = []

        # ---------------------------- case 3 --------------------------------
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6))'
        # self.formula_comp = {1: '(l1_1 && l1_2)',
        #                      2: '(l2_2 && l2_3)',
        #                      3: '(l3_3 && l3_4)',
        #                      4: '(l4_1)',
        #                      5: '(l5_4)',
        #                      6: '(l6_3)'}
        # self.exclusion = [('e1', 'e2'), ('e1', 'e4'), ('e2','e3'), ('e2','e6'), ('e3','e5')]
        # self.no = []
        # # ---------------------------- case 4 --------------------------------
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6))'
        # self.formula_comp = {
        #                      1: '(l1_1 && (l1_2 || l1_3) && (l1_10 || l1_13))',
        #                      2: '(l2_4 && (l2_5 || l2_6) && (l2_11 || l2_14))',
        #                      3: '(l3_7 && (l3_8 || l3_9) && (l3_12 || l3_15))',
        #                      4: '(l4_1)',
        #                      5: '(l5_4)',
        #                      6: '(l6_7)'}
        # # ---------------------------- case 5 --------------------------------
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6))'
        # self.formula_comp = {
        #     1: '(l1_1 && (l1_2 || l1_3) && (l1_10 || l1_13) && l1_4)',
        #     2: '(l2_4 && (l2_5 || l2_6) && (l2_11 || l2_14) && l2_7)',
        #     3: '(l3_7 && (l3_8 || l3_9) && (l3_12 || l3_15) && l3_16)',
        #     4: '(l4_1)',
        #     5: '(l5_4)',
        #     6: '(l6_7)'}
        # self.exclusion = [('e1', 'e2'), ('e1', 'e4'), ('e1', 'e5'), ('e2', 'e3'), ('e2', 'e5'), ('e2', 'e6'),
        #                   ('e3', 'e6')]
        # self.no = []

        # ---------------------------- case 6 -------------------good-------------
        # self.formula = '[]<> e1 && []!e2'
        # self.formula_comp = {
        #     1: '(l2_1 )',
        #     2: '(l3_1)'}  # '(l3_13 || l3_14)' ok  (l3_13 || l3_11)  ok
        # self.exclusion = []
        # self.no = ['l3_1']

        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6)) && []!e7'
        # self.formula_comp = {
        #                      1: '(l1_1 && (l1_2 || l1_3) && (l1_10 || l1_13) && l1_4)',
        #                      2: '(l2_4 && (l2_5 || l2_6) && (l2_11 || l2_14) && l2_7)',
        #                      3: '(l3_7 && (l3_8 || l3_9) && (l3_12 || l3_15) && l3_16)',
        #                      4: '(l4_1)',
        #                      5: '(l5_4)',
        #                      6: '(l6_7)',
        #                      7: '(l3_11 || l3_10)'}  #'(l3_13 || l3_14)' ok  (l3_13 || l3_11)  ok
        # self.exclusion = [('e1', 'e2'), ('e1', 'e4'), ('e1','e5'), ('e2','e3'), ('e2','e5'), ('e2','e6'), ('e3','e6')]
        # self.no = ['l3_11','l3_10']
        # ---------------------------- case 7 --------------------------------
        # # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6)) && []!e7 && [](!e6 U e4)'  # 212.44136 14.196864 6.675931049455233 4.894404948592937
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6)) && []!e7 && [](e6 -> X(!e6 U e4))'
        # self.formula_comp = {
        #     1: '(l1_1 && (l1_2 || l1_3) && (l1_10 || l1_13) && l1_4)',
        #     2: '(l2_4 && (l2_5 || l2_6) && (l2_11 || l2_14) && l2_7)',
        #     3: '(l3_7 && (l3_8 || l3_9) && (l3_12 || l3_15) && l3_16)',
        #     4: '(l4_1)',
        #     5: '(l5_4)',
        #     6: '(l6_7)',
        #     7: '(l3_10 || l3_11)'}
        # self.exclusion = [('e1', 'e2'), ('e1', 'e4'), ('e1', 'e5'), ('e2', 'e3'), ('e2', 'e5'), ('e2', 'e6'),
        #                   ('e3', 'e6')]
        # self.no = ['l6_7', 'l3_10', 'l3_11']
        # ---------------------------- case 8 --------------------------------
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6)) && []!e7 && [](e6 -> X(!e6 U e4)) && <> e8'
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6)) && []!e7 && <> e8'
        #
        # self.formula_comp = {
        #     1: '(l1_1 && (l1_2 || l1_3) && (l1_10 || l1_13) && l1_4)',
        #     2: '(l2_4 && (l2_5 || l2_6) && (l2_11 || l2_14) && l2_7)',
        #     3: '(l3_7 && (l3_8 || l3_9) && (l3_12 || l3_15) && l3_16)',
        #     4: '(l4_1)',
        #     5: '(l5_4)',
        #     6: '(l6_7)',
        #     7: '(l3_10 || l3_11)',
        #     8: '(l4_3 && l5_6 && l6_9)'}
        # # #
        # self.exclusion = [('e1', 'e2'), ('e1', 'e4'), ('e1','e5'), ('e2','e3'), ('e2','e5'), ('e2','e6'), ('e3','e6')]
        # self.no = ['l3_10','l3_11'] #, 'l6_7',
        # ---------------------------- case 9 --------------------------------
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6)) && []!e7 && [](e6 -> X(!e6 U e4)) && <> e8 && [](e5 -> X(!e5 U e4))'
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6)) ' \
        #                '&& []!e7 && <> e8 && []<>e9 && (!e8 U e9)'
        # self.formula_comp = {
        #     1: '(l1_1 && (l1_2 || l1_3) && (l1_10 || l1_13) && l1_4)',
        #     2: '(l2_4 && (l2_5 || l2_6) && (l2_11 || l2_14) && l2_7)',
        #     3: '(l3_7 && (l3_8 || l3_9) && (l3_12 || l3_15) && l3_16)',
        #     4: '(l4_1)',
        #     5: '(l5_4)',
        #     6: '(l6_7)',
        #     7: '(l3_10 || l3_11)',
        #     8: '(l4_3 && l5_6 && l6_9 )',
        #     9: '(l2_17 && l2_18 && l4_19 & l4_20)'}
        # #
        # self.exclusion = [('e1', 'e2'), ('e1', 'e4'), ('e1', 'e5'), ('e2', 'e3'), ('e2', 'e5'), ('e2', 'e6'),
        #                   ('e3', 'e6')]
        # self.no = ['l6_7', 'l3_10', 'l3_11']
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6)) && []!e7 && [](e6 -> X(!e6 U e4)) && <> e8 && (!e8 U e9) && []<> e_10'
        # self.formula_comp = {
        #     1: '(l1_1 && (l1_2 || l1_3) && (l1_10 || l1_13) && l1_4)',
        #     2: '(l2_4 && (l2_5 || l2_6) && (l2_11 || l2_14) && l2_7)',
        #     3: '(l3_7 && (l3_8 || l3_9) && (l3_12 || l3_15))',
        #     4: '(l4_1)',
        #     5: '(l5_4)',
        #     6: '(l6_7)',
        #     7: '(l3_10 || l3_11)',
        #     8: '(l4_3 && l5_6 && l6_9)',
        #     9: '(l5_16 && l5_17)',
        #     10: '(l6_17 && l6_18 && l6_19 && l6_20)',
        # }
        # # #
        # self.exclusion = [('e1', 'e2'), ('e1', 'e4'), ('e1','e5'), ('e2','e3'), ('e2','e5'), ('e2','e6'), ('e3','e6'), ('e9', 'e_10')]
        # self.no = ['l6_7','l3_10','l3_11', 'l4_3', 'l5_6' ,'l6_9']
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && []<>(e4 && <>(e5 && <> e6)) && <> e7 && []<> e8' #&& [](e8 -> X(!e8 U e9))'
        # self.formula_comp = {
        #                         1: '(l1_1 && (l1_2 || l2_2) && (l1_3 || l2_3) && l1_4)',
        #                         2: '(l2_4 && (l2_5 || l3_5) && (l2_6 || l3_6) && l2_7)',
        #                         3: '(l3_7 && (l3_8 || l4_8) && (l3_9 || l4_9) && l3_10)',
        #                         4: '(l4_1)',
        #                         5: '(l5_4)',
        #                         6: '(l6_7)',
        #                         7: '(l4_11 && (l4_12 || l5_12) && (l4_13 || l5_13) && l4_14)',
        #                         8: '(l5_14 && (l5_15 || l6_15) && (l5_16 || l6_16) && l5_17)',
        #                         9: '(l6_17 && (l6_18 || l6_19 || l6_20))',
        #                         10: '(l1_11)',
        #                         11: '(l2_14)',
        #                         12: '(l3_17)',
        # }
        # self.exclusion = [('e1', 'e_2'), ('e1', 'e4'), ('e1', 'e5'), ('e2', 'e3'), ('e2', 'e5'), ('e2', 'e6'), ('e3', 'e6'),
        #                   # ('e7', 'e8'), ('e8', 'e9')]
        #                   ('e7', 'e8'), ('e7', 'e_10'), ('e7', 'e_11'), ('e8', 'e9'), ('e8', 'e_11'), ('e8', 'e_12'), ('e9', 'e_12')]
        # self.no = []
        # # ---------------------------- case 10--------------------------------
        # self.formula = '[]<> e1 && []<> e2 && []<> e3 && [](e4 -> X(!e4 U e5)) && []!e6'
        # self.formula_comp = {
        #                     1: '(l1_1 && (l1_4 || l1_7) && (l1_10 || l1_13) && l1_2)',
        #                     2: '(l2_2 && (l2_5 || l2_8) && (l2_11 || l2_14) && l2_3)',
        #                     3: '(l3_3 && (l3_6 || l3_9) && (l3_12 || l3_15))',
        #                     4: '(l4_1 && l6_3)',
        #                     5: '(l5_2)',
        #                     6: '(l3_15 && l3_10)',
        #                     7: '(l4_16 && (l4_17 || l4_18) && l5_19 && (l5_20 || l5_21))',
        #                     8: '(l6_22 && (l6_23 || l6_24))',
        #                     9: '(l4_16 && (l4_17 || l4_18) && l5_19 && (l5_20 || l5_21))'}
        # regions with ! in front of it
        # self.no = []
        # self.formula = '[]<> e1 '
        # self.formula_comp = {1: '(l3_10 || l3_11)',
        #                      }
        # self.formula = '[]<> l11 && [](l11 -> l22) && (l31 && <>l42)'
        # self.formula = '<>l4 && []<>l1 && [](l1 -> X(!l1 U l2)) && []<>l3 && []!l5'
        # self.formula = '<>l4 && []<>l1 && []<>l5'  # formula 1
        # self.formula =  '<>(rb && <>b) && <>[]r1 && [](rb -> X(!gb U b)) && <>(gb && <>b) && [](gb -> X(!rb U b))'  # \phi 2
        # self.formula = '<>(rb && <>(b && r2)) && <>[]r1 && [](rb -> X(!gb U b)) && <>(gb && <>(b && r4)) && [](gb -> X(!rb U b))'   #\phi 3
        # self.formula = '([]<>r4) && ([]<>r3) && ([]<>r6)'     # \phi 4 inspect room r3, r4, r6 infinitely often
        # self.formula = 'gb U b'

    def Formulation(self):
        # print('Task specified by LTL formula: ' + self.formula)
        return self.workspace, self.regions, self.obs, self.init_state, self.uni_cost, self.formula, self.formula_comp, self.exclusion, self.no
