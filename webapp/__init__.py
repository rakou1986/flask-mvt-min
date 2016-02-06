#!/usr/bin/env python
#coding: utf-8

from webapp.app import app

from webapp.views import admin, player

app.register_blueprint(admin.bp, url_prefix="/admin")
app.register_blueprint(player.bp, url_prefix="/player")
