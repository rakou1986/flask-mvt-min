#!/usr/bin/env python
#coding: utf-8

from flask import render_template, Blueprint

# bp ではなく app とする例もあるが、見分けやすいよう bp という名前で。
bp = Blueprint("admin", __name__) # 第一引数はurl_for用

@bp.route("/")
def index():
  """
  管理者用ページの機能一覧
  URLは /admin/

  これは webapp/__init__.py で定義している。
  """
  # webapp/templates/ 配下でファイルを探してレンダ
  return render_template("admin_index.html")
