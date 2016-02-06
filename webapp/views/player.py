#!/usr/bin/env python
#coding: utf-8

from flask import render_template, Blueprint

from webapp import services

# bp ではなく app とする例もあるが、見分けやすいよう bp という名前で。
bp = Blueprint("player", __name__) # 第一引数はurl_for用

@bp.route("/list/")
def list():
  """
  ある対戦ゲームのプレイヤーリスト。
  URLは /player/list/

  /player/ の部分は webapp/__init__.py で定義している。
  """
  players = services.get_all_players()
  # webapp/templates/ 配下でファイルを探してレンダ
  return render_template("player_list.html", players=players)
