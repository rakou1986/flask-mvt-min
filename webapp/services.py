#!/usr/bin/env python
#coding: utf-8

"""
viewsが必要とするDBアクセスなどviewsに書くと
viewsの見通しが悪くなりそうな処理はここに書く。

services/__init__.py を作ってviewsの名称に対応して細分化してもよい。
"""

def get_all_players():
  players = ["player1", "player2", "player3"]
  return players
