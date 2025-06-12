#!/usr/bin/env python3
import os
import chess
import chess.pgn
from state import State
import numpy as np

def get_dataset(num_samples=None):
    x,y=[],[]
    ng=0
    for fn in os.listdir("data"):
        pgn=open(os.path.join("data", fn))
        while 1:
            try:
                game=chess.pgn.read_game(pgn)
            except exception:
                break
            value={'1/2-1/2':0,'0-1':-1,'1-0':1}[game.headers['Result']]
            board=game.board()
            for i,move in enumerate(game.mainline_moves()):
                board.push(move)
                ser=State(board).serialized()[:,:,0]
                x.append(ser)
                y.append(value)
            print("parsing game %d got %d examples" %(ng,len(x)))
            if num_samples is not None and len(x)>num_samples:
                return x,y
            ng+=1
    x=np.array(x)
    y=np.array(y)
    return x,y
if __name__=="__main__":
    X,Y=get_dataset(1e6)
    np.savez("processed/dataset_1M.npz",X,Y)

