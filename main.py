"""""""""""""""""
CHESS SIMULATOR V1
"""""""""""""""""

"""
IMPORTS
"""
import numpy as np
from matplotlib import pyplot as plt


class chess_board():
    def __init__(self, board_size=(8,8)):
        self.board = np.zeros(shape=board_size, dtype="<U5")
        self.set_pieces()

    def __str__(self):
          counter=8
          rows = []
          for row in self.board:
                #print(f"row in self.board {row}")
                rows.append(" +" + "----+" * 8)
                formatted_row = []
                for piece in row:
                      #print(f"Each piece in row {piece}")
                      formatted_row.append(f"{piece:^4}")
                rows.append(f"{counter}" + "|" + "|".join(formatted_row) +"|")
                counter-=1
          rows.append(" +" + "----+" * 8)
          rows.append("    A    B    C    D    E    F    G    H")
          return "\n".join(rows) 


    def set_pieces(self):
        bpawn = "bP"
        wpawn = "wP"
        white_pieces = ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        black_pieces = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
        for i in range(8):
            self.board[1,i] = bpawn                                             #When you access board from here, numpy numerical indexing. Only when accessing board as a class does it
            self.board[6,i] = wpawn
            self.board[0, i] = black_pieces[i]
            self.board[7, i] = white_pieces[i]

    def dictionary(self):
        dictionary = {"A1" : (7,0),"A2" : (6,0),"A3" : (5,0),"A4" : (4,0),
                      "A5" : (3,0),"A6" : (2,0),"A7" : (1,0),"A8" : (0,0),
                      "B1" : (7,1),"B2" : (6,1),"B3" : (5,1),"B4" : (4,1),
                      "B5" : (3,1),"B6" : (2,1),"B7" : (1,1),"B8" : (0,1),
                      "C1" : (7,2),"C2" : (6,2),"C3" : (5,2),"C4" : (4,2),
                      "C5" : (3,2),"C6" : (2,2),"C7" : (1,2),"C8" : (0,2),
                      "D1" : (7,3),"D2" : (6,3),"D3" : (5,3),"D4" : (4,3),
                      "D5" : (3,3),"D6" : (2,3),"D7" : (1,3),"D8" : (0,3),
                      "E1" : (7,4),"E2" : (6,4),"E3" : (5,4),"E4" : (4,4),
                      "E5" : (3,4),"E6" : (2,4),"E7" : (1,4),"E8" : (0,4),
                      "F1" : (7,5),"F2" : (6,5),"F3" : (5,5),"F4" : (4,5),
                      "F5" : (3,5),"F6" : (2,5),"F7" : (1,5),"F8" : (0,5),
                      "G1" : (7,6),"G2" : (6,6),"G3" : (5,6),"G4" : (4,6),
                      "G5" : (3,6),"G6" : (2,6),"G7" : (1,6),"G8" : (0,6),
                      "H1" : (7,7),"H2" : (6,7),"H3" : (5,7),"H4" : (4,7),
                      "H5" : (3,7),"H6" : (2,7),"H7" : (1,7),"H8" : (0,7)}

        return dictionary

    def __getitem__(self, key):
        if key in self.dictionary():
            coordinate = self.dictionary()[key]
            return self.board[coordinate]
        else:
            raise ValueError("Incorrect square selected, please try again")

    def __setitem__(self, key, piece):
         if key in self.dictionary():
                    coordinate = self.dictionary()[key]
                    self.board[coordinate] = piece
         else:
              raise ValueError("Incorrect square selected, please try again")


    def pawn_moves(self, old_position, new_position, colour, is_legal=False):
           old_coordinate = self.dictionary()[old_position]                    #Legal moves should go through __set_item__ before being placed. Then we can do arithmetic on coordinates
           new_coordinate = self.dictionary()[new_position]
           diff = tuple(map(lambda x, y: x - y, old_coordinate, new_coordinate)) #Rather than chess positions
           print(f"Difference: {diff}")
           print(f"Colour: {colour}")
           if diff == (0,0):
                        return is_legal
           if colour == "w":
                if old_coordinate[0] == 6:    
                    if diff in [(1,0), (2,0)]:
                        if self.board[new_coordinate] == "":                       # So we don't go into occupied squares
                            is_legal = True
                elif diff in [(1,0)]:
                        if self.board[new_coordinate] == "":                       # So we don't go into occupied squares
                            is_legal = True  
                      
                elif diff in [(1,1), (1,-1)]:
                    if self.board[new_coordinate] != "":   
                        if self.board[new_coordinate][0] != "w":
                            is_legal = True
           else:
                if old_coordinate[0] == 1:
                    if diff in [(-1,0), (-2,0)]:
                        if self.board[new_coordinate] == "":                   # So we don't go into occupied squares
                            is_legal = True
                elif diff in [(-1,0)]:
                       if self.board[new_coordinate] == "":                    # So we don't go into occupied squares
                            is_legal = True  
                elif diff in [(-1,1), (-1,-1)]:
                    if self.board[new_coordinate] != "":
                        if self.board[new_coordinate][0] != "b":   
                            is_legal = True
                
           return is_legal

    def knight_moves(self, old_position, new_position, colour, is_legal=False):
         old_coordinate = self.dictionary()[old_position]                       #Legal moves should go through __set_item__ before being placed. Then we can do arithmetic on coordinates
         new_coordinate = self.dictionary()[new_position]
         diff = tuple(map(lambda x, y: x - y, old_coordinate, new_coordinate)) #Rather than chess positions
         print(f"Difference: {diff}")
         print(f"Colour: {colour}")
         if diff == (0,0):
                    return is_legal
         if diff in [(2,1), (2,-1), (-2,1), (-2,-1)]:
                            if self.board[new_coordinate] == "":               # So we don't go into occupied squares
                                is_legal = True
                            elif self.board[new_coordinate] != "":
                                if colour == "w":   
                                    if self.board[new_coordinate][0] != "w":
                                        is_legal = True
                                else:
                                    if self.board[new_coordinate][0] != "b":
                                        is_legal=True  
         return is_legal

    def bishop_moves(self, old_position, new_position, colour, is_legal=False):
             old_coordinate = self.dictionary()[old_position]                       #Legal moves should go through __set_item__ before being placed. Then we can do arithmetic on coordinates
             new_coordinate = self.dictionary()[new_position]
             diff = tuple(map(lambda x, y: x - y, old_coordinate, new_coordinate)) #Rather than chess positions
             print(f"Difference: {diff}")
             print(f"Colour: {colour}")
             if diff == (0,0):
                    return is_legal
             if abs(diff[0]) == abs(diff[1]):
                                print("Difference found for bishop")
                                if self.board[new_coordinate] == "":               # So we don't go into occupied squares
                                    is_legal = True
                                elif self.board[new_coordinate] != "":
                                    if colour == "w":   
                                        if self.board[new_coordinate][0] != "w":
                                            is_legal = True
                                    else:
                                        if self.board[new_coordinate][0] != "b":
                                            is_legal=True  

             return is_legal

    def rook_moves(self, old_position, new_position, colour, is_legal=False):
                 old_coordinate = self.dictionary()[old_position]                       #Legal moves should go through __set_item__ before being placed. Then we can do arithmetic on coordinates
                 new_coordinate = self.dictionary()[new_position]
                 diff = tuple(map(lambda x, y: x - y, old_coordinate, new_coordinate)) #Rather than chess positions
                 print(f"Difference: {diff}")
                 print(f"Colour: {colour}")
                 if diff == (0,0):
                        return is_legal
                 if (diff[0] == 0 and diff[1] != 0) or (diff[1] == 0 and diff[0] != 0):
                                             if self.board[new_coordinate] == "":               # So we don't go into occupied squares
                                                 is_legal = True
                                             elif self.board[new_coordinate] != "":
                                                 if colour == "w":   
                                                     if self.board[new_coordinate][0] != "w":
                                                         is_legal = True
                                                 else:
                                                     if self.board[new_coordinate][0] != "b":
                                                         is_legal=True  
                 return is_legal

    def queen_moves(self, old_position, new_position, colour, is_legal=False):
                 old_coordinate = self.dictionary()[old_position]                       #Legal moves should go through __set_item__ before being placed. Then we can do arithmetic on coordinates
                 new_coordinate = self.dictionary()[new_position]
                 diff = tuple(map(lambda x, y: x - y, old_coordinate, new_coordinate)) #Rather than chess positions
                 print(f"Difference: {diff}")
                 print(f"Colour: {colour}")
                 if diff == (0,0):
                        return is_legal
                 if self.board[new_coordinate] == "":               # So we don't go into occupied squares
                    is_legal = True
                 elif self.board[new_coordinate] != "":
                    if colour == "w":   
                        if self.board[new_coordinate][0] != "w":
                            is_legal = True
                    else:
                        if self.board[new_coordinate][0] != "b":
                            is_legal=True  
                 return is_legal

    def king_moves(self, old_position, new_position, colour, is_legal=False):
                     old_coordinate = self.dictionary()[old_position]                       #Legal moves should go through __set_item__ before being placed. Then we can do arithmetic on coordinates
                     new_coordinate = self.dictionary()[new_position]
                     diff = tuple(map(lambda x, y: x - y, old_coordinate, new_coordinate)) #Rather than chess positions
                     print(f"Difference: {diff}")
                     print(f"Colour: {colour}")
                     if diff == (0,0):
                           return is_legal
                     if diff in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
                        if self.board[new_coordinate] == "":               # So we don't go into occupied squares
                            is_legal = True
                        elif self.board[new_coordinate] != "":
                            if colour == "w":   
                                if self.board[new_coordinate][0] != "w":
                                    is_legal = True
                     else:
                            if self.board[new_coordinate][0] != "b":
                                is_legal=True  
                     return is_legal

    def check_other_pieces(self, differences, piece, colour):
          diff_1, diff_2 = differences


    def pieces_dictionary(self):
          dictionary = {"P" : "Pawn", "R": "Rook", "N" : "Knight", "Q" : "Queen",
                        "K" : "King", "B" : "Bishop"}
          return dictionary
      
                       
if __name__ == "__main__":
        board = chess_board()
        print(board)
        i = 0
        while i < 10:
            if i % 2 == 0:
                colour="w"
                square_to_move = input("White to move. Select square piece ")
                piece = board[square_to_move]
                #print(piece[1])
                #dict = board.dictionary()
                #print(board.pieces_dictionary())
                print(f"{board.pieces_dictionary()[piece[1]]} selected at {square_to_move} ")
                where_to_move = input("Where to move? ") 
            else:
                colour="b"
                square_to_move = input("Black to move. Select square piece ")
                piece = board[square_to_move]
                print(f"{board.pieces_dictionary()[piece[1]]} selected at {square_to_move} ")
                where_to_move =  input(f"{board[square_to_move]} selected. Where to move? ") 

        
            #print(colour)
            #print(piece)
            if piece != "":
                if piece[1] == "P":
                    legal = board.pawn_moves(square_to_move, where_to_move, colour)
                    print(f"Pawn {legal}")
                elif piece[1] == "N":
                    legal = board.knight_moves(square_to_move, where_to_move, colour)
                    print(f"Knight {legal}")
                elif piece[1] == "B":
                    legal = board.bishop_moves(square_to_move, where_to_move, colour)
                    print(f"Bishop {legal}")
                elif piece[1] == "R":
                    legal = board.rook_moves(square_to_move, where_to_move, colour)
                    print(f"Rook {legal}")
                elif piece[1] == "Q":
                    legal = board.queen_moves(square_to_move, where_to_move, colour)
                    print(f"Queen {legal}")
                elif piece[1] == "K":
                    legal = board.king_moves(square_to_move, where_to_move, colour)
                    print(f"King {legal}")
                                        
                if legal:
                    board[where_to_move] = piece
                    board[square_to_move] = ""
                    i+=1
            else:
                 print("Illegal move made. Please try again")
            print(board)










        

    