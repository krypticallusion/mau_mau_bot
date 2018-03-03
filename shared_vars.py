#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from config import TOKEN,URL, WORKERS
import logging
from telegram.ext import Updater

from game_manager import GameManager
from database import db

db.bind('sqlite', 'uno.sqlite3', create_db=True)
db.generate_mapping(create_tables=True)

gm = GameManager()

def updater_process():
    updater = Updater(token=TOKEN, workers=WORKERS)
    updater.start_webhook(listen='0.0.0.0',
                      port=8443,
                      url_path=TOKEN,
                      key='private.key',
                      cert='cert.pem',
                      webhook_url=URL:8443/TOKEN)
    updater.idle()

dispatcher = updater.dispatcher
